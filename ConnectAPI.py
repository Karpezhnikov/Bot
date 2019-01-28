#Скрипт для всех методом VK
#используемых в коде
import vk


#для авторизации
session = vk.Session()
api = vk.API(session, v=5.85)

def send_message(token, user_id, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)

#метод получает друзей пользователя
#в качестве ключа используется ключ Standart-one приложения
def get_friends(token ,user_id):
    attachment = api.friends.get(user_id=user_id, access_token=token, fields='sex')
    return attachment

def message_delete (token, list_message):
    api.messages.delete(access_token=token, message_ids=list_message, spam=1, group_id=173819498)

def get_photo(token, owner_id, photo_ids):
    print(api.photos.get(owner_id=owner_id, album_id='profile', count=0, access_token=token)['count'])
    #photo = api.photos.get(owner_id=owner_id, album_id='wall', count=1, photo_ids=photo_ids, access_token=token)['items'][0]['id']
    attachment = ''#str(photo)
    return attachment

def get_Byld(token, photo_id):
    photo = api.photos.getByld(photos=photo_id, access_token=token)
    attacment = str(photo)
    return attacment

def photo_getAlbums (owner_id, album_ids, token):
    attacment = api.photos.getAlbums (owner_id=owner_id, album_ids=album_ids, access_token=token)
    print(attacment)




