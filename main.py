from random import randint
guesses=1
hidden_number=randint(1,100)
while True:
    try:
        user_choice=int(input("Guess a number between 1 and 100:"))
        if user_choice<hidden_number:
            print("Too low try higher number...")
            user_choice=int(input("Guess again:"))
            guesses+=1
        elif user_choice>hidden_number:
            print("Too high try lower number...")
            user_choice=int(input("Guess again:"))
            guesses+=1
        else:
            guesses+=1
            print(f"You got the number {hidden_number} at {guesses} guess(es)")
            break
    except ValueError:
        print("Invalid number")
