guess_no = 8
i=1
while i <= 3:
    guess = int(input(f'{i} = Guess the no.'))
    if guess == guess_no:
        print(f' You have guessed the correct no. ie. {guess_no}')
        break
    else:
        i += 1
else:
    print(" Sorry, you failed. Better luck next time!!")