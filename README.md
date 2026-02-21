# AI Labs — Knowledge Representation, Intelligent Agents & Machine Learning

A structured collection of AI lab exercises covering Prolog logic programming, intelligent agent design, and core machine learning algorithms.

## Repository Structure

```
agent/
├── lab-1/   # Prolog — Knowledge Representation & Logic Programming
├── lab-2/   # Python — Intelligent Agents & Search Algorithms
├── lab-3/   # Python — Machine Learning Algorithms
└── requirements.txt
```

## Labs at a Glance

### [Lab 1 — Prolog](./lab-1/README.md)

Prolog programs that demonstrate knowledge representation and logical inference.

| File | Topic |
|------|-------|
| `fac.pl` | Recursive factorial |
| `fibo.pl` | Fibonacci sequence |
| `route.pl` | Graph route finding |
| `Friendship.pl` | Transitive friendship |
| `Jealousy.pl` | Gender-aware jealousy rule |
| `bort&sis.pl` | Brother/sister-in-law relationships |
| `nephew.pl` | Nephew and cousin relationships |
| `q7.pl` | Multiplication table generator |
| `lab1.pl` | Happiness and music facts |
| `lab1b.pl` | Simple jealousy rule |

**Concepts:** facts, rules, unification, recursion, negation-as-failure, list construction.

---

### [Lab 2 — Intelligent Agents](./lab-2/README.md)

Python implementations of intelligent agents and classical AI search algorithms with interactive GUI visualisations.

| File | Topic |
|------|-------|
| `vacuum.py` | Reactive vacuum cleaner agent with obstacle detection (tkinter GUI) |
| `Block_World.py` | STRIPS-like planning agent solving block stacking problems (tkinter GUI) |
| `8_puzzels.py` | A* search with Manhattan distance heuristic for the 8-puzzle |
| `Tic_Tac_Toe.py` | Heuristic evaluation function e(p) for game-playing agents |
| `temperature.py` | Boltzmann probability simulation with temperature annealing |

**Concepts:** reactive agents, BFS planning, A* search, heuristic evaluation, simulated annealing.

---

### [Lab 3 — Machine Learning](./lab-3/README.md)

From-scratch implementations of fundamental ML algorithms using NumPy, plus a scikit-learn SVM example.

| File | Topic |
|------|-------|
| `perceptron_logic.py` | Perceptron for AND and OR logic gates |
| `X_OR.py` | Two-layer neural network (backpropagation) for XOR |
| `KNN.py` | K-Nearest Neighbours classifier |
| `kmean.py` | K-Means clustering |
| `svm.py` | Linear SVM via scikit-learn |
| `Hopfield.py` | Hopfield network for bipolar pattern recovery |
| `Bi-dir.py` | Bidirectional Associative Memory (BAM) |
| `odd&even.py` | Perceptron classifier for odd/even detection |

**Concepts:** linear classification, backpropagation, instance-based learning, unsupervised clustering, maximum-margin classifiers, Hopfield networks, bidirectional associative memory.

---

## Getting Started

### Prerequisites

- [SWI-Prolog](https://www.swi-prolog.org/) for Lab 1
- Python 3.8+ for Labs 2 and 3
- `tkinter` (bundled with most Python distributions) for Lab 2 GUI programs

### Installation

```bash
git clone https://github.com/Reyansh-yad/agent.git
cd agent
python -m venv .venv
# Windows
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

### Quick Start

```bash
# Lab 1 — run Prolog factorial
swipl lab-1/fac.pl
# ?- fac(5, F).

# Lab 2 — launch vacuum cleaner agent GUI
python lab-2/vacuum.py

# Lab 3 — train KNN classifier
python lab-3/KNN.py
```

## Dependencies

- **NumPy** — array operations (Labs 2 & 3)
- **Matplotlib** — probability visualisation (Lab 2 `temperature.py`)
- **scikit-learn** — SVM and train/test split (Lab 3 `svm.py`)
- **tkinter** — GUI windows (Lab 2 `vacuum.py`, `Block_World.py`)

## License

MIT License — free to use for educational and research purposes.
