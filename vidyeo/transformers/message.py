from .base import BaseTransformer

class MessageBagTransformer(BaseTransformer):

    def transform(self, message_bag):
        return {
            "status" : message_bag.status,
            "message": message_bag.message,
        }
