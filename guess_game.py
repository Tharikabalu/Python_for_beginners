secret_number=10
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    Guess=int(input('guess the number:'))
    if Guess==secret_number:
        print('you win!')
        break
    else:
        if guess_count==2:
            print('Game over')
        else:
            print('try again')

    guess_count+=1
