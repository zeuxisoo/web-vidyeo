from .base import BaseTransformer

class StreamerTransformer(BaseTransformer):

    def transform(self, streamer):
        return {
            "id"     : streamer.id,
            "status" : streamer.status,
            "cover"  : streamer.cover,
            "channel": streamer.channel
        }
