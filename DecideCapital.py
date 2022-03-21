# def checkSmallWord(word):
#     for charac in word:
#         if charac.isupper() == True:
#             return False
#     return True
# def checkLargeWord(word):
#     for charac in word:
#         if charac.islower() == True:
#             return False
#     return True
# def decideCapital(word):
#     if word[0].islower():
#         return checkSmallWord(word)
#     if word[0].isupper() and word[1].isupper():
#         return checkLargeWord(word)
#     return checkSmallWord(word[1:])
        
# print(decideCapital("Flag"))
import re
re.fullmatch(r"[A-Z]*|.[a-z]*", "Falg")