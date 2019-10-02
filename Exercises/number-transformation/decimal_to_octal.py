def decimal_integer_to_octal(number):
    number = int(number)
    result = ""
    while number != 0:
        division = number / 8
        number = int(division)
        result += str(int((division - int(division)) * 8))
    return result[::-1]


def decimal_fraction_to_octal(number):
    result = ""
    number = number - int(number)
    while number != 0:
        number *= 8
        if int(number) > 0:
            result += str(int(number))
            number = number - int(number)
        else:
            result += "0"
    return result


def decimal_to_octal(number):
    integer_part = decimal_integer_to_octal(number)
    decimal_part = decimal_fraction_to_octal(number)
    if not len(integer_part):
        integer_part = "0"
    if len(decimal_part):
        decimal_part = "." + decimal_part
    return integer_part + decimal_part


def main():
    number = float(input("Number: "))
    result = decimal_to_octal(number)
    print("Octal:", result)


if __name__ == '__main__':
    main()
