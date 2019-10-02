from time import sleep


def main():
    buffer = ""
    buffer_length = 0
    current_size = 1
    number = 1
    try:
        while True:
            buffer += " " + str(number)
            buffer_length += 1
            if buffer_length == current_size:
                print(buffer)
                buffer = ""
                buffer_length = 0
                current_size += 1
            number += 1
            sleep(0.1)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
