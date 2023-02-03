import argparse


class Terminal:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="tinypy",
            description="Tinypy is a collection of small Python functions and classes which make common patterns shorter and faster.",
            epilog=f"Documentation is available at the GitHub page: https://github.com/arashyeganeh/tinypy  ",
        )
        self.verArg()
        self.srcArg()
        self.dstArg()
        self.actionArg()

    def verArg(self):
        self.parser.add_argument(
            "-v", "--version", action="version", version=f"%(prog)s 0.2.2"
        )

    def srcArg(self):
        return self.parser.add_argument(
            "-s",
            "--src",
            metavar="import.json",
            required=True,
            help="The path to the JSON file to convert",
        )

    def dstArg(self):
        return self.parser.add_argument(
            "-d",
            "--dest",
            metavar="export.csv",
            required=True,
            help="The path to the CSV file to create",
        )

    def actionArg(self):
        return self.parser.add_argument(
            "-a",
            "--action",
            metavar="",
            required=True,
            help="json2csv, csv2json",
        )

    def getParserArgs(self):
        return self.parser.parse_args()
