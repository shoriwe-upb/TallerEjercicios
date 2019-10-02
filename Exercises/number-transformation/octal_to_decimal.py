def octal_to_decimal_integer(number):
    if "." in number:
        number = number.split('.')[0]
    result = 0
    for index, multiplier in enumerate(range(len(number) - 1, -1, -1)):
        value = int(number[index])
        result += value * (8 ** multiplier)
    return result


def octal_to_decimal_fraction(number):
    if "." in number:
        number = number.split(".")[1]
    else:
        number = "0"
    result = 0
    for index, value in enumerate(number):
        value = int(value)
        result += value * (8 ** (-1 * (index + 1)))
    return result


def octal_to_decimal(number):
    integer_part = octal_to_decimal_integer(number)
    decimal_part = octal_to_decimal_fraction(number)
    return integer_part + decimal_part


def main():
    number = input("Octal: ")
    result = octal_to_decimal(number)
    print("Number:", result)


if __name__ == '__main__':
    main()
