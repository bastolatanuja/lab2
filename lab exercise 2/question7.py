#game finding a secret number within 3 attempts using while loop.
secrect_number= 9
guess_count= 0
guess_limit= 3
while guess_count < guess_limit:
    guess=int(input("guess: "))
    guess_count +=1
    if guess==secrect_number:
        print("you won")
else:
    print("sorry,you failed")