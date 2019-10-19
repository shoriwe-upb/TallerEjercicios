def main():
    while True:
        try:
            numero = int(input("Numero: "))
            if numero > 0:
                print(numero)
                break
        except ValueError:
            pass


if __name__ == '__main__':
    main()
