#Even or odd number
print ("This program shows if a number is even or odd and if a multiple of 4!")
a= int(input ("Please input a number: "))
mod= a%2
if mod==0:
	print (str(a) + ' is Even')

          
else:
        print(str(a) + 'is Odd')
if a%4==0:
	print (str(a) + ' is a multiple of 4')
