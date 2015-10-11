from flask import current_app
from hashids import Hashids

class MessageBag(object):

    def __init__(self, status, message):
        self.status  = status
        self.message = message

class MessageHelper(object):

    @staticmethod
    def create(error, message):
        if error:
            return MessageHelper.error(message)
        else:
            return MessageHelper.ok(message)

    @staticmethod
    def error(message):
        return MessageBag('error', message)

    @staticmethod
    def ok(message):
        return MessageBag('ok', message)
