ref = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


def hex_to_decimal_integer(number):
    if "." in number:
        number = number.split('.')[0]
    result = 0
    for index, multiplier in enumerate(range(len(number) - 1, -1, -1)):
        value = number[index]
        if value in ref.keys():
            value = ref[value]
        else:
            value = int(value)
        result += value * (16 ** multiplier)
    return result


# I don't know why but this have a  little error margin
def hex_to_decimal_fraction(number):
    if "." in number:
        number = number.split(".")[1]
    else:
        number = "0"
    result = 0
    for index, value in enumerate(number):
        if value in ref.keys():
            value = ref[value]
        else:
            value = int(value)
        result += int(value) * (16 ** (-1 * (index + 1)))
    return result


def hex_to_decimal(number):
    integer_part = hex_to_decimal_integer(number)
    decimal_part = hex_to_decimal_fraction(number)
    return integer_part + decimal_part


def main():
    number = input("Hex: ")
    result = hex_to_decimal(number)
    print("Number:", result)


if __name__ == '__main__':
    main()
