def main():
    number = float(input("Number: "))
    integer_part = int(number)
    decimal_part = number - integer_part

    print("Decimal:", decimal_part)
    print("Integer:", integer_part)


if __name__ == '__main__':
    main()
