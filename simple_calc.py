#A simple calculator
x=float(input ("Please input a number: "))
y=float(input("Please input another number: "))
c=input("Please select a to add,s to subtract,m to multiply or d to divide: ")
if c=='a':
	
	print (x+y)
elif c=='s':
 	print (x-y)
elif c=='m':
	print (x*y)
elif c=='d':
  	print (x/y)
else:
 	print("Please rerun the program")
 
