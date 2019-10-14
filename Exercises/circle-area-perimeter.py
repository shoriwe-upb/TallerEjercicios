from math import pi


def main():
    radius = float(input("Circle radius: "))
    print("Perimeter:", 2*pi*radius)
    print("Area:", pi*(radius**2))


if __name__ == '__main__':
    main()
