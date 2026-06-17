import random 
print("guess number between 1 and 20.")
random_number = random.randint(1,20)
i=0

while True:
    i+=1
    guess_number = int(input("Take a guess!\n"))
    if(guess_number<random_number and guess_number!=67):
        print("Your guess is too low.")
    elif(guess_number>random_number and guess_number!=67):
        print("Your guess is too high.")
    elif(guess_number== 67):
        print("SIXSEVEN, you win!")
        break
    else:
        print('Good job! Your guessed my number in {} guesses!'.format(i))
        break

    