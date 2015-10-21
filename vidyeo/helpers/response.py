from flask import jsonify

class ResponseHelper(object):

    @staticmethod
    def item(data, transformer):
        transformed_data = transformer().transform(data)

        return jsonify(
            data=transformed_data
        )

    @staticmethod
    def collection(datas, transformer):
        transformer       = transformer()
        transformed_datas = [transformer.transform(data) for data in datas]

        return jsonify(
            data=transformed_datas
        )

    @staticmethod
    def status_code(error):
        return 400 if error else 200
