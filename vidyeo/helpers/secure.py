from flask import current_app
from hashids import Hashids

class SecureHelper(object):

    @staticmethod
    def encode_channel(channel):
        hash_ids = Hashids(
            salt=current_app.config['HASH_IDS_SALT'],
            min_length=current_app.config['HASH_IDS_MIN_LENGTH']
        )

        return hash_ids.encode(channel)
