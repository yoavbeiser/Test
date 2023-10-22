
class Person:
    number_of_people = 0

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return f"name is {self.name} and {self.age} years old"

    def __eq__(self, other):
        print("equals method called")
        return self.age == other.age and self.name == other.name
def greeting():
    name = input("what is your name?: ")
    print(f"Hello {name}")
def run():
    print("welcome...")
    greeting()

if __name__ == "__main__":
    run()