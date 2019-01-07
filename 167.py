class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        stop = False
        while not stop:
            left = i+1
            right = len(numbers)-1
            while left <= right:
                middle = (left+right)//2
                if numbers[i]+numbers[middle] == target:
                    stop=True
                    break
                elif numbers[i]+numbers[middle] > target:
                    right = middle-1
                elif numbers[i]+numbers[middle] < target:
                    left = middle+1
            i += 1

        return [i, middle+1]