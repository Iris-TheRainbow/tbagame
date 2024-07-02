class commandHandler():
    def __init__(self, player):
        self.player = player
        self.command = ''

    def manual():
        print('movement:\nmove arond the map wiht cardinal directions (Nprth, South, East, West)')
        print('You can also move around with normal directions (Up, Down, Left, Right)')
        print('they may also start with \'go\'')
        input()

    def commandNotFound():
        print("command not found, try something else (enter to continue)")
        input()
    
    def inputCommand(self):
        self.command = input("What would you like to do?\n")

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
        self.command = command
    
    def parseCommand(self):
        command = self.command
        
        
