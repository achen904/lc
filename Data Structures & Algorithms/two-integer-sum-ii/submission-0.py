class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for l in range(len(numbers) - 1):
            r = len(numbers) - 1
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            else:
                while l < r and numbers[l] + numbers[r] > target:
                    r -= 1
                    if numbers[l] + numbers[r] == target:
                        return [l + 1 , r + 1]
                
