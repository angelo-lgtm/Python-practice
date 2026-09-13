import random

print("WELCOME TO THE GUESSING GAME!\n To exit enter (-1)")
print("Guess between 1 - 100")

real = random.randint(1, 100)

while True:
    value = input("Enter the number to you guessed: ")
    number = int(value)
    if number == real:
        print("You guessed correct!!")
        break
    elif number > real and number < 100:
        print("Too high")
    elif number > 0 and number < real:
        print("To low")
    elif number == -1:
        break
    else:
        print("Invalid input try again")

print("Thank you playing our game!")
        