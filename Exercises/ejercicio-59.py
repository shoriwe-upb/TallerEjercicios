def main():
    positives = 0
    negatives = 0
    evens = 0
    odds = 0
    eigth_multiple = 0
    while True:
        try:
            number = float(input("Number: "))
            if number < 0:
                negatives += 1
            else:
                positives += 1
            if number % 2:
                odds += 1
            else:
                evens += 1
            if not number % 8:
                eigth_multiple += 1
        except ValueError:
            break
    print("positivesp", positives)
    print("negatives", negatives)
    print("evens", evens)
    print("odds", odds)
    print("eigth_multiple", eigth_multiple)


if __name__ == '__main__':
    main()
