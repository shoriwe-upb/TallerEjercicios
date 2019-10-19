def main():
    evens = 0
    odds = 0
    fives = 0
    while evens < 10 and fives < 20:
        try:
            numero = float(input("Number: "))
            if numero % 2:
                if not numero % 5:
                    fives += 1
                odds += 1
            else:
                evens += 1
        except ValueError:
            pass
    print("evens", evens)
    print("Odds", odds)
    print("fives", fives)


if __name__ == '__main__':
    main()
