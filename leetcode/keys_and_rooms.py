# https://leetcode.com/problems/keys-and-rooms
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        unused_keys = {0}

        while len(unused_keys) > 0:
            k = unused_keys.pop()
            visited.add(k)
            keys = rooms[k]
            unused_keys.update(set(keys).difference(visited))

        return len(visited) == len(rooms)
