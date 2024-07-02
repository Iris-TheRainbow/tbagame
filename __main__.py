import command, level, player

player = player()
process = command.commandHandler(player)
 
while True:
    process.inputCommand()
    process.sanatizeCommand()
    process.parseCommand()