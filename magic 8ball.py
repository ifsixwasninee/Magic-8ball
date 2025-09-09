# Imports a random range of integers for the function.
import random

# The random function is called to choose between a range of integers between 1-9.
random_number = random.randint(1, 9) 

# Question variable is created and used to input/initiate the game process.
question = random_number
question = input("What is your magic question?:")

# If, Elif, & Else statements are used to print various messages based on the initial terminal input.
if random_number == 1:
    print("Yes - definitely")
elif random_number == 2:
    print("It is decidedly so")
elif random_number == 3:
    print("Without a doubt.")
elif random_number == 4: 
    print("Reply hazy, try again.")
elif random_number == 5: 
    print("Ask again later.")
elif random_number == 6: 
    print("Better not tell you now.")
elif random_number == 7: 
    print("My sources say no.")
elif random_number == 8: 
    print("Outlook not so good.")
else: 
  print("Very doubtful.")

# Used as the print function, to output a message based on the random integers selected per use.
print(random_number)