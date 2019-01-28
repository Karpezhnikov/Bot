# главный скрипт
from vk_api.longpoll import VkLongPoll, VkEventType
import ConnectAPI
import flask
from mysite import vkapi
from mysite import setting_key
import os
from PIL import Image

#os.startfile(r'D:\picture.jpg')

connect_token = setting_key.connect_token
ser_key_app = setting_key.ser_key_app
group_id= setting_key.group_id

def viseliza_game(user_id):


    #всего 10 попыток
    #




    longpoll = flask.connect_group()# подключение к группе
    ConnectAPI.send_message(connect_token, user_id, 'Начнем игру!', '')
    #подготовим игру
    #нужно создать рандомайзер слов

    #разобраться с добавление фото

    word = 'окно'
    count_word = len(word)








    attacment =''
    message = 'Я придумал слово!\nОно начинается на ' +'"'+ word[0].upper()+'"'+ '\nУгадай слово!\nНапиши следущую букву' +'\nУ тебя есть 10 попыток'
    ConnectAPI.send_message(ser_key_app, user_id, message, attacment)
    #подготовка завершина
    win_game = 1 #счетчик правильных букв


    end_game = 0 #счетчик НЕ правильных букв



    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW and event.to_me == True:
            print('Пришло ссобщение')
            if event.text.lower() == word[win_game]:                                                                     #если угадал букву
                win_game += 1
                if win_game >= count_word:#для определения победы
                    message = 'Поздравляю! Ты выиграл!\nХочешь еще? Напиши "виселица"'
                    ConnectAPI.send_message(connect_token, user_id, message, '')
                    vkapi.main()  # перезапуск main чтобы не повторялись сообщения

                else:#для сообщения пользователю о том что он угадал
                    message = 'Ты угадал! '+ str(win_game) +'-ю букву'+'\n Давай дальше: ' + str(word[0:win_game]) + ('*'*(count_word-win_game))
                ConnectAPI.send_message(connect_token, user_id, message,'')

            elif event.text.lower() != word[win_game]: #and end_game !=count_word:                                       #если не угадал букву
                end_game += 1
                if end_game >= 10:  # если проиграл, то игра заканчивается(возврат в главный файл)
                    message = 'Ты проиграл\nХочешь еще? Напиши "виселица"'
                    attacment = ''
                    ConnectAPI.send_message(connect_token, user_id, message, '')
                    vkapi.main()  # перезапуск main чтобы не повторялись сообщения

                message = 'Ты не угадал! У тебя осталось '+str(10 - end_game)+' попыток'
                if end_game < 10:
                    ConnectAPI.send_message(connect_token, user_id, message, '')
                else:#блок для обозначения неправильной работы кода
                    ConnectAPI.send_message(connect_token, user_id, 'Что-то пошло не так', '')


            #if end_game >= count_word:#если проиграл, то игра заканчивается(возврат в главный файл)
             #   message = 'Ты проиграл\nХочешь еще? Напиши "виселица"'
              #  attacment = ''
               # ConnectAPI.send_message(connect_token, user_id, message, '')
                #vkapi.main()#перезапуск main чтобы не повторялись сообщения
                #break


            #if win_game >= count_word:#если виграл, предлагает сыграть еще раз(возврат в главный файл)
             #   message = 'Поздравляю! Ты выиграл!\nХочешь еще? Напиши "виселица"'
              #  attacment  = ''
               # vkapi.main()#перезапуск main чтобы не повторялись сообщения
                #break

    return message, attacment






































