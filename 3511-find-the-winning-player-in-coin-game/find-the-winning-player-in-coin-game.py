import math
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        if min(x, y//4) % 2 == 1:
            return "Alice"

        return "Bob"