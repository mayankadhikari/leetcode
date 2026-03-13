import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def isPossible(t):
            total_h = 0
            for w in workerTimes:
                # Solve w * x * (x + 1) / 2 <= t
                val = (2 * t) // w
                total_h += int((-1 + math.sqrt(1 + 4 * val)) // 2)
                if total_h >= mountainHeight:
                    return True
            return total_h >= mountainHeight

        low, high = 1, 10**16
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if isPossible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans