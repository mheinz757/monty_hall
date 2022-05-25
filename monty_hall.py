import random
import sys

if __name__ == "__main__":
    n = 10
    print(f"There are {n} doors in front of you, labeled 0 through {n-1}.\nBehind one of them is a car, while the other {n-1} have goats behind them.", end = "\n\n")

    # create a set of all doors
    idxs = set(range(n))

    # generate the car_idx and remove it from the idxs set
    car_idx = random.randint(0, n-1)
    idxs.remove(car_idx)

    # get the user_idx
    # user_idx = random.randint(0, n-1)
    while True:
        print(f"Which door would you like to select? Choose an integer between 0 and {n-1}.")
        try:
            user_idx = int(input("door> "))
        except ValueError:
            print(f"\nError: the door chosen must be an integer between 0 and {n-1}.")
        else:
            if user_idx not in range(n):
                print(f"\nError: the door chosen must be an integer between 0 and {n-1}.")
            else:
                print("")
                break
    
    # remove user_idx from idxs
    if user_idx in idxs:
        idxs.remove(user_idx)

    # find out which doors the quiz master opens
    removed_idxs = random.sample(idxs, n-2)
    for i in removed_idxs:
        idxs.remove(i)
    removed_idxs.sort()

    # Tell user which doors have been opened
    if n >= 5:
        print("The quiz master opens doors ", end = "")
        print(*removed_idxs[0:-1], sep = ", ", end = "")
        print(f", and {removed_idxs[-1]}, revealing a goat behind each one.")
    elif n == 4:
        print("The quiz master opens doors ", end = "")
        print(*removed_idxs, sep = " and ", end = "")
        print(f", revealing a goat behind both.")
    elif n == 3:
        print("The quiz master opens door ", end = "")
        print(*removed_idxs, end = "")
        print(f", revealing a goat.")

    # get the list of the doors remaining
    idxs.add(car_idx)
    idxs.add(user_idx)

    # Update user on remaining doors
    print("There are two doors remaining: ", end = "")
    print(*idxs, sep = " and ", end = ".\n")
    print(f"One of these has a car behind it and the other has a goat behind it.\nYou can either choose to stay with your original choice ({user_idx}), switch to the other door, or exit the program.", end = "\n\n")

    # let the user select a strategy
    while True:
        print("Which strategy would you like to choose?")
        print("switch) Switch to the other door")
        print("stay) Stay with original choice")
        print("exit) Exit the program")
        strategy = input("switch/stay/exit> ").strip().lower()
        print("")

        if strategy not in ["switch", "stay", "exit"]:
            print("Error: input must be either \"switch\", \"stay\", or \"exit\".")
        elif strategy == "exit":
            print("Exiting...")
            sys.exit()
        else:
            break

    # decide if you win or lose based on the users strategy
    if strategy == "switch":
        idxs.remove(user_idx)
        user_idx, = idxs
        print(f"You have switched to door {user_idx}. " , end = "")
        if car_idx in idxs:
            print("This door opens... revealing a car. YOU WIN!")
        else:
            print("This door opens... revealing a goat. You lose :(")
    elif strategy == "stay":
        print(f"You have stayed with door {user_idx}. " , end = "")
        if user_idx == car_idx:
            print("This door opens... revealing a car. YOU WIN!")
        else:
            print("This door opens... revealing a goat. You lose :(")