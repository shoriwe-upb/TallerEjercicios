def main():
    sum_ = 0
    for n in range(3):
        sum_ += float(input(f"Number {n+1}: "))
    print("med:", sum_ / 3)


if __name__ == '__main__':
    main()
