def request_numbers():
    numbers = []
    for n in range(3):
        number = float(input("Number: "))
        numbers.append(number)
    return numbers


def main():
    numbers = request_numbers()
    ordered = list(sorted(numbers))
    if numbers == ordered:
        print("Aumentando")
    elif numbers == ordered[::-1]:
        print("Disminiyendo")
    else:
        print("Ninguno")


if __name__ == '__main__':
    main()
