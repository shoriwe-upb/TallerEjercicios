def factors(number):
    n = 2
    yield 1
    while int(number ** 1 / 2) + 1 > 1:
        if not number % n:
            number /= n
            yield n
        else:
            n += 1
        if number == 1:
            break


def main():
    number = int(input("Number: "))
    for divisor in factors(number):
        print(divisor)


if __name__ == '__main__':
    main()
