class Room:
    def __init__(self, name: str):
        self.name = name


class House:
    def __init__(self):
        # The House creates and owns these Room objects directly.
        self.rooms = [Room("Kitchen"), Room("Bedroom")]


# --- Running the code ---
my_house = House()

for room in my_house.rooms:
    print(f"Room created: {room.name}")
