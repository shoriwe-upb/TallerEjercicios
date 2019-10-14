def main():
    money_received = int(input("Money received: "))
    price = int(input("Price: "))
    change = money_received - price
    result = {100000: 0, 50000: 0, 20000: 0, 10000: 0, 5000: 0, 2000: 0, 1000: 0}

    for key in result.keys():
        calculation = int(change / key)
        if calculation:
            result[key] = calculation
            change -= key * calculation
    print(result)


if __name__ == '__main__':
    main()
