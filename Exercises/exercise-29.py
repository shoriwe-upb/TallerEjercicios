def main():
    number = int(input("Number: "))
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Is Zero")
    if number % 2:
        print("Es impar")
    else:
        print("Es par")


if __name__ == '__main__':
    main()
