def main():
    object_a_mass = float(input("Object A mass: "))
    object_b_mass = float(input("Object B mass: "))
    distance = float(input("Distance between both: "))
    G = 6.67408 * (10**11)
    print(G*(object_a_mass*object_b_mass)/ (distance ** 2))


if __name__ == '__main__':
    main()
