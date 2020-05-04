secret_word = "Python"
guess = ""
guess_count = 0
guess_limited = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limited:
        guess = input("Enter guess: ")
        guess_count += 1
        pass
    else:
        out_of_guesses = True
    pass

if out_of_guesses:
    print("Out of guesses, YOU LOSE!!!!")

else:
    print("Congratulate!!!! YOU WIN")
