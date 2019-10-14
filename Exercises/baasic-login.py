def main():
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "password":
        print("Welcome")
    else:
        print("Wrong username or password")


if __name__ == '__main__':
    main()
