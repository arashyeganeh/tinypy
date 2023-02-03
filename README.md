# tinypy

<p>
    <img alt="version" src="https://img.shields.io/badge/Version-0.0.3-green"/>
    <img alt="python" src="https://img.shields.io/badge/Python- > 3.6 -blue?logo=python&logoColor=white"/>
    <br>
    <a href="https://pypi.org/project/tinypy/">
        <img alt="version" src="https://img.shields.io/badge/pypi-tinypy-yellow"/>
    </a>
    <a href="https://github.com/arashyeganeh/tinypy">
        <img alt="version" src="https://img.shields.io/badge/Docs-github-lightslategrey"/>
    </a>
    <a href="https://github.com/arashyeganeh/tinypy/releases/tag/0.2.2">
        <img alt="version" src="https://img.shields.io/badge/Build-tar.gz | whl-lightseagreen"/>
    </a>
    <a href="https://github.com/arashyeganeh/tinypy/issues">
    	<img alt="version" src="https://img.shields.io/badge/issues-https://github.com/arashyeganeh/tinypy/issues-red"/>
    </a>
</p>


Tinypy is a collection of small Python functions and classes which make common patterns shorter and faster. All of these can be done by it:

* convert JSON files to CSV files
* convert CSV files to JSON files

## Installation

```bash
pip install tinypy
```

## Usage

### Script

You can also convert the JSON file to a CSV file by passing the "src "and "dest" directories to the function `json2csv(src, dest)`

```python
import tinypy as tp

_tp = tp.Tinypy()
_tp.json2csv(src="sample.json", dest="new-sample.csv")
```

This will convert the JSON file located at `sample.json` to a CSV file located at `new-sample.csv`.

### Command Line Interface

Tinypy also provides a command line interface for converting JSON files to CSV files.

```bash
tinypy -s sample.json -d new-sample.csv json2csv
```

This command will convert the JSON file located at `sample.json` to a CSV file located at `new-sample.csv`.

## Advanced Usage

To get more information, use -h or --help in Command Line Interface.

```bash
> tinypy -h

usage: tinypy [-h] [-v] -s import.json -d export.csv -a

Tinypy is a collection of small Python functions and classes which make common patterns shorter and faster.

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -s import.json, --src import.json
                        The path to the JSON file to convert
  -d export.csv, --dest export.csv
                        The path to the CSV file to create
  -a , --action         json2csv, csv2json

Documentation is available at the GitHub page: https://github.com/arashyeganeh/tinypy
```

### Options

#### action

| Action name |           Description           |                             Docs                             |
| :---------: | :-----------------------------: | :----------------------------------------------------------: |
|  json2csv   | convert JSON files to CSV files | [Read](https://github.com/arashyeganeh/tinypy/tree/main/docs/json2csv) |
|  csv2json   | convert CSV files to JSON files | [Read](https://github.com/arashyeganeh/tinypy/tree/main/docs/csv2json) |

## Requirements

- Python > 3.6

## License

This library is released under the MIT License.

## Contributing

The Tinypy project welcomes contributions. 

Please submit a pull request or an issue on GitHub if you have any improvements to suggest.

## Support

If you have any issues or questions, please feel free to reach out to us on [the GitHub](https://github.com/arashyeganeh/tinypy/issues).

## References

More information can be found on the [GitHub page](https://github.com/arashyeganeh/tinypy).
