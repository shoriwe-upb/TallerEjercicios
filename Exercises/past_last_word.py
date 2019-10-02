def main():
    text = input("Text: ").split(" ")
    if len(text) >= 2:
        print(text[-2])
    else:
        print("Not enough word")


if __name__ == '__main__':
    main()
