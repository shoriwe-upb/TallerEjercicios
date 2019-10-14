def main():
    number = input("Number: ")
    print(number, number*2, number*3)
    print(sum(int(n) for n in (number, number*2, number*3)))


if __name__ == '__main__':
    main()
