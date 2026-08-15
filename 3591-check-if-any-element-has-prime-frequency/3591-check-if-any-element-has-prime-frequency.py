class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(n):
            if n < 2: return False
            if n == 2 or n == 3: return True
            if n % 2 == 0 or n % 3 == 0: return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i+2) == 0:
                    return False
                i += 6
            return True
        mp = Counter(nums)
        for v in mp.values():
            if is_prime(v): return True
        return False