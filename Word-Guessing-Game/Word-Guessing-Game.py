import random

def wordGuessingGame():
    words = ["software","python","november","laptop","headphone","football","hangman","cheese"]
    word = random.choice(words)
    guess = []
    attempts = 5

    while attempts>0:
        empty_word=""
        for i in word:
            if i in guess:
                empty_word+=i+" "
            else:
                empty_word+="_ "
        print(empty_word)
        new_guess = input("guess a letter: ").lower()
        if new_guess in guess:
            print("you guessed that letter already!!")
            continue
        guess.append(new_guess)
        if new_guess in word:
            print("Right guess! Attempts left : ", attempts)
        else:
            attempts-=1
            print("Wrong guess! Attempts left : ", attempts)

        right_guess = True
        for letter in word:
            if letter not in guess:
                right_guess = False
                break

        if right_guess:
            print("Congratulations! You guessed the word:",word)
            break
    if attempts<=0:
        print("Sorry! You lost! The word was: ",word)  

wordGuessingGame()