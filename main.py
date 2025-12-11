# This is an example of Abstraction and Encapsultation 

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


class CoffeeMachine:
    def __brew_coffee(self):
        print("brewing coffee")
    def __boil_water(self):
        print("boiling water")
    def __pour_water_over_coffee(self):
        print("pouring water over coffee")

    def make_coffee(self):
        # step1: berw coffee
        self.__brew_coffee()
        # step2: boil waterr
        self.__boil_water()
        #step3: pour water over coffee
        self.__pour_water_over_coffee()

        print("made coffee successsfully")

#This is an example of Inheretance and polymorphism

class Animal:
    def speak(self):
        print("default speak")

class Dog(Animal):
    def speak(self):
        print("bark!")


class Cat(Animal):
    def speak(self):
        print("meow!")



def make_animal_speak(animal):
    animal.speak()

def test_inheretance_polymorphism():
    print("------------------- implementing Inheretance and polymorphism ------------------------")
    animals = [Dog(), Cat()]
    for animal in animals:
        make_animal_speak(animal)

def test_abstraction_encapsulation():
    print("------------------- implementing abstraction and encapsulation ------------------------")
    coffee_machine = CoffeeMachine()
    coffee_machine.make_coffee()

    Bank_account = BankAccount(1000)
    print("Initial Balance:", Bank_account.get_balance())
    Bank_account.deposit(500)
    print("Balance after deposit:", Bank_account.get_balance())
    Bank_account.withdraw(300)
    print("Balance after withdrawal:", Bank_account.get_balance())

def main():

    test_abstraction_encapsulation()
    test_inheretance_polymorphism()

if __name__ == "__main__":
    main()

