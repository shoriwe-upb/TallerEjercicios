def main():
    numero = int(input("Numero: "))
    even = False
    for n in range(1, numero):
        if even:
            print(n*-1)
            even = False
        else:
            print(n)
            even = True


if __name__ == '__main__':
    main()
