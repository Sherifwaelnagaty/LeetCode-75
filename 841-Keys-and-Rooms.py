class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keyList = [0]  # Since room 0 is always unlocked, we assume that we have the key to it.
        keySet = {0}

        solved = False
        while len(keyList) != 0 and not solved:
            keys = rooms[keyList.pop()]
            for key in keys:
                if not (key in keySet):
                    keyList.append(key)
                    keySet.add(key)
            if len(keySet) == len(rooms):
                solved = True
        
        return solved
        