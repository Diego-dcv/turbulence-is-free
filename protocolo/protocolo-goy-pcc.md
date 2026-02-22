# PROTOCOLO: Test del PCC en modelo no lineal GOY
# ================================================
# Distribuir a cada IA por separado. No compartir resultados entre ellas.

## Contexto

En un test anterior, se verificó que en un modelo de difusión lineal en red,
el coste de mantener la energía concentrada es >> 1 comparado con dejar que el
sistema se redistribuya libremente. Ese resultado fue criticado porque el modelo
era lineal y no podía generar blow-up.

Este segundo test introduce **no linealidad** mediante un Shell Model GOY
(Gledzer-Ohkitani-Yamada), que es el modelo mínimo de cascada de energía
turbulenta. Incluye un término cuadrático que transfiere energía entre escalas
(como la advección en Navier-Stokes) más un término de disipación viscosa.

## Modelo GOY

Hay N shells, cada una con un número de onda k_n = k_0 × λ^n y una velocidad
compleja u_n. La ecuación de evolución es:

    du_n/dt = i × [a × k_n × u_{n+1} × conj(u_{n+2})
                 + b × k_{n-1} × u_{n-1} × conj(u_{n+1})
                 + c × k_{n-2} × u_{n-2} × conj(u_{n-1})]
              - ν × k_n² × u_n
              + f_n

Con a = 1, b = -0.5, c = -0.5 (conserva energía en el término no lineal).

## Parámetros

- N_shells = 15
- k_0 = 1, λ = 2  (por tanto k_n va de 1 a 16384)
- dt: adaptar según ν para estabilidad numérica
  (sugerencia: dt ≤ 1e-5 para ν ≥ 0.02, dt ≤ 1e-6 para ν < 0.01)
- Pasos transiente: 30000–50000 (hasta que el espectro se estabilice)
- Pasos de medida: 30000–50000
- Realizaciones: al menos 3 semillas aleatorias
- Forzamiento: f_0 = 5.0 (solo en la shell grande), resto = 0

IMPORTANTE: usar un integrador que maneje la rigidez del término -ν k² u.
Se recomienda IF-RK2 (Integrating Factor Runge-Kutta) o ETDRK2, donde
la disipación se trata exactamente vía exp(-ν k² dt) y la no linealidad
se integra explícitamente.

## Protocolo PCC

### Modo B — Cascada libre (turbulencia normal)
1. Inicializar u con ruido aleatorio pequeño (amplitud ~1e-3).
2. Forzar solo en shell 0 (f_0 = 5.0).
3. Dejar evolucionar libremente (transiente + medida).
4. Medir: disipación acumulada durante la fase de medida.
   disipacion = Σ_t [ν × Σ_n (k_n² × |u_n|²)] × dt

### Modo A — Concentración forzada en escalas finas
1. Misma inicialización y forzamiento base que Modo B.
2. Mismo transiente (con forzamiento normal).
3. Durante la fase de medida: en cada paso, si la fracción de energía
   en las últimas 3 shells (shells N-3 a N-1) es < 80% de la energía total,
   inyectar energía en esas shells para restaurar la fracción.
4. Medir: energía total inyectada en las shells finas durante la medida.
   trabajo = Σ_t [energía inyectada por paso]

### Ratio
ratio = trabajo_modo_A / disipacion_modo_B

## Barrido de ν
Ejecutar para: ν = 0.005, 0.01, 0.02, 0.05, 0.1, 0.2
Ajustar dt según necesidad numérica.

## Qué reportar
Para cada ν:
- coste_A (media ± std sobre realizaciones)
- coste_B (media ± std)
- ratio (media ± std)
- dt utilizado
- número de realizaciones
- cualquier inestabilidad numérica observada

## Preguntas adicionales
1. ¿El ratio es >> 1 para todo ν? ¿Crece o decrece con ν?
2. ¿El espectro de energía sigue la ley de Kolmogorov (E_n ~ k_n^{-2/3})
   en Modo B?
3. ¿Hay alguna condición bajo la cual el ratio cae a ≤ 1?
4. ¿Qué pasa si cambias las shells objetivo (ej. shells intermedias
   en vez de las más finas)?
5. Interpretación: ¿qué implica este resultado para la conjetura de
   regularidad de Navier-Stokes?
