# Based on https://www.youtube.com/watch?v=YQc2ysYubYc


# Transform the integer binary part of the number
def binary_to_decimal_integer(number):
    if "." in number:
        number = number.split(".")[0]
    result = 0
    for index, bit in enumerate(number[::-1]):
        if bit == "1":
            result += 2**index
    return result


# Transform the decimal binary part of the number
def binary_to_decimal_fraction(number):
    if "." in number:
        number = number.split(".")[1]
    else:
        number = "0"
    result = 0
    for index, bit in enumerate(number):
        result += int(bit) * (2**(-1*(index+1)))
    return result


def binary_to_decimal(number):
    integer_part = binary_to_decimal_integer(number)
    decimal_part = binary_to_decimal_fraction(number)
    return integer_part + decimal_part


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


def binary_to_octal(number):
    return decimal_to_octal(binary_to_decimal(number))


def main():
    number = input("Binary: ")
    result = binary_to_octal(number)
    print("Octal:", result)


if __name__ == '__main__':
    main()
