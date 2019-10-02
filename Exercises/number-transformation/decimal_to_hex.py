ref = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


def decimal_integer_to_hex(number):
    number = int(number)
    result = ""
    while number != 0:
        division = number / 16
        number = int(division)
        hex_key = (division - int(division)) * 16
        result += ref.setdefault(hex_key, str(int(hex_key)))
    return result[::-1]


# I don't know why but this have a  little error margin
def decimal_fraction_to_hex(number):
    result = ""
    number = number - int(number)
    while number != 0:
        number *= 16
        if int(number) > 0:
            result += ref.setdefault(int(number), str(int(number)))
            number = number - int(number)
        else:
            result += "0"
    return result


def decimal_to_hex(number):
    integer_part = decimal_integer_to_hex(number)
    decimal_part = decimal_fraction_to_hex(number)

    if not len(integer_part):
        integer_part = "0"
    if len(decimal_part):
        decimal_part = "." + decimal_part
    return integer_part + decimal_part


def main():
    number = float(input("Number: "))
    result = decimal_to_hex(number)
    print("Hex:", result)


if __name__ == '__main__':
    main()
