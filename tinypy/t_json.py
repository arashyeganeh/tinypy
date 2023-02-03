import json


class TJson:
    def read(self, src, encoding="UTF-8", callback=None):
        try:
            with open(src, mode="r", encoding=encoding) as file:
                data = json.load(file)
                if callback:
                    return callback(data)

            return data

        except json.decoder.JSONDecodeError as e:
            raise Exception(e)

    def write(self, dest, data, mode="w", encoding="UTF-8"):
        try:
            with open(dest, mode=mode, encoding=encoding) as file:
                file.write(data)

        except json.decoder.JSONDecodeError as e:
            raise Exception(e)
