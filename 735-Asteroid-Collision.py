class Solution:
    def asteroidCollision(self,asteroids):
        arr = []
        for asteroid in asteroids:
            if not arr or asteroid > 0:
                arr.append(asteroid)
            else:
                while arr and arr[-1] > 0:
                    if arr[-1] + asteroid < 0:
                        arr.pop()
                    elif arr[-1] + asteroid == 0:
                        arr.pop()
                        break
                    else:
                        break
                else:
                    arr.append(asteroid)
    
        return arr
