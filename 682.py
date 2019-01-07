class Solution:
    def calPoints(self,ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        result = 0
        for i in range(len(ops)):
            if ops[i] == "+":
                stack.append(stack[-1]+stack[len(stack)-2])
            elif ops[i] == "D":
                stack.append(stack[-1]*2)
            elif ops[i] == "C":
                stack.pop()
            else:
                stack.append(int(ops[i]))
        for j in range(len(stack)):
            result += stack[j]
        return result