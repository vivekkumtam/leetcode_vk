import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        else:
            return math.pow(x,n)