# AI Lab - Intelligent Agents & Algorithms

A comprehensive collection of intelligent agent implementations and AI algorithms for various problem domains.

## Overview

This repository contains implementations of intelligent agents and classical AI algorithms designed to solve diverse problems:

- **8-Puzzle Solver** (`8_puzzels.py`): Implements A* algorithm with Manhattan distance heuristic to solve the classic 8-puzzle problem
- **Tic-Tac-Toe Heuristic Evaluator** (`Tic_Tac_Toe.py`): Calculates game evaluation functions based on open winning lines for game-playing agents
- **Boltzmann Temperature Simulator** (`temperature.py`): Simulates probability distributions under varying temperature conditions using Boltzmann distributions
- **Block World Agent** (`Block_World.py`): Uses STRIPS-like planning with breadth-first search to solve block stacking problems
- **Vacuum Agent** (`vacuum.py`): A reactive and planning-based vacuum cleaner agent with intelligent navigation

## Features

### 8-Puzzle Solver
- A* search algorithm with optimal pathfinding
- Manhattan distance heuristic for efficient node evaluation
- Path reconstruction showing sequence of moves (UP, DOWN, LEFT, RIGHT)
- Solvability checking and visualization of solving steps
- Node prioritization using f-score (g + h)

### Tic-Tac-Toe Heuristic Evaluator
- Calculates e(p) = (open lines for player) - (open lines for opponent)
- Identifies all 8 possible winning lines (rows, columns, diagonals)
- Optional verbose diagnostic output via `verbose` parameter
- Pure function design with configurable diagnostic output
- Evaluates board positions for minimax game-playing algorithms

### Boltzmann Temperature Simulator
- Calculates probability distributions based on temperature parameter
- Validates input parameters (empty arrays, temperature bounds, cooling rate)
- Configurable node tracking with `tracked_indices` parameter
- Simulates annealing process with temperature cooling schedules
- Visualizes probability changes across temperature ranges
- Prevents infinite loops with cooling rate validation (0 < rate < 1)

### Block World Agent
- STRIPS-like planning algorithm with action preconditions and effects
- Breadth-first search for finding optimal action sequences
- Actions: pick_up, put_down, stack, unstack
- Visual state representation and goal tracking
- Interactive GUI with block visualization

### Vacuum Agent
- Reactive decision-making based on environment observations
- Advanced pathfinding and navigation
- Intelligent obstacle avoidance
- Multiple cleaning strategies
- Real-time performance metrics

## Files

- `8_puzzels.py` - A* algorithm implementation for 8-puzzle solving
- `Tic_Tac_Toe.py` - Heuristic evaluation for tic-tac-toe game states
- `temperature.py` - Boltzmann probability simulation with temperature annealing
- `Block_World.py` - Block world environment with STRIPS-like planning agent
- `vacuum.py` - Vacuum world environment with intelligent cleaning agent
- `README.md` - This documentation file

## Getting Started

### Prerequisites

- Python 3.10 or higher (tested on 3.13)
- tkinter (usually included with Python)
- Standard library modules: collections, copy, random, time

### Installation

```bash
git clone https://github.com/Reyansh-yad/agent.git
cd agent
```

### Setup

Create a virtual environment and install dependencies.

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running the Agents

**Perceptron Logic (AND/OR gates):**
```bash
python perceptron_logic.py
```
Trains a simple perceptron and prints predictions for AND and OR logic gates.

**8-Puzzle Solver:**
```bash
python 8_puzzels.py
```
Solves the 8-puzzle and displays the solution path with visualization.

**Tic-Tac-Toe Heuristic Evaluator:**
```bash
python Tic_Tac_Toe.py
```
Evaluates board positions and prints heuristic values. Use `verbose=True` for diagnostic output.

**Boltzmann Temperature Simulator:**
```bash
python temperature.py
```
Runs temperature annealing simulation and displays probability distribution changes with interactive plots.

**Block World Agent:**
```bash
python Block_World.py
```

**Vacuum Agent:**
```bash
python vacuum.py
```

Block World and Vacuum agents launch interactive GUI windows showing agents in action with real-time visualization.

## Architecture Details

### 8-Puzzle Solver

**Algorithm:** A* Search
- Uses priority queue (heapq) ordered by f-score
- Maintains open list (frontier) and closed set (visited states)
- Calculates g-score: cost from start node
- Calculates h-score: Manhattan distance heuristic
- f-score: g + h (total estimated cost)

**Key Methods:**
- `get_manhattan_distance(state)` - Calculates heuristic distance to goal
- `get_neighbors(node)` - Generates valid moves (UP, DOWN, LEFT, RIGHT)
- `solve()` - Executes A* algorithm
- `reconstruct_path(node)` - Backtracks from goal to start

### Tic-Tac-Toe Heuristic Evaluator

**Components:**
- `calculate_heuristic(board, player, verbose=False)` - Evaluates board positions
- Identifies all 8 winning lines (3 rows, 3 cols, 2 diagonals)
- Pure function with optional diagnostic output

**Heuristic Calculation:**
- Counts open lines (lines without opponent pieces) for player
- Counts open lines (lines without player pieces) for opponent
- Returns: player_open_lines - opponent_open_lines

### Boltzmann Temperature Simulator

**Algorithm:** Simulated Annealing
- Calculates Boltzmann probabilities: P(i) ∝ exp(value[i] / T)
- Applies temperature cooling schedule
- Tracks probability evolution across temperature range

**Key Methods:**
- `boltzmann_probability(values, temperature)` - Calculates probability distribution
  - Validates empty input
  - Checks temperature > 0
  - Normalizes probabilities
- `run_simulation(tracked_indices=None)` - Runs full simulation
  - Validates cooling_rate (0 < rate < 1)
  - Tracks selected node indices
  - Visualizes results with matplotlib

**Parameters:**
- `tracked_indices` - List of nodes to monitor (default: [0, 1])
- `cooling_rate` - Temperature decay per iteration (0 < rate < 1)
- `initial_temp` - Starting temperature
- `final_temp` - Stopping threshold

### Block World Agent

**Components:**
1. `BlockWorld` - Represents the environment state (block positions, clear surfaces, holding status)
2. `BlockWorldAgent` - Planning agent that solves block stacking problems
3. `BlockWorldGUI` - Visualization interface

**Planning Algorithm:**
- Uses STRIPS-style action representation
- Implements breadth-first search (BFS) for optimal solution
- State space: All possible configurations of block positions
- Actions consider preconditions and effects:
  - `pick_up(block)` - Pick up a clear block from table
  - `put_down(block)` - Put down held block on table
  - `stack(block1, block2)` - Stack block1 on block2
  - `unstack(block, source)` - Remove block from source

**Key Methods:**
- `get_state()` - Returns current state as hashable tuple
- `get_possible_actions()` - Generates valid actions from current state
- `apply_action()` - Updates world state based on action
- `search_plan()` - Finds optimal action sequence to goal

### Vacuum Agent

**Components:**
1. `VacuumAgent` - The intelligent agent with navigation logic
2. `Room` - The environment with grid-based layout
3. `VacuumGUI` - Real-time visualization interface

**Cell Types:**
- CLEAN (0) - Already cleaned
- DIRTY (1) - Needs cleaning
- OBSTACLE (2) - Cannot pass through
- AGENT (3) - Agent position

**Agent Strategies:**
- Reactive approach: Immediate response to sensory input
- Pathfinding: Optimal route planning
- Obstacle detection: Collision avoidance

**Performance Tracking:**
- Total moves count
- Cells cleaned count
- Cleaning efficiency ratio
- Path optimization analysis

## Customization

### 8-Puzzle Configuration
You can modify:
- Initial puzzle state configuration
- Goal state definition
- Heuristic function (currently Manhattan distance)
- Search algorithm parameters

### Tic-Tac-Toe Configuration
You can modify:
- Board state and piece positions
- Player symbols ('X' or 'O')
- Verbose output (enable/disable diagnostics)
- Use in minimax with alpha-beta pruning

### Boltzmann Simulator Configuration
You can modify:
- Node values (energy levels)
- Temperature schedule (initial_temp, final_temp, cooling_rate)
- Tracked node indices
- Visualization appearance and colors

### Block World Configuration
You can modify:
- Number and labels of blocks
- Initial block positions
- Goal state configuration
- Planning algorithm parameters
- GUI visualization appearance

### Vacuum Configuration
You can modify:
- Room dimensions (grid size)
- Initial dirt distribution
- Obstacle placement and patterns
- Agent starting position
- Cleaning strategy selection
- Simulation speed

## Examples

### 8-Puzzle Example
```python
from 8_puzzels import PuzzleSolver

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
start = (1, 2, 3, 4, 0, 5, 7, 8, 6)

solver = PuzzleSolver(start, goal)
solution = solver.solve()
print(f"Solution: {' -> '.join(solution)}")
```

### Tic-Tac-Toe Example
```python
from Tic_Tac_Toe import calculate_heuristic

board = [['X', '-', '-'],
         ['-', 'O', '-'],
         ['X', '-', '-']]

h_value = calculate_heuristic(board, 'X', verbose=True)
print(f"Heuristic: {h_value}")
```

### Boltzmann Simulator Example
```python
from temperature import run_simulation

# Track nodes 0, 1, and 2
run_simulation(tracked_indices=[0, 1, 2])
```

### Block World Example
The agent can solve problems like:
- "Stack block A on block B and block C on the table"
- "Create a tower with A on B on C"
- "Move all blocks from their current positions to achieve goal state"

### Vacuum Example
The agent can handle:
- Room layouts of any size
- Irregular obstacle patterns
- High-density dirt areas
- Efficient path optimization

## Algorithms & Concepts

**Key AI Concepts Implemented:**
1. **A* Search** - Optimal pathfinding with heuristics (8-Puzzle)
2. **Heuristic Evaluation** - Game state assessment (Tic-Tac-Toe)
3. **Probability Distributions** - Boltzmann statistics and temperature-based selection
4. **Simulated Annealing** - Temperature-based optimization (Temperature Simulator)
5. **State Space Search** - Explores possible world states (Block World)
6. **Planning** - STRIPS-like representation and solving (Block World)
7. **Reactive Control** - Immediate environmental responses (Vacuum)
8. **Constraint Handling** - Enforces action preconditions (Block World)

**Search Strategies:**
- Breadth-First Search (Block World planning)
- A* Search with Manhattan distance heuristic (8-Puzzle)
- Reactive Decision Making (Vacuum)
- Temperature-guided sampling (Boltzmann)
- Path optimization algorithms

## Code Quality Features

- **Input Validation**: Empty array checks, parameter bounds validation
- **Pure Functions**: Optional diagnostic output without side effects
- **Module Guard**: Test code wrapped in `if __name__ == "__main__":` blocks
- **Configurable Parameters**: Tracked indices, cooling rates, heuristic selection
- **Error Handling**: Clear error messages for invalid inputs
- **Documentation**: Comprehensive docstrings and inline comments

## Performance Considerations

- **8-Puzzle**: Solution time depends on puzzle complexity; Manhattan distance provides excellent heuristic
- **Tic-Tac-Toe**: O(8) line evaluation (constant time); suitable for minimax implementation
- **Temperature Simulator**: O(iterations × n_nodes) for probability calculations
- **Block World**: Solution time depends on problem complexity; BFS guarantees optimality
- **Vacuum**: Cleaning time optimized through path planning
- **GUI**: Real-time updates with configurable speed
- **Memory**: Efficient state representation using tuples and dictionaries

## Dependencies

- Python 3.7+
- NumPy (for temperature simulator)
- Matplotlib (for visualization)
- tkinter (for Block World and Vacuum GUIs, usually included with Python)
- Standard library: heapq, collections, copy, random, time

## Future Enhancements

- **Advanced Algorithms**: IDA*, bidirectional search, memory-bounded variants
- **Machine Learning**: Learned heuristics, neural network evaluators
- **Multi-Agent Systems**: Cooperative and adversarial agent interactions
- **Complex Environments**: Larger puzzles, dynamic obstacles, uncertainty
- **Optimization**: Genetic algorithms, particle swarm optimization
- **Game Theory**: Minimax with alpha-beta pruning, MCTS implementations
- **Reinforcement Learning**: Q-learning, policy gradient methods
- **Natural Language**: Goal specification from text descriptions
- **Visualization**: 3D rendering, real-time analytics dashboards

## Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Improve algorithms
- Enhance documentation
- Add new agent types

## License

MIT License - Feel free to use this code for educational and research purposes.