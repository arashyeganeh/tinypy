import tinypy as tp

print(tp.__version__)
_tp = tp.Tinypy()
_tp.json2csv(src="sample.json", dest="new-sample.csv")
