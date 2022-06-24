class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        queue = set()
        queue.add(0)
        visited = set()
        while queue:
            currentRoom = queue.pop()
            visited.add(currentRoom)
            for eachRoom in rooms[currentRoom]:
                if eachRoom not in visited:
                    queue.add(eachRoom)
        if len(visited) == len(rooms):
            return True
        else:
            return False