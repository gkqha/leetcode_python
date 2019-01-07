class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s = set()
        for e in emails:
            local, host = e.split("@")
            local = local.replace(".", "")
            index = local.find("+")
            if index != -1:
                local = local[:index]
            s.add(local + host)
        return len(s)
