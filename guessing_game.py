print("This is guessing game. You will get a total of 5 chances to guess the number.")
n = 90
chances = 1


def game():
    global n
    global chances
    while chances <= 5:
        guessed_num = int(input("\nGuess the number: "))
        if 0 <= guessed_num < 50:
            print("You are way-way off. Go for something much bigger.")
        elif guessed_num >= 125:
            print("You are still way-way off. Go for something much smaller.")
        elif n > guessed_num >= 80:
            print("You are quite close. Go a bit higher.")
        elif n < guessed_num <= 100:
            print("You are quite close. Go a bit lower.")
        elif 50 <= guessed_num < 80:
            print("You are still off. Go higher.")
        elif 100 < guessed_num < 125:
            print("You are still off. Go lower.")
        else:
            print("Correct guess. You won, & consumed", chances, "chances. Congratulation!!!!")
            break
        print("Number of chances left :", 5 - chances)
        chances += 1

    if chances > 5:
        print("Game Over. Sorry you have exhausted all your chances. Better luck next time.")
        chances = 1
    response = (str(input("Do you want to try again? Type y or n: ")))

    for x in response:
        if x == 'y':
            chances = 1
            game()
        else:
            break


game()
