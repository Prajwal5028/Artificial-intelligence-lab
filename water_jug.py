from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target_amount):
    # Queue for holding states in the format (jug1_amount, jug2_amount, path)
    queue = deque()
    visited = set()  # To track visited states to avoid repetition

    # Start with both jugs empty, with an empty path
    queue.append((0, 0, []))
    visited.add((0, 0))

    while queue:
        jug1, jug2, path = queue.popleft()

        # Record the current state in the path
        path = path + [(jug1, jug2)]

        # Check if we have reached the target amount in either jug
        if jug1 == target_amount or jug2 == target_amount:
            print("Solution found with the following steps:")
            for step in path:
                print(f"Jug1 = {step[0]}, Jug2 = {step[1]}")
            return f"Final state: Jug1 = {jug1}, Jug2 = {jug2}"

        # Possible actions
        possible_actions = [
            (jug1_capacity, jug2),          # Fill jug1
            (jug1, jug2_capacity),          # Fill jug2
            (0, jug2),                      # Empty jug1
            (jug1, 0),                      # Empty jug2
            (max(jug1 - (jug2_capacity - jug2), 0), min(jug2_capacity, jug1 + jug2)),  # Pour jug1 -> jug2
            (min(jug1_capacity, jug1 + jug2), max(jug2 - (jug1_capacity - jug1), 0)),  # Pour jug2 -> jug1
        ]

        for action in possible_actions:
            if action[:2] not in visited:  # Check only jug amounts, ignore path for visited check
                queue.append((*action, path))
                visited.add(action[:2])

    return "No solution found."

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2
print(water_jug_bfs(jug1_capacity, jug2_capacity, target_amount))
