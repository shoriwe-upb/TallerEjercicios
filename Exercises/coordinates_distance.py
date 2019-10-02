from math import sin, cos, pi
from math import acos as arccos


def read_coordinates():
    while True:
        try:
            x, y = (float(value) for value in input("x, y ===> ").strip().split(","))
            return x * pi / 180, y * pi / 180
        except ValueError:
            pass


def main():
    x1, y1 = read_coordinates()
    x2, y2 = read_coordinates()
    distance = 6371 * arccos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))
    print("Distance between both coordinates:", str(round(distance)) + "Km")


if __name__ == '__main__':
    main()
