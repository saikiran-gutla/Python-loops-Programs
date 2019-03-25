# PROGRAM TO PRINT NUMBERS FROM 1 TO N WHICH ARE MULTIPLES OF 3 AND 5
n = int(input("Enter a number : "))
for i in range(n):
    if i%3 == 0 and i%5 == 0:
        print('Multiples of 3 and 5 are :',i)