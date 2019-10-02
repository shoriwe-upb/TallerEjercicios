# Based on https://www.youtube.com/watch?v=YQc2ysYubYc


# Transform the integer part of the number
def decimal_integer_to_binary(number):
    number = int(number)
    result = ""
    while number != 0:
        division = number % 2
        if division:
            result += "1"
        else:
            result += "0"
        number = int(number / 2)
    return result[::-1]


# Transform the decimal part of the number
def decimal_fraction_to_binary(number):
    number = number - int(number)
    result = ""
    while number != 0:
        number = number * 2
        if int(number) > 0:
            number = number - int(number)
            result += "1"
        else:
            result += "0"
    return result


def decimal_to_binary(number):

    integer_part = decimal_integer_to_binary(number)
    decimal_part = decimal_fraction_to_binary(number)
    if not len(integer_part):
        integer_part = "0"
    # when the decimal part wasn't ".0" add to it the dot to  verify that
    if len(decimal_part):
        decimal_part = "." + decimal_part
    return integer_part + decimal_part


def main():
    number = float(input("Decimal number: "))
    binary = decimal_to_binary(number)
    print("Binary:", binary)


if __name__ == '__main__':
    main()
