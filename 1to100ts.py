# PROGRAM TO PRINT 1 TO 100 AND IF NUM IS MULTIPLE OF 3 PRINT 'TECHNO'
# IF NUM MULTIPLE OF 5 PRINT 'SOFT'
# IF NUM MULTIPLE OF 3 AND 5 PRINT 'TECHNO SOFT'
for i in range(1,100):
    if i%3 ==0:
        print(i,'is divisible 3, "Tecno"')
    if i%5 == 0:
        print(i,'Divisible by 5,"Soft"')
    if i%3==0 and i%5 == 0:
        print(i,'is divisble by 3 and 5,"Tecno soft"')
