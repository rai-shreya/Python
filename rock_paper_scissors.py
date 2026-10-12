import random
list=["rock","paper","scissors"]
user=input("Enter your choice: rock,paper or scissors:")
comp=random.choice(list)
print("The computer chose:",comp)
print("You chose:",user)
if user==comp:
  print("It is a tie.")
elif user=="rock" and comp=="scissors":
  print("You win.")
elif user=="rock" and comp=="paper":
  print("You lose.")
elif user=="paper" and comp=="rock":
  print("You win.")
elif user=="paper" and comp=="scissors":
  print("You lose.")
elif user=="scissors" and comp=="paper":
  print("You win.")