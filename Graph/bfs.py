from collections import deque
main_graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "E"],
    "C": ["A", "E", "F"],
    "D": ["A"],
    "E": ["B", "C", "F"],
    "F": ["C", "E"]
}

def bfs_shortest_path(graph, start, target):
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        node, distance = queue.popleft()
        if node == target:
            return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    return -1

level = bfs_shortest_path(main_graph, "A", "F")
print(level)

