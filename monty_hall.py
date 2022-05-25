import random

if __name__ == "__main__":
    n = 10
    idxs = set(range(n))
    car_idx = random.randint(0, n-1)
    idxs.remove(car_idx)

    user_idx = random.randint(0, n-1)
    if user_idx in idxs:
        idxs.remove(user_idx)

    print(idxs)
    print(user_idx)
    print(car_idx)
