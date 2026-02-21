# Lab 1 — Prolog Knowledge Representation & Logic Programming

A collection of Prolog programs demonstrating knowledge representation, logical inference, and recursive algorithms.

## Overview

This lab introduces Prolog as a tool for representing knowledge and performing logical reasoning. The programs cover:

- **Basic facts and rules** — simple knowledge bases with family/social relationships
- **Recursive algorithms** — factorial and Fibonacci using Prolog recursion
- **Graph search** — finding routes through a directed graph
- **Relationship modelling** — jealousy, friendship, family ties, and kinship

## Files

| File | Description |
|------|-------------|
| `lab1.pl` | Basic happiness/music facts and rules |
| `lab1b.pl` | Simple jealousy rule based on shared love interest |
| `fac.pl` | Recursive factorial computation |
| `fibo.pl` | Recursive Fibonacci sequence and printer |
| `route.pl` | Route finding over a directed edge graph |
| `Friendship.pl` | Transitive friendship/connectivity relationship |
| `Jealousy.pl` | Gender-aware jealousy rule |
| `bort&sis.pl` | Brother-in-law and sister-in-law relationships |
| `nephew.pl` | Nephew and cousin relationships via parent/sibling rules |
| `q7.pl` | Multiplication table generator using recursion |

## Program Details

### `lab1.pl` — Happiness & Music
Defines facts about who is happy and who listens to music, with a rule that derives music-listening from happiness and air-guitar-playing from listening to music.

```prolog
?- playsAirGuitar(yogita).
true.
```

### `lab1b.pl` — Simple Jealousy
A minimal jealousy rule: two people are jealous of each other if they both love the same person.

```prolog
?- jealous(vanu, madan).
true.
```

### `fac.pl` — Factorial
Computes the factorial of a non-negative integer using Prolog recursion.

```prolog
?- fac(5, F).
F = 120.
```

### `fibo.pl` — Fibonacci
Computes individual Fibonacci numbers and includes a `print_fib/1` predicate that prints all Fibonacci numbers from index 0 to N.

```prolog
?- fib(7, F).
F = 13.

?- print_fib(6).
0 1 1 2 3 5 8
```

### `route.pl` — Route Finding
Defines directed edges between nodes and recursively finds a path (route) between any two reachable nodes, returning the path as a list.

```prolog
?- route(a, d, Path).
Path = [a, b, c, d].
```

### `Friendship.pl` — Transitive Friendship
Checks whether two people are directly or transitively connected through a chain of friendships.

```prolog
?- connected(a, e).
true.
```

### `Jealousy.pl` — Gender-Aware Jealousy
Extends the jealousy concept by requiring that the jealous parties be of opposite genders.

```prolog
?- jealous(raj, amit).
true.
```

### `bort&sis.pl` — Brother/Sister-in-Law
Models sibling relationships through a shared parent and derives brother-in-law / sister-in-law relations using marriage facts.

```prolog
?- brother_in_law(amit, sita).
true.
```

### `nephew.pl` — Nephew & Cousin
Derives nephew and cousin relationships from parent and sibling rules.

```prolog
?- nephew(karan, amit).
true.

?- cousin(karan, priya).
true.
```

### `q7.pl` — Multiplication Table
Prints a complete multiplication table for a given number N (1 × N through 10 × N) using tail-recursive Prolog.

```prolog
?- table(7).
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

## Getting Started

### Prerequisites

- [SWI-Prolog](https://www.swi-prolog.org/) (recommended) or any ISO-compatible Prolog interpreter

### Running a Program

Start SWI-Prolog and load a file:

```bash
swipl fac.pl
```

Then query from the interactive prompt:

```prolog
?- fac(6, F).
F = 720.
```

To exit:

```prolog
?- halt.
```

## Key Prolog Concepts Demonstrated

| Concept | Example |
|---------|---------|
| Facts | `happy(yogita).` |
| Rules | `playsAirGuitar(X) :- listen2Music(X).` |
| Recursion | `fac/2`, `fib/2`, `route/3` |
| Unification | Pattern matching in all predicates |
| Negation-as-failure | `X \= Y` to ensure distinct entities |
| Arithmetic | `F is N * F1` in factorial |
| List construction | `[X|T]` in route finding |

## License

MIT License — free to use for educational and research purposes.
