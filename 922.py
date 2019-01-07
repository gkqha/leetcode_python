class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        o = 0
        e = 0
        result = [0]*len(A)
        for index in range(len(A)):
            if A[index] % 2 == 0:
                result[o*2] = A[index]
                o += 1
            else:
                result[e*2+1] = A[index]
                e += 1
        return result


s = Solution()
print(s.sortArrayByParityII([4, 2, 5, 7]))
