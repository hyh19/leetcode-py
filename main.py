from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.kSum(3, nums, 0, len(nums) - 1, 0)

    # 返回升序子数组 nums[lo..hi] 中所有和为 target 且不重复的 k 元组
    def kSum(self, k: int, nums: List[int], lo: int, hi: int, target: int) -> List[List[int]]:
        if hi - lo + 1 < k:
            return []
        if k == 2:
            return self.twoSum(nums, lo, hi, target)
        res = []
        i = lo
        while i <= hi:
            curNum = nums[i]
            sp = self.kSum(k - 1, nums, i + 1, hi, target - curNum)
            for x in sp:
                x.append(curNum)
                res.append(x)
            while i <= hi and nums[i] == curNum:
                i += 1
        return res

    # 返回升序子数组 nums[lo..hi] 中所有和为 target 且不重复的 2 元组
    def twoSum(self, nums: List[int], lo: int, hi: int, target: int) -> List[List[int]]:
        res = []
        while lo < hi:
            first, second = nums[lo], nums[hi]
            sum = first + second
            if sum < target:
                while lo < hi and nums[lo] == first:
                    lo += 1
            elif sum > target:
                while lo < hi and nums[hi] == second:
                    hi -= 1
            else:
                res.append([first, second])
                while lo < hi and nums[lo] == first:
                    lo += 1
                while lo < hi and nums[hi] == second:
                    hi -= 1
        return res
