def main():
    numbers = []
    equals = 0
    for n in range(3):
        number = float(input(f"Number {n+1}: "))
        if number in numbers:
            equals += 1
            if equals == 2 and n == 2:
                equals += 1
        numbers.append(number)
    equals += 1 if equals == 1 else 0
    print(f"{equals} equal numbers")


if __name__ == '__main__':
    main()
