class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def to_base(num: int, base: int) -> str:
            if num == 0:
                return "0"
            digits = []
            while num:
                digits.append(str(num % base))
                num //= base
            return ''.join(reversed(digits))

        def generate_palindromes():
            # Generate palindromes in base 10: odd and even length
            length = 1
            while True:
                # Odd length
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[-2::-1])  # odd length
                # Even length
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[::-1])   # even length
                length += 1

        count = 0
        total = 0
        for num in generate_palindromes():
            if is_palindrome(to_base(num, k)):
                total += num
                count += 1
                if count == n:
                    break
        return total