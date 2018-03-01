'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)'''
print('Welcome to Rock, paper, scissor game') 
print('Press r for rock or s for scissor or p for paper')
user1=input('User1 make your selection: \n')
user2=input('User2 make your selection: \n')
if user1==user2:
 print("Please start again!")
elif user1=='r'and user2=='s':
 print("User1 wins")
elif user1=='s' and user2=='p':
 print("User1 wins")
elif user1=='p' and user2=='r':
 print("User1 wins")
elif user2=='r'and user1=='s':
 print("User2 wins")
elif user2=='s' and user1=='p':
 print("User2 wins")
elif user2=='p' and user1=='r':
 print("User2 wins")
else:
 print("Please make correct selection!")
print("Start over again?")


