import csv
import glob
import os

truth_file = "../input/186c4726-ce81-493e-976f-d92de0f023e3.txt"
out_file = "icr142.csv"
samples = []
with open(truth_file) as in_handle:
    in_handle.readline()
    for line in in_handle:
        samples.append(line.split()[0])

with open(out_file, "w") as out_handle:
    writer = csv.writer(out_handle)
    writer.writerow(["samplename", "description", "variant_regions", "validate", "validate_regions"])
    for sample in sorted(list(set(samples))):
        fastqs = glob.glob("../input/fastqs/*_%s_*.fastq.gz" % sample)
        samplename = os.path.basename(os.path.commonprefix(fastqs))[:-2]
        writer.writerow([samplename, sample, "../input/truth/ICR142-%s-call.bed" % sample,
                         "../input/truth/ICR142-%s.vcf" % sample,
                         "../input/truth/ICR142-%s-validate.bed" % sample])
            



