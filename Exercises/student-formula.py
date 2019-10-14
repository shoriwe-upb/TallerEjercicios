def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    inside_sqrt = ((b ** 2) - (4 * a * c))
    if inside_sqrt >= 0:
        print((-b + (inside_sqrt ** (1 / 2))) / (2 * a))
        print((-b - (inside_sqrt ** (1 / 2))) / (2 * a))
    else:
        print("Sin solucion")


if __name__ == '__main__':
    main()
