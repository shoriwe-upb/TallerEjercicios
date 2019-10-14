def main():
    ref = (.15, .2, .15, .3, .2)
    final_grade = 0
    for index, value in enumerate(ref):
        grade = float(input(f"Grade {index+1}: "))
        final_grade += grade * value
    print(final_grade)
    if final_grade < 3:
        print("Perdio")
        if final_grade < 2:
            print("No puede habilitar")
    else:
        print("Aprobo")
        if final_grade > 4.5:
            print("Felicitacion")


if __name__ == '__main__':
    main()
