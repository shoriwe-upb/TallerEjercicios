def main():
    ref = "lunes,martes,miercoles,juevez,viernes,sabado,domindo".split(",")
    day = int(input("Day: ")) - 1
    print(ref[day])


if __name__ == '__main__':
    main()
