from random import randint
guesses=1
hidden=randint(1,100)
while True:
    try:
        number=int(input("Guess a number between 1 and 100:"))
        if number<hidden:
            print("Too low try higher number...")
            number=int(input("Guess again:"))
            guesses+=1
        elif number>hidden:
            print("Too high try lower number...")
            number=int(input("Guess again:"))
            guesses+=1
        else:
            guesses+=1
            print(f"You got the number {hidden} at {guesses} guess(es)")
            break
    except ValueError:
        print("invalid number")
