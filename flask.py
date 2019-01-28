import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from setting_key import connect_token
from mysite import vkapi

def connect_group():

    vk_session = vk_api.VkApi(
        token=connect_token)  # Авторизоваться как сообщество

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)

    #переменная в которую записывается
    #любое изменение в сообществе
    #мы получаем лист
    longpoll = VkLongPoll(vk_session)
    print('Соединение № 1 создано')
    return longpoll

def connect_group_2():

    vk_session = vk_api.VkApi(
        token=connect_token)  # Авторизоваться как сообщество

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)

    #переменная в которую записывается
    #любое изменение в сообществе
    #мы получаем лист
    longpoll = VkLongPoll(vk_session)
    print('Соединение № 1 создано')
    return longpoll
