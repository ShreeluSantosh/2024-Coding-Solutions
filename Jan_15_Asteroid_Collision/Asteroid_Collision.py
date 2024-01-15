class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for x in asteroids:
            surv = True
            if x > 0:
                s.append(x)
            else:
                while(len(s) > 0):
                    y = s[-1]
                    if y < 0:
                        break
                    elif x+y == 0:
                        s.pop()
                        surv = False
                        break
                    elif x+y < 0:
                        s.pop()
                    else:
                        surv = False
                        break
                if surv:
                    s.append(x)
        return s