def main():
    count = 0
    sum_ = 0
    while True:
        try:
            number = float(input(f"Number {count+1}: "))
            count += 1
            sum_ += number
        except ValueError:
            if not count:
                count = 1
            break
    print(sum_)
    print(sum_ / count)


if __name__ == '__main__':
    main()
