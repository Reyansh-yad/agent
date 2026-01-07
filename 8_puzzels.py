import heapq

class Node:
    def __init__(self, state, parent=None, move=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.move = move  # The move that got us here (e.g., "UP")
        self.g = g  # Cost from start
        self.h = h  # Heuristic cost to goal
        self.f = g + h  # Total estimated cost

    # Define comparison for the priority queue (based on f-score)
    def __lt__(self, other):
        return self.f < other.f

class PuzzleSolver:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.grid_size = 3

    def get_manhattan_distance(self, state):
        """
        Calculates the Manhattan distance heuristic.
        Sum of abs(x_val - x_goal) + abs(y_val - y_goal) for all tiles.
        """
        distance = 0
        for i, tile in enumerate(state):
            if tile == 0: continue  # Don't calculate distance for the empty space
            
            # Current (row, col)
            current_row, current_col = i // self.grid_size, i % self.grid_size
            
            # Goal (row, col) - We find where 'tile' should be in the goal state
            goal_index = self.goal_state.index(tile)
            goal_row, goal_col = goal_index // self.grid_size, goal_index % self.grid_size
            
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

    def get_neighbors(self, node):
        """
        Generates valid child states by moving the blank space (0).
        """
        neighbors = []
        state = list(node.state)
        zero_index = state.index(0)
        
        # Current coordinates of the blank space
        row, col = zero_index // self.grid_size, zero_index % self.grid_size

        # Possible moves: Up, Down, Left, Right
        # (row_change, col_change, move_name)
        moves = [(-1, 0, "UP"), (1, 0, "DOWN"), (0, -1, "LEFT"), (0, 1, "RIGHT")]

        for dr, dc, move_name in moves:
            new_row, new_col = row + dr, col + dc

            # Check boundaries
            if 0 <= new_row < self.grid_size and 0 <= new_col < self.grid_size:
                # Calculate new index for the blank space
                new_index = new_row * self.grid_size + new_col
                
                # Create a new state by swapping
                new_state = state[:]
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                
                neighbors.append((tuple(new_state), move_name))

        return neighbors

    def solve(self):
        """
        Executes the A* Algorithm.
        """
        # Priority Queue stores Nodes: ordered by f-score
        open_list = []
        
        # Closed Set stores visited states to avoid cycles
        closed_set = set()

        # Create start node
        start_h = self.get_manhattan_distance(self.start_state)
        start_node = Node(self.start_state, None, None, 0, start_h)
        
        heapq.heappush(open_list, start_node)

        while open_list:
            # Pop the node with the lowest f value
            current_node = heapq.heappop(open_list)

            # Check if goal reached
            if current_node.state == self.goal_state:
                return self.reconstruct_path(current_node)

            # Add to visited
            closed_set.add(current_node.state)

            # Generate neighbors
            for neighbor_state, move in self.get_neighbors(current_node):
                if neighbor_state in closed_set:
                    continue

                # Calculate scores
                g_score = current_node.g + 1
                h_score = self.get_manhattan_distance(neighbor_state)
                neighbor_node = Node(neighbor_state, current_node, move, g_score, h_score)

                # Add to priority queue
                heapq.heappush(open_list, neighbor_node)

        return None  # No solution found

    def reconstruct_path(self, node):
        """
        Backtracks from the goal node to the start node to determine moves.
        """
        path = []
        while node.parent:
            path.append(node.move)
            node = node.parent
        return path[::-1] # Return reversed path (Start -> Goal)

    def print_state(self, state):
        """
        Helper to print the board in a 3x3 grid.
        """
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

# --- Main Execution ---
if __name__ == "__main__":
    # 0 represents the empty space
    # Goal: 1 2 3
    #       4 5 6
    #       7 8 0
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    # Initial State (A solvable configuration)
    # 1 2 3
    # 4 0 5
    # 7 8 6
    start = (1, 2, 3, 4, 0, 5, 7, 8, 6)

    print("Solving...")
    solver = PuzzleSolver(start, goal)
    solution_moves = solver.solve()

    if solution_moves:
        print(f"Solution found in {len(solution_moves)} moves:")
        print(" -> ".join(solution_moves))
        
        # Optional: visualize the steps
        print("\nVisualizing Path:")
        curr = list(start)
        solver.print_state(curr)
        
        for move in solution_moves:
            print(f"Move: {move}")
            zero_idx = curr.index(0)
            
            if move == "UP": swap_idx = zero_idx - 3
            elif move == "DOWN": swap_idx = zero_idx + 3
            elif move == "LEFT": swap_idx = zero_idx - 1
            elif move == "RIGHT": swap_idx = zero_idx + 1
            
            curr[zero_idx], curr[swap_idx] = curr[swap_idx], curr[zero_idx]
            solver.print_state(curr)
    else:
        print("No solution found (or state is unsolvable).")