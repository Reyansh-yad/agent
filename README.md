# Agent

Implementation of intelligent agents for different environments.

## Overview

This repository contains comprehensive implementations of intelligent agents designed to interact with and solve tasks in various environments:

- **Block World Agent** (`block_world.py`): Uses STRIPS-like planning with breadth-first search to solve block stacking problems and achieve goal states
- **Vacuum Agent** (`vacuum.py`): A reactive and planning-based vacuum cleaner agent that intelligently cleans dirty locations and navigates obstacles

## Features

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

- `block_world.py` - Block world environment with STRIPS-like planning agent
- `vacuum.py` - Vacuum world environment with intelligent cleaning agent
- `README.md` - This documentation file

## Getting Started

### Prerequisites

- Python 3.7 or higher
- tkinter (usually included with Python)
- Standard library modules: collections, copy, random, time

### Installation

```bash
git clone https://github.com/Reyansh-yad/agent.git
cd agent
```

### Running the Agents

**Block World Agent:**
```bash
python block_world.py
```

**Vacuum Agent:**
```bash
python vacuum.py
```

Both will launch interactive GUI windows showing the agents in action with real-time visualization.

## Architecture Details

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
1. **State Space Search** - Explores possible world states
2. **Planning** - STRIPS-like representation and solving
3. **Heuristics** - Guides search for optimal solutions
4. **Constraint Handling** - Enforces action preconditions
5. **Reactive Control** - Immediate environmental responses

**Search Strategies:**
- Breadth-First Search (Block World)
- Reactive Decision Making (Vacuum)
- Path optimization algorithms

## Performance Considerations

- **Block World**: Solution time depends on problem complexity
- **Vacuum**: Cleaning time optimized through path planning
- **GUI**: Real-time updates with configurable speed
- **Memory**: Efficient state representation using tuples

## Future Enhancements

- Multi-agent coordination and cooperation
- Machine learning integration for strategy optimization
- More complex environments and scenarios
- Advanced pathfinding (A*, Dijkstra)
- Stochastic environment handling
- Hierarchical planning decomposition
- Natural language goal specification

## Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Improve algorithms
- Enhance documentation
- Add new agent types

## License

MIT License - Feel free to use this code for educational and research purposes.