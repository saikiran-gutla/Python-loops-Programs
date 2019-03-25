str = input('Enter a string')
ch = input('Enter a character')
cnt = 0
for i in str:
    if i == ch:
        cnt+=1
print(f'{ch} repeated {cnt} times')