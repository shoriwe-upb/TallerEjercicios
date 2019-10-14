def main():
    time_ = float(input("Time: "))
    speed = float(input("Speed: "))
    acceleration = float(input("Acceleration: "))

    distance = speed * time_ + ((acceleration * (time_**2)) / 2)
    print(distance)


if __name__ == '__main__':
    main()
