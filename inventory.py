class Inventory:
    def __init__(self, name = str, damage = int):
        self.name = name
        self.damage = damage
        
    def use(self):
        print(f"Using {self.name} with damage {self.damage}")
        
