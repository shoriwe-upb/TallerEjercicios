def main():
    a = float(input("Number a: "))
    b = float(input("Number b: "))
    c = float(input("Number c: "))
    if a > b:
        if a > c:
            print("Higher","A")
        elif a < c:
            print("Higher","C")
        else:
            print("Higher","A and C")
    elif a < b:
        if b > c:
            print("Higher","B")
        elif b < c:
            print("Higher","C")
        else:
            print("Higher","B and C")
    elif a < c:
        print("Higher", "C")
    elif a > c:
        print("Higher","A and B")
    else:
        print("all =")
    ref = (a, b, c)
    print("Smallest", "ABC"[ref.index(min(ref))])


if __name__ == '__main__':
    main()
