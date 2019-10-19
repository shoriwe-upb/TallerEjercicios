def main():
    even_sum = 0
    even_count = 0
    odd_sum = 0
    odd_count = 0
    while True:
        try:
            number = float(input(f"Number {even_count + odd_count + 1}: "))
            if not number % 2:
                even_sum += number
                even_count += 1
            else:
                odd_sum += number
                odd_count += 1
        except ValueError:
            if not even_count:
                even_count = 1
            if not odd_count:
                odd_count = 1
            break
    print("Even sum", even_sum)
    print("Even med", even_sum/even_count)
    print("Odd sum", odd_sum)
    print("Odd med", odd_sum / odd_count)


if __name__ == '__main__':
    main()
