def main():
    a = float(input("Number a: "))
    b = float(input("Number b: "))
    c = float(input("Number c: "))
    if a > b:
        if a > c:
            print("A")
        elif a < c:
            print("C")
        else:
            print("A and C")
    elif a < b:
        if b > c:
            print("B")
        elif b < c:
            print("C")
        else:
            print("B and C")
    elif a < c:
        print("C")
    elif a > c:
        print("A and B")
    else:
        print("all =")


if __name__ == '__main__':
    main()
