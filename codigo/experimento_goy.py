"""
PCC Test 2: Shell Model GOY — Test No Lineal del PCC
=====================================================
Integrador: IF-RK2 (Integrating Factor Runge-Kutta orden 2).
La disipación (-ν k² u) se trata exactamente vía factor exponencial.
La no linealidad se integra con Heun explícito en variables transformadas.

Parámetros por defecto: 15 shells, dt=5e-5, 30000+30000 pasos, 3 realizaciones.
"""

import numpy as np
import csv
import os

# ─── PARÁMETROS ──────────────────────────────────────────────────────
N_SHELLS = 15
K0 = 1.0
LAMBDA = 2.0
EPSILON = 0.5
DT = 5e-5
PASOS_TRANSIENTE = 30000
PASOS_MEDIDA = 30000
NU_RANGE = np.array([0.005, 0.01, 0.02, 0.05, 0.1, 0.2])
REALIZACIONES = 3
FORCING_AMP = 5.0
FRACCION_OBJETIVO = 0.8

A_COEF = 1.0
B_COEF = -EPSILON
C_COEF = -(1.0 - EPSILON)


# ─── MODELO GOY ──────────────────────────────────────────────────────

def make_k(n, k0, lam):
    return k0 * lam ** np.arange(n)


def nonlinear(u, k):
    """Término no lineal GOY: i * [a*k_n*u_{n+1}*u*_{n+2} + ...]"""
    N = len(u)
    nl = np.zeros(N, dtype=complex)
    nl[:N-2] += A_COEF * k[:N-2] * u[1:N-1] * np.conj(u[2:N])
    nl[1:N-1] += B_COEF * k[0:N-2] * u[0:N-2] * np.conj(u[2:N])
    nl[2:N] += C_COEF * k[0:N-2] * u[0:N-2] * np.conj(u[1:N-1])
    return 1j * nl


def step_ifrk2(u, k, nu, dt, forcing, E_full):
    """
    IF-RK2: Integrating Factor Runge-Kutta orden 2.
    E_full = exp(-nu * k² * dt) precalculado.
    
    du/dt = L*u + N(u) + f,  con L = -nu*k² (diagonal)
    
    1) N1 = N(u) + f
    2) u* = E*u + dt*E*N1            (Euler en variables IF)
    3) N2 = N(u*) + f
    4) u_new = E*u + dt/2*(E*N1 + N2) (Heun correction)
    """
    N1 = nonlinear(u, k) + forcing
    u_star = E_full * u + dt * E_full * N1
    N2 = nonlinear(u_star, k) + forcing
    u_new = E_full * u + 0.5 * dt * (E_full * N1 + N2)
    return u_new


def E_total(u):
    return 0.5 * np.sum(np.abs(u)**2)


def E_per_shell(u):
    return 0.5 * np.abs(u)**2


def dissipation_rate(u, k, nu):
    return nu * np.sum(k**2 * np.abs(u)**2)


# ─── MODO B: CASCADA LIBRE (turbulencia normal) ─────────────────────

def modo_b(nu, k, seed):
    """Forzamiento en shell grande, cascada libre hacia shells pequeñas."""
    rng = np.random.default_rng(seed)
    N = len(k)
    u = (rng.standard_normal(N) + 1j * rng.standard_normal(N)) * 1e-3
    
    f = np.zeros(N, dtype=complex)
    f[0] = FORCING_AMP * (1 + 0j)
    
    E_full = np.exp(-nu * k**2 * DT)
    
    for _ in range(PASOS_TRANSIENTE):
        u = step_ifrk2(u, k, nu, DT, f, E_full)
    
    diss_acum = 0.0
    for _ in range(PASOS_MEDIDA):
        u = step_ifrk2(u, k, nu, DT, f, E_full)
        diss_acum += dissipation_rate(u, k, nu) * DT
    
    return diss_acum


# ─── MODO A: CONCENTRACIÓN FORZADA EN SHELLS FINAS ──────────────────

def modo_a(nu, k, seed):
    """Mismo forzamiento + inyección continua para concentrar en shells altas."""
    rng = np.random.default_rng(seed)
    N = len(k)
    u = (rng.standard_normal(N) + 1j * rng.standard_normal(N)) * 1e-3
    
    f_base = np.zeros(N, dtype=complex)
    f_base[0] = FORCING_AMP * (1 + 0j)
    
    obj = list(range(N-3, N))  # últimas 3 shells
    E_full = np.exp(-nu * k**2 * DT)
    
    # Transiente con forzamiento normal
    for _ in range(PASOS_TRANSIENTE):
        u = step_ifrk2(u, k, nu, DT, f_base, E_full)
    
    # Medición: inyectar para mantener 80% en shells finas
    trabajo = 0.0
    for _ in range(PASOS_MEDIDA):
        u = step_ifrk2(u, k, nu, DT, f_base, E_full)
        
        Et = E_total(u)
        if Et < 1e-30:
            continue
        
        Ep = E_per_shell(u)
        E_obj = np.sum(Ep[obj])
        frac = E_obj / Et
        
        if frac < FRACCION_OBJETIVO:
            deficit = FRACCION_OBJETIVO - frac
            for s in obj:
                dE = deficit * Et / len(obj)
                if np.abs(u[s]) > 1e-30:
                    phase = u[s] / np.abs(u[s])
                else:
                    phase = 1.0 + 0j
                du = np.sqrt(max(2.0 * dE, 0)) * phase
                u[s] += du
                trabajo += dE
    
    return trabajo


# ─── MAIN ─────────────────────────────────────────────────────────────

def main():
    k = make_k(N_SHELLS, K0, LAMBDA)
    
    print("PCC Shell Model GOY — Test No Lineal")
    print(f"Shells={N_SHELLS}, lambda={LAMBDA}, epsilon={EPSILON}, dt={DT}")
    print(f"k_range: [{k[0]:.0f}, {k[-1]:.0e}]")
    print(f"Transiente={PASOS_TRANSIENTE}, Medida={PASOS_MEDIDA}, Runs={REALIZACIONES}")
    print(f"nu: {NU_RANGE}")
    print("=" * 70)
    
    resultados = []
    
    for nu in NU_RANGE:
        ratios = []
        cas, cbs = [], []
        
        for s in range(REALIZACIONES):
            print(f"  nu={nu:.4f} seed={s}", end=" -> ", flush=True)
            
            cb = modo_b(nu, k, s)
            ca = modo_a(nu, k, s)
            cas.append(ca)
            cbs.append(cb)
            
            if cb > 1e-30:
                r = ca / cb
                ratios.append(r)
                print(f"A={ca:.3e}  B={cb:.3e}  ratio={r:.2f}")
            else:
                print(f"A={ca:.3e}  B~0")
        
        rm = np.mean(ratios) if ratios else float('nan')
        rs = np.std(ratios) if ratios else float('nan')
        resultados.append({
            'nu': nu, 
            'ratio_media': rm, 
            'ratio_std': rs,
            'coste_a_media': np.mean(cas),
            'coste_b_media': np.mean(cbs)
        })
        
        tag = "PCC VALIDO" if rm > 1 else ("PCC FALLA" if not np.isnan(rm) else "SIN DATOS")
        print(f"  -- nu={nu:.4f}: ratio = {rm:.2f} +/- {rs:.2f} [{tag}]\n")
    
    # CSV
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            '..', 'datos', 'resultados_goy.csv')
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=resultados[0].keys())
        w.writeheader()
        w.writerows(resultados)
    
    print("=" * 70)
    print("SOBREVIVE EL PCC A LA NO LINEALIDAD?")
    print("=" * 70)
    for r in resultados:
        tag = "PCC VALIDO" if r['ratio_media'] > 1 else "PCC FALLA"
        print(f"  nu={r['nu']:.4f}  ratio={r['ratio_media']:.2f}  [{tag}]")
    print(f"\nCSV guardado: {csv_path}")


if __name__ == '__main__':
    main()
