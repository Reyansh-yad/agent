import numpy as np
import matplotlib.pyplot as plt


def boltzmann_probability(values, temperature):
    """
    Calculates Boltzmann probability distribution.
    
    Args:
        values: Array-like of node values
        temperature: Temperature parameter (must be > 0)
        
    Returns:
        Probability distribution over values
        
    Raises:
        ValueError: If temperature <= 0
    """
    values = np.array(values)
    
    # Handle empty input
    if values.size == 0:
        return values
    
    if temperature <= 0:
        raise ValueError("Temperature must be greater than 0")
    
    exponents = np.exp((values - np.max(values)) / temperature)
    
    probabilities = exponents / np.sum(exponents)
    return probabilities

def run_simulation(tracked_indices=None):
    """
    Runs a temperature-based simulation of node selection probability.
    
    Args:
        tracked_indices: List of node indices to track (default: [0, 1])
    """
    if tracked_indices is None:
        tracked_indices = [0, 1]
    
    node_values = [5.0, 10.0, 15.0, 20.0]
    initial_temp = 1.0
    final_temp = 0.1
    cooling_rate = 0.95
    
    # Validate cooling_rate
    if not (0.0 < cooling_rate < 1.0):
        raise ValueError(f"cooling_rate must be strictly between 0 and 1, got {cooling_rate}")
    
    temperatures = []
    prob_histories = {idx: [] for idx in tracked_indices}
    
    current_temp = initial_temp
    
    # Print header
    header = "Temp (T)"
    for idx in tracked_indices:
        header += f"\t P(Node {idx})"
    print(header)
    
    while current_temp > final_temp:
        probs = boltzmann_probability(node_values, current_temp)
        temperatures.append(current_temp)
        
        # Track selected node indices
        for idx in tracked_indices:
            prob_histories[idx].append(probs[idx])
        
        # Print row
        row_str = f"{current_temp:<10.4f}"
        for idx in tracked_indices:
            row_str += f"\t {probs[idx]:<15.6f}"
        print(row_str)
        
        current_temp *= cooling_rate
    
    # Plot results
    plt.figure(figsize=(10, 6))
    colors = ['red', 'green', 'blue', 'orange']
    linestyles = ['--', '-', '-.', ':']
    
    for idx, tracked_idx in enumerate(tracked_indices):
        plt.plot(
            temperatures, 
            prob_histories[tracked_idx], 
            label=f'Prob. of Node {tracked_idx}',
            color=colors[idx % len(colors)],
            linestyle=linestyles[idx % len(linestyles)]
        )

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
    # Run simulation tracking nodes 0 and 1
    run_simulation(tracked_indices=[0, 1])
