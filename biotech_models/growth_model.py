import numpy as np
import matplotlib.pyplot as plt

def simulate_growth():
    # 1. Parâmetros do Modelo (Exemplo: Cultura de Leveduras)
    P0 = 10         # População inicial (ex: milhões de células/mL)
    K = 1000        # Capacidade de carga (limite do meio de cultura)
    r = 0.35        # Taxa intrínseca de crescimento
    
    # 2. Configuração do Tempo
    t_max = 48      # Simular 48 horas
    t = np.linspace(0, t_max, 500)
    
    # 3. Equação de Crescimento Logístico
    # P(t) = (K * P0 * exp(r*t)) / (K + P0 * (exp(r*t) - 1))
    population = (K * P0 * np.exp(r * t)) / (K + P0 * (np.exp(r * t) - 1))
    
    # 4. Adicionando Ruído Experimental Realístico
    noise = np.random.normal(0, 15, size=population.shape)
    measured_data = population + noise

    # 5. Visualização
    plt.figure(figsize=(10, 6))
    plt.plot(t, population, 'r-', linewidth=2.5, label='Modelo Teórico (Logístico)')
    plt.scatter(t[::15], measured_data[::15], color='black', alpha=0.6, label='Dados Experimentais Simulados')
    
    plt.title('Simulação de Crescimento Celular em Biorreator')
    plt.xlabel('Tempo (Horas)')
    plt.ylabel('Densidade Populacional (Células/mL)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    simulate_growth()
