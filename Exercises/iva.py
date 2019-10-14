def main():
    product_price = float(input("Price: "))
    iva_value = product_price * .19
    print("Original:", product_price)
    print("Iva price:", iva_value)
    print("Total:", product_price+iva_value)


if __name__ == '__main__':
    main()
