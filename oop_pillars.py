class CoffeeMachineBase:
    def make_coffee(self):
        pass

class BasicCoffeeMachine(CoffeeMachineBase):
    def __init__(self, water_amount_ml, coffee_ground_grams):
        self.__water = water_amount_ml
        self.__coffee = coffee_ground_grams

    def __brew_coffee(self):
        print("Grinding coffee and creating coffee base")

    def __boil_water(self):
        print(f"Boiling {self.__water} mL of water")

    def __pour_water_over_coffee(self):
        print("Pouring water over coffee grounds")

    def make_coffee(self):
        self.__brew_coffee()
        self.__boil_water()
        self.__pour_water_over_coffee()
        print("Your coffee is ready!\n")

class EspressoMachine(BasicCoffeeMachine):
    def __init__(self, water_amount_ml, coffee_ground_grams, pressure_bar):
        super().__init__(water_amount_ml, coffee_ground_grams)
        self.__pressure = pressure_bar

    def __apply_pressure(self):
        print(f"Applying pressure: {self.__pressure} bar")

    def make_coffee(self):
        self._BasicCoffeeMachine__brew_coffee()  
        self._BasicCoffeeMachine__boil_water()
        self._BasicCoffeeMachine__pour_water_over_coffee()
        self.__apply_pressure()
        print("Espresso is ready!\n")

def serve(coffee_machine: CoffeeMachineBase):
    coffee_machine.make_coffee()

def main():
    serve(BasicCoffeeMachine(200, 15))
    serve(EspressoMachine(50, 18, 9))

if __name__ == "__main__":
    main()

