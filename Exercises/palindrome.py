def main():
    text = input("Text: ")
    if text == text[::-1]:
        print("Is palindrome")
    else:
        print("Is not palindrome")


if __name__ == '__main__':
    main()
