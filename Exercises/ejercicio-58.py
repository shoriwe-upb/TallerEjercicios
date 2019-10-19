def main():
    smaller = 0
    bigger = 0
    while True:
        try:
            number = float(input("Number: "))
            if number > 100:
                bigger += 1
            elif number < 100:
                smaller += 1
        except ValueError:
            break
    print("Smaller: ", smaller)
    print("Bigger: ", bigger)


if __name__ == '__main__':
    main()
