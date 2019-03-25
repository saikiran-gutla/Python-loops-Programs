# PROGRAM TO PRINT 1 TO N NUMBERS WITH ',' SEPARATOR AND THEIR SUM
n = int(input('Enter a number : '))
sum = 0
for i in range(n+1):
    print(i,sep=':',end=',')
    sum = sum+n
print('sum is :',sum)