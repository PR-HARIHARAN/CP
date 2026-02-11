# LC problem link : https://leetcode.com/problems/keys-and-rooms/description/
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        queue = deque([0])
        visited = set()

        while queue:
            room = queue.popleft()
            if room not in visited:
                visited.add(room)
                queue.extend(rooms[room])
        return len(visited) == len(rooms)
