#!/usr/bin/env python3
import json
from .terminal import Terminal
from .t_json import TJson
from .t_csv import TCsv


class Tinypy:
    def json2csv(self, src, dest):
        _tjson = TJson()
        jsonData = _tjson.read(src)
        _tcsv = TCsv()
        _tcsv.write(jsonData, dest)

    def csv2json(self, src, dest):
        def parseCsv(data):
            jsonArray = []
            for row in data:
                jsonArray.append(row)
            return jsonArray

        _tcsv = TCsv()
        csvData = _tcsv.read(src, callback=parseCsv)
        jsonString = json.dumps(csvData, indent=4)
        _tjson = TJson()
        _tjson.write(dest, data=jsonString)


def main():
    _terminal = Terminal()
    args = _terminal.getParserArgs()

    _tinypy = Tinypy()
    if args.action == "json2csv":
        _tinypy.json2csv(args.src, args.dest)

    elif args.action == "csv2json":
        _tinypy.csv2json(args.src, args.dest)

    else:
        print("'--action' or '-a' value is incorrect!")


if __name__ == "__main__":
    main()
