emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com",
          "testemail+david@lee.tcode.com"]
filteredEmails = set()

for email in emails:
    name, domain = email.split('@')
    local = name.split('+')[0].replace('.', '')
    filteredEmails.add(local+'@'+domain)

print(filteredEmails)