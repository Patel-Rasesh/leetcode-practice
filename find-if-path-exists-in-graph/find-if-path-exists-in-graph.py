class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = defaultdict(list)
        for key, value in edges:
            # Bidirectional
            graph[key].append(value)
            graph[value].append(key)
        
        visited = set()
        queue = set([source])
        
        while queue:
            currentNode = queue.pop()
            visited.add(currentNode)
            
            if currentNode == destination:
                return True
            
            for neighbors in graph[currentNode]:
                if neighbors not in visited:
                    queue.add(neighbors)
        return False