import command, level, player

player = player.player()
level = level.level()
handler = command.commandHandler(player, level)

 
while True:
    handler.inputCommand()
    handler.sanatizeCommand()
    handler.parseCommand()