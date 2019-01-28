#главный скрипт
from vk_api.longpoll import VkLongPoll, VkEventType
import ConnectAPI
import command_system
import os
import importlib
import time
import flask
from mysite import setting_key

connect_token = setting_key.connect_token  #ключ сообщества
ser_key_app = setting_key.ser_key_app  #ключ приложения

#импортирует файлы в которых лежат функции
def load_modules():
   # путь от рабочей директории, ее можно изменить в настройках приложения
   files = os.listdir("C:/Users/VivoBook/Desktop/боты вк/project/bot_site/mysite/commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])

def get_answer(body, user_id):
    #print('Новое сообщение:')
    message = 'Не могу понять.\n Набери "помощь", чтобы получить список команд'
    attacment = ''
    for Com_Sys in command_system.command_list:
        if body.lower() in Com_Sys._Command__keys:
            if body.lower() in ('виселица', 'го в виселицу', 'поиграем в виселицу'):
                message, attacment = Com_Sys.process(user_id)
            else:
                #print('Key_command = ', Com_Sys._Command__keys)
                message, attacment = Com_Sys.process()

            #print('Запущен процесс',Com_Sys.process())
            #print('Сообщение отправилось')
    return message, attacment







#разобраться с тем что сообщения распостраняются на 2 подключения








def main():
    load_modules() #инициализация всех функций
    longpoll = flask.connect_group() #подключение к группе

    #event.to_me - если сообщение оправлено от пользователя мне (True), если нет то (False)

    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW and event.to_me == True:


            #print('Event = ',event.__dict__)
            #print('Сообщение от пользоваеля', event.text)
            message, attacment = get_answer(event.text, event.user_id)
            print('Messege 1111')
            print('Event message ', event.__dict__)

            if event.text.lower() == 'сколько девушек': #считает сколько девушек у пользователя

                friends = ConnectAPI.get_friends(ser_key_app, event.user_id)#вызов метода (возвращает список друзей)
                items = friends['items']
                #print(items['last_name'])
                men = 0
                for i in items:
                    if i['sex'] == 2:
                        men = men+1
                women = friends['count']-men
                message = 'У тебя в друзьях '+str(women)+' девушек'+' и '+str(men)+' парней'
                print(women, men)

            ConnectAPI.send_message(connect_token, event.user_id, message, attacment)
            print('Отправили сообщение укцукцук')

            if event.from_me:
                print('От меня для: ', end='')
            elif event.to_me:
                print('Для меня от: ', end='')
#                ConnectAPI.send_message(connect_token, event.user_id, 'Привет', '')
#                #api.messages.send(access_token=connect_token, user_id=str(event.user_id), message='пРИВТЕ', attachment='')

        elif event.type == VkEventType.USER_TYPING:
            print('Печатает ', end='')
#на это можно сделать так, чтобы бот активировался
    #если пользователь печатает
            if event.from_user:
                print(event.user_id)
            elif event.from_group:
                print('администратор группы', event.group_id)

        elif event.type == VkEventType.USER_TYPING_IN_CHAT:
            print('Печатает ', event.user_id, 'в беседе', event.chat_id)

        elif event.type == VkEventType.USER_ONLINE:
            print('Пользователь', event.user_id, 'онлайн', event.platform)

        elif event.type == VkEventType.USER_OFFLINE:
            print('Пользователь', event.user_id, 'оффлайн', event.offline_type)

        else:
            continue

        time.sleep(1)
            #print(event.type, event.raw[1:])



if __name__=='__main__':
    main()




