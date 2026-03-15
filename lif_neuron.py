import numpy as np
import matplotlib.pyplot as plt

def simulate_lif_neuron():
    # 1. Parâmetros do neurônio (Baseados no modelo biofísico)
    tau_m = 20e-3      # Constante de tempo da membrana (20ms)
    EL = -60e-3       # Potencial de repouso/leak (-60mV)
    R = 100e6          # Resistência da membrana (100 MOhm)
    Vth = -50e-3      # Limiar de disparo (-50mV)
    Vreset = -70e-3   # Potencial de reset após o disparo (-70mV)

    # 2. Parâmetros da simulação
    t_max = 0.2        # Simular 200ms
    dt = 0.0001        # Passo de tempo de 0.1ms
    t_range = np.arange(0, t_max, dt)
    steps = len(t_range)

    # 3. Entrada: Corrente sináptica com ruído (Processo estocástico)
    # A corrente média é suficiente para atingir o limiar
    np.random.seed(42)
    I_mean = 2.5e-10   
    I = I_mean * (1 + 0.8 * np.random.randn(steps)) 

    # 4. Inicialização do potencial de membrana
    v = np.zeros(steps)
    v = E_L
    spike_times =

    # 5. Integração numérica (Método de Euler)
    # Equação: dv/dt = (E_L - v + R \cdot I) / \tau_m
    for t in range(1, steps):
        dv = (E_L - v[t-1] + R * I[t]) * (dt / tau_m)
        v[t] = v[t-1] + dv

        # Mecanismo de Disparo
        if v[t] >= V_th:
            v[t] = V_reset      # Reseta o potencial
            spike_times.append(t_range[t])

    # 6. Visualização dos resultados
    plt.figure(figsize=(12, 6))
    plt.plot(t_range * 1000, v * 1000, label='Potencial de Membrana ($V_m$)')
    plt.axhline(V_th * 1000, color='r', linestyle='--', label='Limiar de Disparo')
    plt.title('Simulação de Neurônio Leaky Integrate-and-Fire (LIF)')
    plt.xlabel('Tempo (ms)')
    plt.ylabel('Potencial de Membrana (mV)')
    plt.legend(loc='upper right')
    plt.grid(alpha=0.3)
    plt.show()

if __name__ == "__main__":
    simulate_lif_neuron()
