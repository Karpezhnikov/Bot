import command_system
import flask
from game import viseliza

def visel(user_id):

   message = 'Что-то не так('
   message, attement = viseliza.viseliza_game(user_id) #запускаем игру


   return message, attement

visel_command = command_system.Command()

visel_command.keys = ['виселица', 'го в виселицу', 'поиграем в виселицу']
visel_command.desciption = 'сыграем в виселицу'
visel_command.process = visel