# ACCEPT A STRING AND COUNT EACH VOWEL SEPARATELY
str = input('Enter a string: ')
s = str.lower()
acnt = ecnt = icnt = ocnt = ucnt = 0
for i in s:
    if i in 'a':
        acnt = acnt + 1
    elif i in 'e':
        ecnt += 1
    elif i in 'i':
        icnt += 1
    elif i in 'o':
        ocnt += 1
    elif i in 'u':
        ucnt += 1

if acnt>=1:
    print('a count is',acnt)
if ecnt>=1:
    print('e count is',ecnt)
if icnt>=1:
    print('i count is',icnt)
if ocnt>=1:
    print('o count is',ocnt)
if ucnt>=1:
    print('u count is',ucnt)




