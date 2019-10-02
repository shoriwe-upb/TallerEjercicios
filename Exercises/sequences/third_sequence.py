# I couldn't find a way to print symmetrically  the odd lines
def main():
    rows = int(input("Number of rows: "))
    for current_row in range(rows, -1, -1):
        if current_row % 2:
            continue
        print(int((rows-current_row) / 2)*" " + "-"*current_row + int((rows-current_row) / 2)*" ")


if __name__ == '__main__':
    main()
