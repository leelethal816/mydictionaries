sometext = open("sometext.txt", "r")

sometext = sometext.read().split()

i = 0
worddict = dict()

for each in sometext:
    sometext[i] = each.rstrip(",").rstrip(".").lower()
    if sometext[i] not in worddict:
        worddict[sometext[i]] = sometext.count(sometext[i])
    i += 1

for each in worddict:
    print(f"{each} has appeared {worddict[each]} time(s) in the text")
