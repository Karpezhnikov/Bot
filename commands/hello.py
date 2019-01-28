import command_system
# функции для сообщений
def hello():

    message = 'Привет)'
    return message, ''

hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'дратути', 'здравствуй', 'здравствуйте']
hello_command.description = 'поприветствую тебя'
hello_command.process = hello
#hello = command_system.command_list[0]
