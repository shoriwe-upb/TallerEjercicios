def main():
    a, b = input("A: "), input("B: ")
    print(f"A={a}\nB={b}")
    a, b = b, a
    print(f"A={a}\nB={b}")


if __name__ == '__main__':
    main()
