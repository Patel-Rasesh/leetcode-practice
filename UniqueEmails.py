class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        outputEmails = []
        for email in emails:
            localName = email.split('@')[0]
            domainName = email.split('@')[1]
            # Processing on localName
            localName = localName.split('+')[0]
            localName = localName.replace('.', '')
            outputEmails.append(localName+'@'+domainName)
        return outputEmails

obj = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(obj.numUniqueEmails(emails))