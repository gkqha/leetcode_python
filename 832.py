class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        first = []
        for i in range(len(A)):
            tmp_list = []
            for _ in range(len(A[i])):
                tmp_int=A[i].pop()
                if tmp_int==1:
                    tmp_list.append(0)
                else:
                    tmp_list.append(1)
            first.append(tmp_list)
        return first

s = Solution()
print(s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))

