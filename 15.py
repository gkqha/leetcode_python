class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closestNum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if abs(threeSum - target) < abs(closestNum - target):
                    closestNum = threeSum
                if threeSum > target:
                    r-=1
                elif threeSum < target:
                    l+=1
                else:
                    return target
        return closestNum
s = Solution()
print(s.threeSumClosest([-1,2,1,-4],1))