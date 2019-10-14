def main():
    distance = float(input("Distance: "))
    days = int(input("Days: "))
    if distance > 1000 and days > 7:
        discount = 0.85
    else:
        discount = 1
    result = distance * 5000 * discount
    if result < 100000:
        result = 100000
    print(result)


if __name__ == '__main__':
    main()
