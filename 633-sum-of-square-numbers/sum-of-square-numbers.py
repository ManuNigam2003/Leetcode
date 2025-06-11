class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(floor(math.sqrt(c))+1):
            b = sqrt(c - a*a)
            if b.is_integer():
                return True
        return False
        