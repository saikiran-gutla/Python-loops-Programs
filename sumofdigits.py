# PROGRAM TO TAKE A NUMBER AND FIND SUM OF DIGITS OF A GIVEN NUMBER
num = int(input('Enter a number :'))
sum = 0
while(num>0):
        rem = num%10
        sum = sum + rem
        num = num//10
print('sum is',sum)