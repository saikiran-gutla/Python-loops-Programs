
# ACCEPT A STRING AND REMOVE VOWELS FROM A STRING

string = input('Enter a String: ')
temp = ''
for i in string:
    if i not in 'aeiou':
        temp = temp+i
print(temp,"is a string without vowels")
