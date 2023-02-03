# Usage

## Script

```python
import tinypy as tp

print(tp.__version__)
_tp = tp.Tinypy()
_tp.csv2json(src="sample.csv", dest="new-sample.json")
```

## Command Line Interface

```bash
tinypy -s sample.csv -d new-sample.json csv2json
```

