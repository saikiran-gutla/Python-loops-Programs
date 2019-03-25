n = int(input('Enter a number : '))
sum = 0
for i in range(n):
    if i%2==0:
        print(i,end=',')
        sum = sum+i
print('sum is ',sum)