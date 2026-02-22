"""
Principio de Coste de Concentración (PCC) — Experimento de difusión en red
=========================================================================

Protocolo unificado para replicación independiente.
Genera resultados comparables con métricas estandarizadas.

Uso:
    python experimento_pcc.py

Parámetros por defecto: N=50, p=0.15, 500 pasos, 5 realizaciones.
Genera CSV con resultados y gráfico PNG.

Autor: Diego-dcv
Colaboración: Claude (Anthropic), ChatGPT (OpenAI), DeepSeek, Grok (xAI)
Fecha: Febrero 2026
Licencia: CC BY 4.0
"""

import numpy as np
import csv
import os

# ─── PARÁMETROS ───────────────────────────────────────────────────────
N = 50                           # Número de nodos
P_CONEXION = 0.15                # Probabilidad de conexión (Erdős-Rényi)
PASOS = 500                      # Pasos temporales por modo
NU_RANGE = np.linspace(0.01, 0.5, 20)  # Barrido de viscosidad/difusividad
REALIZACIONES = 5                # Semillas aleatorias para promediar
OBJETIVO = 0.8                   # Fracción de energía concentrada (Modo A)
NODO_OBJETIVO = 0                # Nodo donde se concentra (Modo A)
VENTANA_RESIDUAL = 50            # Últimos N pasos para coste_B

# ─── FUNCIONES ────────────────────────────────────────────────────────

def generar_red(n, p, semilla):
    """Genera red aleatoria Erdős-Rényi como lista de vecinos."""
    rng = np.random.default_rng(semilla)
    # Matriz de adyacencia simétrica
    adj = rng.random((n, n)) < p
    adj = np.triu(adj, k=1)
    adj = adj | adj.T
    np.fill_diagonal(adj, False)
    vecinos = [np.where(adj[i])[0].tolist() for i in range(n)]
    return vecinos, adj


def paso_difusion(energia, vecinos, nu, n):
    """Un paso de difusión en red. Devuelve nueva energía."""
    transferencias = np.zeros(n)
    for i in range(n):
        for j in vecinos[i]:
            if i < j:
                diff = energia[i] - energia[j]
                flujo = nu * diff * 0.1
                transferencias[i] -= flujo
                transferencias[j] += flujo
    energia_nueva = energia + transferencias
    energia_nueva = np.maximum(energia_nueva, 0)
    # Renormalizar a energía total = 1
    s = energia_nueva.sum()
    if s > 0:
        energia_nueva /= s
    return energia_nueva


def disipacion_gradiente(energia, adj, nu):
    """Disipación como energía de gradiente en el grafo: ν × E^T L E."""
    # L = D - A (Laplaciano); E^T L E = Σ_{(i,j)} (E_i - E_j)^2
    diff_sq = 0.0
    n = len(energia)
    for i in range(n):
        for j in range(i+1, n):
            if adj[i, j]:
                diff_sq += (energia[i] - energia[j]) ** 2
    return nu * 0.1 * diff_sq


def modo_a(vecinos, adj, nu, n, pasos, objetivo, nodo):
    """Modo A: mantener concentración. Devuelve (coste_inyeccion, disipacion_acumulada)."""
    # Iniciar desde estado concentrado (80% en nodo objetivo)
    energia = np.ones(n) * (1.0 - objetivo) / (n - 1)
    energia[nodo] = objetivo
    coste_inyeccion = 0.0
    disipacion = 0.0
    
    for _ in range(pasos):
        energia = paso_difusion(energia, vecinos, nu, n)
        disipacion += disipacion_gradiente(energia, adj, nu)
        
        # Inyectar para mantener objetivo
        actual = energia[nodo]
        if actual < objetivo:
            inyeccion = objetivo - actual
            coste_inyeccion += inyeccion
            energia[nodo] = objetivo
            # Renormalizar el resto para mantener energía total = 1
            otros_idx = [i for i in range(n) if i != nodo]
            otros_sum = energia[otros_idx].sum()
            if otros_sum > 0:
                factor = (1.0 - objetivo) / otros_sum
                for i in otros_idx:
                    energia[i] *= factor
    
    return coste_inyeccion, disipacion


def modo_b(vecinos, adj, nu, n, pasos, ventana):
    """Modo B: evolución libre. Devuelve (coste_residual, disipacion_acumulada)."""
    # Misma condición inicial que Modo A: estado concentrado
    energia = np.ones(n) * (1.0 - OBJETIVO) / (n - 1)
    energia[NODO_OBJETIVO] = OBJETIVO
    desviaciones = []
    disipacion = 0.0
    
    for _ in range(pasos):
        energia = paso_difusion(energia, vecinos, nu, n)
        disipacion += disipacion_gradiente(energia, adj, nu)
        
        # Desviación del equilibrio uniforme (norma L2 = std)
        desviaciones.append(np.std(energia))
    
    # Coste B: promedio de desviación residual (últimos pasos) × 0.01
    coste_residual = np.mean(desviaciones[-ventana:]) * 0.01
    
    return coste_residual, disipacion


# ─── EJECUCIÓN PRINCIPAL ──────────────────────────────────────────────

def main():
    print(f"PCC Experiment: N={N}, p={P_CONEXION}, pasos={PASOS}, realizaciones={REALIZACIONES}")
    print(f"ν range: {NU_RANGE[0]:.3f} → {NU_RANGE[-1]:.3f} ({len(NU_RANGE)} puntos)")
    print("=" * 70)
    
    resultados = []
    
    for nu in NU_RANGE:
        ratios_clasico = []
        ratios_energetico = []
        
        for semilla in range(REALIZACIONES):
            vecinos, adj = generar_red(N, P_CONEXION, semilla)
            
            coste_a, diss_a = modo_a(vecinos, adj, nu, N, PASOS, OBJETIVO, NODO_OBJETIVO)
            coste_b, diss_b = modo_b(vecinos, adj, nu, N, PASOS, VENTANA_RESIDUAL)
            
            # Ratio clásico (protocolo original)
            if coste_b > 0:
                ratios_clasico.append(coste_a / coste_b)
            
            # Ratio energético (mejora ChatGPT: work_A / diss_B)
            if diss_b > 0:
                ratios_energetico.append(coste_a / diss_b)
        
        media_clasico = np.mean(ratios_clasico) if ratios_clasico else float('nan')
        std_clasico = np.std(ratios_clasico) if ratios_clasico else float('nan')
        media_energetico = np.mean(ratios_energetico) if ratios_energetico else float('nan')
        std_energetico = np.std(ratios_energetico) if ratios_energetico else float('nan')
        
        resultados.append({
            'nu': nu,
            'ratio_clasico_media': media_clasico,
            'ratio_clasico_std': std_clasico,
            'ratio_energetico_media': media_energetico,
            'ratio_energetico_std': std_energetico,
        })
        
        print(f"ν={nu:.3f} | clásico: {media_clasico:.2e} ± {std_clasico:.2e} | energético: {media_energetico:.2e} ± {std_energetico:.2e}")
    
    # ─── GUARDAR CSV ──────────────────────────────────────────────────
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'datos', 'resultados_pcc.csv')
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=resultados[0].keys())
        writer.writeheader()
        writer.writerows(resultados)
    
    print(f"\nResultados guardados en: {csv_path}")
    print("Experimento completado.")


if __name__ == '__main__':
    main()
