import random
def guesser():
    right_number = random.randint(0,10)
    atempts = 0
    while True:
        try: 
            user_number = int(input("Try to guess number from 0 to 10: "))
        except ValueError:
            print("Error. You need to write number")
            continue    
        if user_number < right_number:
            user_number = int(input("Too small 😢. Try again! "))
            
            atempts +=1
        elif user_number > right_number:
            user_number = int(input("Too big 😢. Try again! "))
            atempts +=1
        else:
            print(f"You are right! 🎉🥳 The answer is {right_number} and you did it in {atempts+1} atempts")
            break
if __name__ == "__main__":
    guesser()
