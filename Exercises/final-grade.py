def main():
    ref = (.15, .2, .15, .3, .2)
    final_grade = 0
    for index, value in enumerate(ref):
        grade = float(input(f"Grade {index+1}: "))
        final_grade += grade * value

    print("Final grade:", final_grade)


if __name__ == '__main__':
    main()
