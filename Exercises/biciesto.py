def main():
    year = int(input("Year: "))
    if not year % 4:
        if not year % 100:
            if not year % 400:
                print("Es biciesto")
            else:
                print("No es biciesto")
        else:
            print("No es biciiesto")
    else:
        print("No es biciesto")


if __name__ == '__main__':
    main()
