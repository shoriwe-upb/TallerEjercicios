from collections import Counter


def main():
    text = input("Text: ")
    count_of_chars = Counter(text)
    for char in count_of_chars.keys():
        print(char, "==>", count_of_chars[char])


if __name__ == '__main__':
    main()
