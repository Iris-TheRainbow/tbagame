import command, level, player

player = player.player()
level = level.level()
handler = command.commandHandler(player)

 
while True:
    handler.inputCommand()
    handler.sanatizeCommand()
    handler.parseCommand()