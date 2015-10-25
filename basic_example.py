#!/usr/bin/env python
# -*- coding: utf-8 -*-


from baseGroupBot import BaseGroupBot

def simpleHandler(instance,  message):
        '''This handler will simply print received messages'''
        m = message.getBody()
        sender=message.getFrom()
        print str(sender)+" said "+str(m)

bgb = BaseGroupBot("your_user_name", "your_password", "roome_name", "your_nick_for_the_room")
bgb.connect()
bgb.addHandler("message", simpleHandler)
bgb.sendMessage("Hello world !")
bgb.listenInfinite()