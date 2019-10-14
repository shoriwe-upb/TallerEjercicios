def read_xy(number):
    for symbol in "xy":
        yield float(input(f"{symbol}{number}: "))


def main():
    x, y = tuple(read_xy(1))
    x2, y2 = tuple(read_xy(2))
    print((((x2-x)**2)+((y2-y)**2))**(1/2))


if __name__ == '__main__':
    main()
