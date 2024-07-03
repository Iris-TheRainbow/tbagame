#itemManfest = [daggar]
class daggar():
    def __init__(self):
        self.type = 'weapon'
        self.name = 'daggar'
        self.damage = 1
        self.speed = 7

class sword():
    def __init__(self):
        self.type = 'weapon'
        self.name = 'sword'
        self.damage = 4
        self.speed = 3

class oldKey():
    def __init__(self):
        self.type = 'key'
        self.name = 'old key'
        self.keylevel = 0
    
def giveItem(player, item):
    if item == 'daggar':
        player.inventory.append(daggar())
    if item == 'sword':
        print('sword')
        player.inventory.append(sword())
    if item == 'old key':
        player.inventory.append(oldKey())