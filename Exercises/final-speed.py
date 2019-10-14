def main():
    time_ = float(input("Time: "))
    acceleration = float(input("Acceleration: "))
    distance = acceleration * (time_ ** 2)
    final_speed = (2*acceleration*distance) ** (1/2)

    print(final_speed)


if __name__ == '__main__':
    main()
