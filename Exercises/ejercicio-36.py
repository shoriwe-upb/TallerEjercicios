def main():
    a = float(input("Number a: "))
    b = float(input("Number b: "))
    c = float(input("Number c: "))

    if a + b > c:
        print("Es mayor")
    elif a + b < c:
        print("Es menor")


if __name__ == '__main__':
    main()
