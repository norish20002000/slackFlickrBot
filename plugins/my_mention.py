# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import flickrBot

keyword = ""

@default_reply()
def default_dunc(message):
    keyword = message.body['text']

    msg = flickrBot.getFlickrImage(keyword)

    message.reply(msg)