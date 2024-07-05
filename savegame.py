import items
import os

def save(level, player, name):
    if not os.path.exists('savegame/'):
        os.mkdir('savegame/')
    with open('savegame/' + name, 'w') as f:
        f.write(str(name) + '\n')
        f.write(str(player.x) + '\n')
        f.write(str(player.y) + '\n')
        f.write(str(player.health) + '\n')
        for item in player.inventory:
            f.write(item.name + '\n')

def load(level, player, name):
    if os.path.exists('savegame/' + name):
        with open('savegame/' + name, 'r') as f:
            lines = f.readlines()
            print(lines)
            player.x = int(lines[1].strip())
            player.y = int(lines[2].strip())
            player.health = lines[3].strip()
            player.inventory = []
            for i in range(3, len(lines)):
                    item = lines[i].strip()
                    items.giveItem(player, item)
    else:
        print('Save: \'' + name + '\' does not exist')