level = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]
]

class player():
    def __init__(self):
        self.x = 3
        self.y = 4
        self.inventory = ['daggar', 'note']
        self.health = 20
player = player()

def process():
    while True:
        value = input("what will you do?\n").lower()
        if value.startswith('go '):
            value = value[3:]
        if value == 'up' or value == 'north':
            player.x += 1
        elif value == 'down' or value == 'south':
            player.x += -1
        elif value == 'left' or value == 'west':
            player.y += -1
        elif value == 'right' or value == 'east':
            player.y += 1
        elif value == 'help':
            print('movement:\nmove arond the map wiht cardinal directions (Nprth, South, East, West)')
            print('You can also move around with normal directions (Up, Down, Left, Right)')
            print('they may also start with \'go\'')
            input()
        elif value == 'attack':
            player.health += -1
            print(player.health)
        elif value == 'inventory':
            for i in range(len(player.inventory)):
                print(player.inventory[i])
            input()


        else:
            print("command not found, try something else (enter to continue)")
            input()
        

process()