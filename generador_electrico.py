
# -*- coding: utf-8 -*-
# Simulación de generador eléctrico sencillo (CA -> puente -> C -> carga)
# Parámetros editables al inicio.

import numpy as np
import matplotlib.pyplot as plt #instale pip install matplotlib si le falla

# Parámetros
N_turns = 600
coil_area = 0.0008
B_peak = 0.7
rpm = 900
pole_pairs = 1
R_load = 120.0
C_filter = 0.0022
diode_drop = 0.9

f_elec = (rpm / 60.0) * pole_pairs
T = 0.25
fs = 20000
t = np.arange(0, T, 1/fs)
w = 2 * np.pi * f_elec
E_max = N_turns * coil_area * B_peak * w
v_ac = E_max * np.sin(w * t)

v_rect = np.abs(v_ac) - 2*diode_drop
v_rect[v_rect < 0] = 0.0

v_cap = np.zeros_like(t)
for i in range(1, len(t)):
    dt = t[i] - t[i-1]
    if v_rect[i] > v_cap[i-1]:
        v_cap[i] = v_rect[i]
    else:
        v_cap[i] = v_cap[i-1] * np.exp(-dt / (R_load * C_filter))

i_load = v_cap / R_load

# Gráficas
plt.figure(); plt.title("PROGRAMA ECHO POR DIEGO A. SEPULVEDA H. FUAA Universidad""\n"" Voltaje inducido (CA)"); plt.plot(t, v_ac); plt.xlabel("Tiempo [s]"); plt.ylabel("Voltaje [V]"); plt.grid(True); plt.tight_layout()
plt.figure(); plt.title("PROGRAMA ECHO POR DIEGO A. SEPULVEDA H. FUAA Universidad""\n"" Voltaje rectificado y filtrado"); plt.plot(t, v_rect, label="Rectificado"); plt.plot(t, v_cap, label="Filtrado"); plt.xlabel("Tiempo [s]"); plt.ylabel("Voltaje [V]"); plt.legend(); plt.grid(True); plt.tight_layout()
plt.figure(); plt.title("PROGRAMA ECHO POR DIEGO A. SEPULVEDA H. FUAA Universidad""\n"" Corriente en la carga"); plt.plot(t, i_load); plt.xlabel("Tiempo [s]"); plt.ylabel("Corriente [A]"); plt.grid(True); plt.tight_layout()
plt.show()
