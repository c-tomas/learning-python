from time import time


print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != 'yes': 
    quit()

print("Okay! Let's play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Good job") 
    score += 1
else:
    print("Wrong answer!")

answer = input("What is the best game of 2022? ")
if answer.lower() == "elden ring":
    print("Good job") 
    score += 1
else:
    print("Wrong answer!")

answer = input("What is the best movie of 2022? ")
if answer.lower() == "the batman":
    print("Good job") 
    score += 1
else:
    print("Wrong answer!")

answer = input("What was the best death of the MCU? ")
if answer.lower() == "iron man":
    print("Good job") 
    score += 1
else:
    print("Wrong answer!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")
