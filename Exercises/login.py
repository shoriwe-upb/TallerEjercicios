def login():
    for n in range(3):
        username = input("username: ")
        password = input("password: ")
        print()
        if username == "admin" and password == "super_secure":
            return True
    print("Nice try @ssh013")


def main():
    session = login()
    if session:
        print("Welcome")


if __name__ == '__main__':
    main()
