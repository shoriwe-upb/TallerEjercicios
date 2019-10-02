from time import sleep


def main():
    buffer = ""
    number = 1
    try:
        while True:
            buffer += str(number)
            number += 1
            print(buffer)
            sleep(0.5)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
