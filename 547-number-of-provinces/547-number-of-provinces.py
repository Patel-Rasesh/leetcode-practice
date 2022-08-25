# # class Solution(object):
# #     def findCircleNum(self, isConnected):
# #         """
# #         :type isConnected: List[List[int]]
# #         :rtype: int
# #         """
#         # Approach A - this DFS is working
# #         # 1. Iterate through nodes
# #         nodeIterator = 0
# #         visited = [0] * len(isConnected)
# #         provinces = 0
        
# #         def traverse(nodeIterator, isConnected, visited):
# #             node = isConnected[nodeIterator]
# #             for edge in range(len(node)):
# #                 if isConnected[nodeIterator][edge] == 1 and visited[edge] == 0:
# #                     visited[edge] = 1
# #                     traverse(edge, isConnected, visited)

# #         for nodeIterator in range(len(isConnected)):
# #             for edgeIterator in range(len(isConnected[nodeIterator])):
# #                 if isConnected[nodeIterator][edgeIterator] == 1 and visited[nodeIterator] != 1:
# #                     provinces += 1
# #                     traverse(edgeIterator, isConnected, visited)
                    
# #         return provinces 

# # Approach B - this is taken from solutions to check its complexities
# # UnionFind class
# class UnionFind:
#     def __init__(self, size):
#         self.root = [i for i in range(size)]
#         # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
#         # The initial "rank" of each vertex is 1, because each of them is
#         # a standalone vertex with no connection to other vertices.
#         self.rank = [1] * size
#         self.count = size

#     # The find function here is the same as that in the disjoint set with path compression.
#     def find(self, x):
#         if x == self.root[x]:
#             return x
#         self.root[x] = self.find(self.root[x])
#         return self.root[x]

#     # The union function with union by rank
#     def union(self, x, y):
#         rootX = self.find(x)
#         rootY = self.find(y)
#         if rootX != rootY:
#             if self.rank[rootX] > self.rank[rootY]:
#                 self.root[rootY] = rootX
#             elif self.rank[rootX] < self.rank[rootY]:
#                 self.root[rootX] = rootY
#             else:
#                 self.root[rootY] = rootX
#                 self.rank[rootX] += 1
#             self.count -= 1

#     def getCount(self):
#         return self.count


# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         if not isConnected or len(isConnected) == 0:
#             return 0
#         n = len(isConnected)
#         uf = UnionFind(n)
#         for row in range(n):
#             for col in range(row + 1, n):
#                 if isConnected[row][col] == 1:
#                     uf.union(row, col)
#         return uf.getCount()

class Solution:
    def findCircleNum(self, isConnected):
    
        graph = {}
        for key, value in enumerate(isConnected):
            graph[key] = []
        for key, value in enumerate(isConnected):
            for index in range(len(value)):
                if value[index] == 1 and index != key:
                    graph[key].append(index)
        
        explored = set()
        queue = set()
        
        provinces = 0
        for node in range(len(graph)):
            if node not in explored:
                queue.add(node)        
                while queue:
                    currentNode = queue.pop()
                    explored.add(currentNode)
                    for child in graph[currentNode]:
                        if child not in explored and child not in queue:
                            queue.add(child)

                provinces += 1
        return provinces