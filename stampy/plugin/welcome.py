#!/usr/bin/env python
# encoding: utf-8
#
# Description: Plugin for processing welcome to chats
# Author: Pablo Iranzo Gomez (Pablo.Iranzo@gmail.com)

import logging
import stampy.plugin.config
import stampy.stampy
from stampy.i18n import translate

_ = translate.ugettext


def init():
    """
    Initializes module
    :return: List of triggers for plugin
    """
    triggers = ["*"]
    return triggers


def run(message):  # do not edit this line
    """
    Executes plugin
    :param message: message to run against
    :return:
    """

    # Send greetings
    try:
        if 'new_chat_participant' in message['message']:
            welcomeuser(message=message)
    except:
        pass
    return


def help(message):  # do not edit this line
    """
    Returns help for plugin
    :param message: message to process
    :return: help text
    """

    commandtext = ""
    if stampy.stampy.is_owner_or_admin(message):
        commandtext = _("As admin or owner define 'welcome' to the greeting text sent to new chat members. You can use $username to put long name in the text\n\n")
    return commandtext


def welcomeuser(message):
    """
    Greets new users in chat
    :param message: Message to process for newcomer events
    :return:
    """
    logger = logging.getLogger(__name__)

    msgdetail = stampy.stampy.getmsgdetail(message=message)
    chat_id = msgdetail['chat_id']

    welcome = stampy.plugin.config.gconfig(key='welcome', default=False, gid=chat_id)
    greeting = welcome.replace("$username", msgdetail['name'])

    logger.debug(msg=_('New user in chat, sending greetings: %s') % greeting)

    if greeting:
        stampy.stampy.sendmessage(chat_id=msgdetail["chat_id"], text=greeting,
                                  reply_to_message_id=msgdetail["message_id"],
                                  parse_mode="Markdown")
    return
