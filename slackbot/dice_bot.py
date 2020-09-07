from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.dispatcher import Message

import re


@listen_to('Hello', re.IGNORECASE)
def hello(msg: Message):
    msg.send('World!!')


@respond_to('hi', re.IGNORECASE)
def hi(msg: Message):
    msg.reply('Thank you 39!!')
