import savegame
import items
class commandHandler():
    def __init__(self, player, level):
        self.player = player
        self.level = level
        self.command = ''

    def manual(self):
        print('movement:\nmove arond the map wiht cardinal directions (North, South, East, West)')
        print('You can also move around with normal directions (Up, Down, Left, Right)')
        print('they may also start with \'go\'')
        input()

    def commandNotFound(self):
        print("command not found, try something else (press enter to continue)")
        input()
    
    def emptyCommand(self):
        print('please enter an action (press enter to continue)')
    
    def inputCommand(self):
        self.command = input("What would you like to do?\n")
    
    def checkInventory(self):
        self.player.checkInventory()

    def sanatizeCommand(self):
        command = self.command
        command = command.lower()
        if command.startswith('go '):
            command = command[3:]
        if command == 'north':
            command = 'up'
        elif command == 'south':
            command = 'down'
        elif command == 'east':
            command = 'left'
        elif command == 'west':
            command = 'right'
        elif command == 'manual':
            command = 'help'
        elif command == 'man':
            command = 'help'
        self.command = command
    
    def parseCommand(self, debug = False):
        command = self.command
        
        if debug == True:
            if command == 'where am i':
                print((self.player.x, self.player.y))

            elif command.startswith('give '):
                self.items.give(self.player, command[5:])

            elif command.startswith('Set Health '):
                self.player.health = command[11:]

            elif command.startswith('go to '):
                self.player.x = input("x: ")
                self.player.y = input("y: ")

        if command == 'up':
            self.player.y += 1

        elif command == 'down':
            self.player.y += -1

        elif command == 'left':
            self.player.x += -1

        elif command == 'right':
            self.player.x += -1

        elif command == 'help':
            self.manual()

        elif command == 'inventory':
            self.checkInventory()

        elif command.startswith('save '):
            savegame.save(self.level, self.player, command[5:])

        elif command.startswith('load '):
            savegame.load(self.level, self.player, command[5:])

        elif command == 'stats': 
            print(self.player.health)
            self.checkInventory()

        elif command == 'exit':
            exit()

        else:
            self.commandNotFound()
    
    