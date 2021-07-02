#Gussing the right number game
import random
import sys



number_of_chances =3
p=random.randint(1,100)#assume this the value we have to guess
print("Please guess the number between 1 to 100")
while True :
    n = int(input("Guesss the number:")) #we provide our number to check wheather we guesssed right or not
    if number_of_chances==0: #condition when we exhausted whole chances
        print("Better luck next Time!")
        print("Game over")
        print("Number guessed by the computer is:" + str(p))
        break #when we lost whole chances it will stop the code
    elif n==0: #as we provide the 0 it will show that the game is over
        print("game over")
        break
    elif n < p: # condition to check the number is greater/lesser/equal to numbr to  be guess
        print("Try bigger number!")
        number_of_chances -= 1 #after every wrong guesses we will lost one chance
        print(f"Remaining guess left:{number_of_chances}")
    elif n > p:
        print("Try smaller number!")
        number_of_chances -= 1
        print(f"Remaining guess left:{number_of_chances}")
    elif n == p :
        print("Awesome you won you guessed right number!!")
        print(f"Remaining guess left:{number_of_chances}")
        print("Run again the code ")

        break
    else:
        break


