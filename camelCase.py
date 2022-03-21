words = ['is', 'valid']
string = "isValid"
tempWord = ''
for word in words:
    for i, charac in enumerate(string):
        if tempWord == word:
            print(word)
            tempWord = ''
            break
        else:
            tempWord += charac

