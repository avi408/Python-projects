#Ask the user for a string and print out whether this string is a palindrome or not. 
word=str(input("please enter a word: \n"))
if word==word[::-1]:
 print ("This word is palindrome.")
else:
 print ("the word is not palidrome.") 

