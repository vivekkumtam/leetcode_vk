class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a,2)
        int_b = int(b,2)

        c = int_a + int_b

        bin_c = bin(c)[2:]

        return bin_c