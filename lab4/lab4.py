class Chainsaw:

    def __init__(self, name='Shtil', power=0, chain_speed=0):
        self.__name = name
        self.__power = power
        self.__chain_speed = chain_speed

        self.hours = 10
        self.weight = 0
        self.color = "Orange"

    def get_hours(self):
        return self.hours

    def set_hours(self, hours):
        self.hours += hours

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power

    def get_chain_speed(self):
        return self.__chain_speed

    def set_chain_speed(self, chain_speed):
        self.__chain_speed = chain_speed

    def __str__(self):
        return f'Chainsaw: name={self.__name}, power={self.__power}, chain_speed={self.__chain_speed}, hours={self.hours}'

    def __repr__(self):
        return f"Chainsaw('{self.__name}', {self.__power}, {self.__chain_speed}, {self.hours})"

    @classmethod
    def create(cls, name, power, chain_speed, weight, color, hours):
        obj = cls(name, power, chain_speed)
        obj.weight = weight
        obj.color = color
        obj.hours = hours
        return obj

    def __del__(self):
        print(f'{self.__name}, {self.__power}, {self.__chain_speed} has been deleted')


def main():
    chainsaw_1 = Chainsaw.create("Stihl MS 180", 1500, 9000, 7, "red", 10)
    chainsaw_2 = Chainsaw.create("Husqvarna 120", 1600, 8500, 6, "orange", 12)
    chainsaw_3 = Chainsaw.create("Makita UC4051A", 1800, 9200, 5, "blue", 13)
    chainsaw_1.set_hours(255)
    chainsaw_2.set_hours(22)
    chainsaw_3.set_hours(3)

    lst = [chainsaw_1, chainsaw_2, chainsaw_3]
    mx = lst[0]
    for chainsaw in lst:
        if chainsaw.get_hours() > mx.get_hours():
            mx = chainsaw_1
    print('Бензопила в якої найбільший час роботи :', mx)
    print(chainsaw_1, chainsaw_2, chainsaw_3, sep='\n')


if __name__ == "__main__":
    main()