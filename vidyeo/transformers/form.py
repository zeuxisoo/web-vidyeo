from .base import BaseTransformer

class FormErrorTransformer(BaseTransformer):

    def transform(self, errors):
        data = {}

        for name, errors in errors.items():
            for error in errors:
                data['message'] = error

        return data

class FormSuccessTransformer(BaseTransformer):

    def transform(self, message):
        return {
            message: message
        }
