# ENTER A NUMBER TO PRINT N TO 1 NUMBERS
n = int(input('Enter number :'))
i=0
# while n>1:
#     n-=1
#     print(n,sep=',')
for i in range(n):
    n-=1
    print(n,sep='+')