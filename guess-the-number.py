import random

def guesser():
    right_number = random.randint(0, 10)
    attempts = 0 
    
    print("Welcome to Guess the Number! Try to guess number from 0 to 10.")

    while True:
        attempts += 1 
        
        try: 
            user_number = int(input(f"Attempt #{attempts}. Enter your guess: "))
        
        except ValueError:
            print("Error. You need to write a whole number (0-10).")
            attempts -= 1 
            continue    
        
        if user_number < right_number:
            print("Too small 😢. Try again!")
        
        elif user_number > right_number:
            print("Too big 😢. Try again!")
        
        else:
            print(f"You are right! 🎉🥳 The answer is {right_number} and you did it in {attempts} attempts.")
            break



if __name__ == "__main__":
    guesser()