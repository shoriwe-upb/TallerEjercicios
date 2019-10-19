def main():
    n = int(input("Numero: "))
    m = int(input("Numero: "))
    if n < m:
        if n < 0:
            n = 0
        for number in range(n, m+1):
            print(number)


if __name__ == '__main__':
    main()
