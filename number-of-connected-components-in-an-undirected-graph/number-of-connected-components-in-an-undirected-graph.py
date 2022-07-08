from collections import defaultdict
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # 1. Making a graph out of edges
        graph = defaultdict(int)
        for i in range(n):
            graph[i] = []
        for (node1, node2) in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        # 2. BFS traversal - increment islands, each time queue gets empty
        queue = set()
        visited = set()
        
        islands = 0
        
        while len(visited) != n:
            for node in range(n):
                if node not in visited:
                    queue.add(node)
                    visited.add(node)
                    break
            while queue:
                currentNode = queue.pop()
                for neighbor in graph[currentNode]:
                    if neighbor in visited:
                        continue
                    queue.add(neighbor)
                    visited.add(neighbor)
            islands += 1
                
        return islands
                        