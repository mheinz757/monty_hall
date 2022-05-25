import random
import sys

if __name__ == "__main__":
    n = 10

    # create a set of all doors
    idxs = set(range(n))

    # generate the car_idx and remove it from the idxs set
    car_idx = random.randint(0, n-1)
    idxs.remove(car_idx)

    # get the user_idx
    # user_idx = random.randint(0, n-1)
    print(f"Which door would you like to select? Please enter an integer between 0 and {n-1}. If you would like to exit, please type \"exit\".")
    input1 = input()
    if input1 == "exit":
        print("Exiting...")
        sys.exit()
    user_idx = int(input1)
    while user_idx not in range(n):
        print(f"Error: door selected must be an integer between 0 and {n-1}.")
        print(f"Which door would you like to select? Please enter an integer between 0 and {n-1}. If you would like to exit, please type \"exit\".")
        input1 = input()
        if input1 == "exit":
            print("Exiting...")
            sys.exit()
        user_idx = int(input1)
    
    # remove user_idx from idxs
    if user_idx in idxs:
        idxs.remove(user_idx)

    # find out which doors the quiz_master opens
    removed_idxs = random.sample(idxs, n-2)
    for i in removed_idxs:
        idxs.remove(i)

    # get the list of the doors remaining
    idxs.add(car_idx)
    idxs.add(user_idx)

    # Update user on remaining doors

    # let the user select a strategy
    print("Which strategy would you like to choose: \"switch\" or \"stay\"? If you would like to exit, please type \"exit\".")
    input2 = input()
    if input2 == "exit":
        print("Exiting...")
        sys.exit()
    strategy = input2
    while strategy not in ["switch", "stay"]:
        print("Error: strategy must be either \"switch\" or \"stay\".")
        print("Which strategy would you like to choose: \"switch\" or \"stay\"? If you would like to exit, please type \"exit\".")
        input2 = input()
        if input2 == "exit":
            print("Exiting...")
            sys.exit()
        strategy = input2

    # decide if you win or lose based on the users strategy
    if strategy == "switch":
        idxs.remove(user_idx)
        if car_idx in idxs:
            print("YOU WIN!")
        else:
            print("You lose :(")
    elif strategy == "stay":
        if user_idx == car_idx:
            print("YOU WIN!")
        else:
            print("You lose :(")