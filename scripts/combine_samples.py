import glob
import csv
import collections

combo = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(int)))

for fname in glob.glob("../work/validate/grading-summary*.csv"):
    with open(fname) as in_handle:
        reader = csv.reader(in_handle)
        reader.next()
        for _, caller, vtype, metric, value in reader:
            combo[caller][vtype][metric] += int(value)

with open("icr142-summary.csv", "w") as out_handle:
    writer = csv.writer(out_handle)
    writer.writerow(["sample", "caller", "vtype", "metric", "value"])
    for caller in sorted(combo.keys()):
        for vtype in sorted(combo[caller].keys()):
            for metric in sorted(combo[caller][vtype].keys()):
                writer.writerow(["ICR142", caller, vtype, metric, combo[caller][vtype][metric]])
