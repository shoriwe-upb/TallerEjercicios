def main():
    n = int(input("Numero: "))
    m = int(input("Numero: "))
    sum_ = 0
    if n < m:
        if n < 0:
            n = 0
        for number in range(n, m+1):
            sum_ += number
    print(sum_)


if __name__ == '__main__':
    main()
