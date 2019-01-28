import command_system

def counter_sex():

    message = 'У тебя'
    return message, ''

hello_command = command_system.Command()
hello_command.keys = ['Сколько девушек', 'Сколько парней', 'Сколько баб']
hello_command.description = 'почитаю сколько у тебя в друзьях девушек и парней'
hello_command.process = counter_sex
#hello = command_system.command_list[0]
