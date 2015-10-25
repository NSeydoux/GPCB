#!/usr/bin/python

'''
baseGroupBot - A basic bot that connects to a chatroom and listens to messages
'''

import xmpp

class BaseGroupBot():
    def __init__(self, jid, passwd, room, nick=None):
        'The JID shall be formated as follow : "user_name@server.com". The room name must also be in its complete form : "room_name@muc.server.com"'
        self.jid=xmpp.protocol.JID(jid)
        self.client=xmpp.Client(self.jid.getDomain(), debug=[])
        self.passwd = passwd
        self.room = room
        if(nick != None):
            self.nick = nick
        else:
            self.nick = self.jid.getNode()

    def connect(self, server=None, port=None, status="Available"):
        'Connects the bot to server, authenticates and sends a presence message to the server and to the room'
        if server != None and port != None:
            self.client.connect((server, port))
        else:
            # Connects to the default server/port combination deduced from the JID
            self.client.connect()
        self.client.auth(self.jid.getNode(), self.passwd)
        self.client.sendInitPresence()
        self.client.send(xmpp.Presence(to="{0}/{1}".format(self.room, self.nick), status=status))

    def sendMessage(self, body):
        'Sends a group message to the room'
        self.client.send(xmpp.protocol.Message(to=self.room, typ="groupchat", body=body))

    def addHandler(self, handlerType, handler):
        'Defines a new handler for the client'
        self.client.RegisterHandler(handlerType, handler)

    def listenInfinite(self):
        'Receives messages from the room and reacts accordingly with defined handlers. No stop condition'
        while True:
            self.client.Process(1)
