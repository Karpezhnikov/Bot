import command_system

def info():
   message = ''
   count_command = 0
   for c in command_system.command_list:
        count_command += 1
        message += str(count_command)+'. '+'Напиши ' +'"'+ c.keys[0] +'"'+ ' и я ' + c.description + '\n'
   return message, ''

info_command = command_system.Command()

info_command.keys = ['помощь', 'помоги', 'help']
info_command.desciption = 'покажу список команд'
info_command.process = info