from flask import jsonify

class ResponseHelper(object):

    @staticmethod
    def item(data, transformer):
        transformed_data = transformer().transform(data)

        return jsonify(
            data=transformed_data
        )