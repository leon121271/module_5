class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f"Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


h = House('ЖК Эльбрус', 30)
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

print(h.name, h.number_of_floors)
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)

h.go_to(-3)
h1.go_to(5)
h2.go_to(10)