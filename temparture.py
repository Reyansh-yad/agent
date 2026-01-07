import numpy as np
import matplotlib.pyplot as plt


def boltzmann_probability(values, temperature):
    values = np.array(values)
    
    if temperature <= 0:
        return np.zeros_like(values)
    
    exponents = np.exp((values - np.max(values)) / temperature)
    
    probabilities = exponents / np.sum(exponents)
    return probabilities

def run_simulation():
    node_values = [5.0, 10.0, 15.0, 20.0]
    initial_temp = 1.0
    final_temp = 0.1
    cooling_rate = 0.95
    
    temperatures = []
    inferior_probs = []
    superior_probs = []
    
    current_temp = initial_temp
    print(f"{'Temp (T)':<10} {'P(inferior)':<15} {'P(superior)':<15}")
    
    while current_temp > final_temp:
        probs = boltzmann_probability(node_values, current_temp)
        temperatures.append(current_temp)
        inferior_probs.append(probs[0])
        superior_probs.append(probs[1])   
        
        print(f"{current_temp:<10.4f} {probs[0]:<15.6f} {probs[1]:<15.6f}")
        current_temp *= cooling_rate
    
    plt.figure(figsize=(10, 6))
    plt.plot(temperatures, inferior_probs, label='Prob. of Inferior Node', color='red', linestyle='--')
    plt.plot(temperatures, superior_probs, label='Prob. of Superior Node', color='green')

    plt.title('Effect of Temperature on Node Selection Probability')
    plt.xlabel('Temperature (T)')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid()

    plt.gca().invert_xaxis()
    plt.text(initial_temp, 0.5, 'High Temp', fontsize=12, color='blue')
    plt.text(final_temp + 0.1, 0.9, "High selectivity", fontsize=12, color='blue')

    plt.show()

if __name__ == "__main__":
    run_simulation()



