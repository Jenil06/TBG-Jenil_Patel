class Character:
    def __init__(self, name = str, health = int, damage = int):
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = None

    def attack(self, target):
        damage_apply = self.damage
        if self.inventory:
            damage_apply = self.inventory.damage
        
        target.health -= damage_apply
        target.health = max(target.health, 0)
        

class  hero(Character):
    def __init__(self,name = str,health = int,damage = int):
        super().__init__(name=name, health=health, damage=damage)
        self.position = (0,0)
        self.game_over = False
    
class  enemy(Character):
    def __init__(self,name = str,health = int,damage = int):
        super().__init__(name=name, health=health, damage=damage)
        self.position = (2,4)

players = {'Peter':{'Full Name':'Peter Benjamin Parker',
                    'Health Points':200,
                    'Damage':10},
           'Miles':{'Full Name':'Miles Gonzalo Morales',
                    'Health Points':100,
                    'Damage':5},
           'Gwen':{'Full Name':'Gwendolyne Maxine Stacy',
                   'Health Points':100,
                   'Damage':5},
           'Miguel':{'Full Name':'Miguel O’Hara',
                     'Health Points':150,
                     'Damage':10}
          }
