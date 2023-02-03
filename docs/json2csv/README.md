# Usage

## Script

```python
import tinypy as tp

print(tp.__version__)
_tp = tp.Tinypy()
_tp.json2csv(src="sample.json", dest="new-sample.csv")
```

## Command Line Interface

```bash
tinypy -s sample.json -d new-sample.csv json2csv
```
