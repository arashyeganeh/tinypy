import csv


class TCsv:
    def read(self, src, encoding="utf-8", callback=None):
        try:
            with open(src, mode="r", encoding=encoding) as file:
                data = csv.DictReader(file)
                if callback:
                    return callback(data)

            return data

        except Exception as e:
            raise Exception(e)

    def write(self, data, dest, mode="w", encoding="UTF-8", newline=""):
        try:
            with open(dest, mode=mode, encoding=encoding, newline=newline) as file:
                writer = csv.DictWriter(file, fieldnames=data.keys())
                writer.writeheader()
                writer.writerow(data)

        except Exception as e:
            raise Exception(e)
