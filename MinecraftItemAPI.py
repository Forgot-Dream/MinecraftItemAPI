# -*- coding: utf-8 -*-   

import json
ConfigFileFolder = 'config/'
ConfigFilePath = ConfigFileFolder + 'MinecraftItemAPI.json'

#判断是否为列表内物品
def getMinecraftItemInfo(Item):
    with open(ConfigFilePath , 'r') as f:
        js = json.load(f)
        list = js['minecraft_item']
        if Item in list:
            return True
        else:
            return False