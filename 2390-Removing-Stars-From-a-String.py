class Solution:
    def removeStars(self, s: str) -> str:
        arr = []
        for i in s:
            if i !="*":
                arr.append(i)
            else:
                arr.pop()
        return "".join(arr)            

        
