name = input("Type your name: ")
print('Welcome', name + '!')

answer = input("You are on a dirt road, it has come to an end, and you can go left or right. Which way do you go? ").lower()

if answer == "left":
    answer = input('You come to a river. You can go around it or swim across. Type walk or swim. ').lower()

    if answer == 'swim':
        print('You swam across and were eaten by an aligator.')
    elif answer == 'walk':
        print('You walked for many miles, ran out of water and you lost the game')
    else:
        print("Not a valid option. You lose.")


elif answer == "right":
    answer = input("You come to a bridge. Do you want to cross it or head back? Type cross or back. ").lower()


    if answer == 'back':
        print('You go back and lose.')
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? Type yes or no. ")

    if answer == 'yes':
        print('You talk to the stranger and they give you gold. You win.')
    elif answer == 'no':
        print('You ignore the stranger and they are offended and you lose.')
    else:
        print("Not a valid option. You lose.")



print('Thank you for trying', name)

