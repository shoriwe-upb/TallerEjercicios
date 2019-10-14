def main():
    price = float(input("Price: "))
    iva = price * 0.19
    final_price = price + iva
    if iva > 150000:
        final_price *= 0.95
    print(final_price)


if __name__ == '__main__':
    main()
