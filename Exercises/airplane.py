class Bag(float):
    def valid(self):
        return self <= 500

    def cost(self):
        if self.valid():
            return 0 if self <= 25 else (1500 * self if self <= 300 else 2500 * self)


class AirPlaneCargo(tuple):
    def __init__(self, bags: iter):
        self.__bags = bags
        self.__length = len(bags)

    def number_of_bags(self):
        return self.__length

    def heaviest(self):
        return max(self.__bags)

    def lighter(self):
        return min(self.__bags)

    def med(self):
        return sum(self.__bags) / self.__length

    def money_income(self):
        cop = sum(bag.cost() for bag in self.__bags)
        usd = cop * 3400
        return cop, usd

    def __len__(self):
        return self.__length


def number_input(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            pass


def main():
    bags = []
    for n in range(15):
        weigth = number_input(f"Bag {n+1} weigh: ")
        bags.append(Bag(weigth))
    cargo = AirPlaneCargo(bags)

    print()
    print("Number of bags:", cargo.number_of_bags())
    print("Heaviest bag:", cargo.heaviest())
    print("Lighter bag:", cargo.lighter())
    print("Med of weighs:", cargo.med())
    print("Incomes:\n\tUSD={}\n\tCOP={}".format(*cargo.money_income()))


if __name__ == '__main__':
    main()
