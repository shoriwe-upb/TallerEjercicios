def main():
    text = input("Text: ").split(" ")
    word = input("Word: ")
    if text[0].lower() == word.lower():
        print("They are the same")
    else:
        print("They are not the same")


if __name__ == '__main__':
    main()
