def coordinate_input():
    x, y = input("X, Y Coordinates ==> ").strip().split(",")
    return float(x), float(y)

def main():
    coordinates = []
    print("Type the coordinates in order; it means A,B,C...")
    while True:
        try:
            point = coordinate_input()
            coordinates.append(point)
        except:
            break

    sumatory = 0
    for index, point in enumerate(coordinates):
        if index == len(coordinates) - 1:
            sumatory += point[0] * coordinates[0][1] - point[1] * coordinates[0][0]
        else:
            sumatory += point[0] * coordinates[index+1][1] - point[1] * coordinates[index+1][0]
    print("Area:", abs(sumatory / 2))

if __name__ == '__main__':
    main()