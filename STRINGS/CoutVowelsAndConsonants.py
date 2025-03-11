string = "Hello"

stringToLower = string.lower()
countVowels = 0
countConsonants = 0

for i in string:
    if i.isalpha():
        if i == 'a' or i == 'e' or i=='i' or i == 'o' or i=='u':
            countVowels += 1
        else:
            countConsonants +=1
        
print(countConsonants)
print(countVowels)