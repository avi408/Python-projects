"""a program that asks the user for a number and then prints out a list of all the divisors of that number."""
num=int(input("Please enter a number: "))
list=range(1,num)
list2=[]
for i in list:
 if num%i==0:
  list2.append(i)
print(list2)



