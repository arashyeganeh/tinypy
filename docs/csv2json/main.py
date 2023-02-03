import tinypy as tp

print(tp.__version__)
_tp = tp.Tinypy()
_tp.csv2json(src="sample.csv", dest="new-sample.json")
