def main():
    sum_ = 0
    for n in range(10):
        numero = float(input(f"Number {n+1}:"))
        sum_ += numero
    print(sum_)
    print(sum_ / 10)


if __name__ == '__main__':
    main()
