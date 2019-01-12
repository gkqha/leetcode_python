class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        leng = len(nums)
        if len(nums) == 0 or nums == None:
            return res
        list = []
        list.append(nums[0])
        res.append(list)
        i = 1
        while i < leng:
            size = len(res)
            for j in range(size):
                size2 = len(res[0])
                for k in range(size2 + 1):
                    tmp = res[0].copy()
                    tmp.insert(k, nums[i])
                    res.append(tmp)
                del (res[0])
            i += 1
        return res
