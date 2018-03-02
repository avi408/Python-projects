# This is incorrect but gives the english value of the integer entered as a list.


n = int(input ("Please type a number "))
dNames = ('zero','one','two','three','four','five','six','seven','eight','nine')
l = []
while n >0:
    currentDigit = n % 10
    l.append( dNames[currentDigit])
    n = n // 10
print (l)

