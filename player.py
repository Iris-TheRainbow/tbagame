class player():
    def __init__(self):
        self.x = 3
        self.y = 4
        self.inventory = []
        self.weapons = []
        self.health = 20
    
    def takeDamage(self, damage):
        self.player.health += -damage
    
    def heal(self, damage):
        self.player.health += damage

    def checkInventory(self):
        for i in range(len(self.inventory)):
            print(self.inventory[i])