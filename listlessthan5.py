"""A program that prints out all the elements of the list that are less than 5"""
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list=[]
for i in list:
 if i<5:
  new_list.append(i)
print(new_list)
	   
