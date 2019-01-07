class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        stack = []
        i = 0
        while i < len(s) :
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                else:
                    tmp = stack[-1]
                    if not matches(tmp, s[i]):
                        return False
                    else:
                        stack.pop()
            i += 1
        if stack != []:
            return False
        else:
            return True


def matches(pop, s):
    popS = "([{"
    sS = ")]}"
    if popS.index(pop) == sS.index(s):
        return True
    else:
        return False


test = Solution()
print(test.isValid("]"))
