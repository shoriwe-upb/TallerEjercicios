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


def main():
    number = input("Number: ")
    binary = binary_to_decimal(number)
    print("Binary:", binary)


if __name__ == '__main__':
    main()
