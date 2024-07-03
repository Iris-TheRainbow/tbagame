import items

def save(level, player, name):
    with open(name, 'w') as f:
        f.write(str(name)+ '\n')
        f.write(str(player.x)+ '\n')
        f.write(str(player.y)+ '\n')
        f.write(str(player.health)+ '\n')
        for item in player.inventory:
            f.write(item.name + '\n')

def load(level, player, name):
    with open(name, 'r') as f:
        lines = f.readlines()
        player.x = lines[1]
        player.y = lines[2]
        player.health = lines[3]
        for i in range(3, len(lines)):
                if lines[i] == 'daggar':
                    print()
                    player.inventory.append(items.daggar())
                if lines[i] == 'sword':
                    player.inventory.append(items.sword())
                if lines[i] == 'oldkey':
                    player.inventory.append(items.oldKey())