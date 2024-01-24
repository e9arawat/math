"""Day-31"""


def total_coins(coins, required_sum, n):
    """recursive function"""
    coins_list = [0 for k in range(required_sum + 1)]
    coins_list[0] = 1
    for i in range(0, n):
        for j in range(coins[i], required_sum + 1):
            coins_list[j] += coins_list[j - coins[i]]

    return coins_list[required_sum]


def solver(amount: str):
    """function to find total coins required"""
    if amount == "£2":
        required_sum = 200
    elif amount == "£1":
        required_sum = 100
    else:
        required_sum = int(amount)
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    return total_coins(coins, required_sum, 8)


def answer():
    """calling solver function"""
    return solver("£2")


if __name__ == "__main__":
    print(answer())
    print(solver("150"))
