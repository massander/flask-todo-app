# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

with open('data\data.txt') as file:
    try:
        data = file.readlines()
        group_id = data[0]
        token = data[1]
        login = data[2]
        password = data[3]
    except:
        pass

# # Authorization for user
# vk_session = vk_api.VkApi(login, password)
# vk_session.auth()

# Authorization for group using VkBotLongPoll
vk_session = vk_api.VkApi(token = token)
longpoll = VkLongPoll(vk_session)

vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        pass
