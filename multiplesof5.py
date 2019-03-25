# PROGRAM TO PRINT MULTIPLES OF 5 FROM 1 TO N WITH COMMA SEPARATOR AND THEIR SUM
n = int(input('Enter a number :'))
sum = 0
for i in range(n):
    if i%5==0 and i!=0:
        print(i,end=',')
        sum = sum+i
print('Multiples of 5 sum is : ',sum)