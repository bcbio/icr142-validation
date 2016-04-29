#!/usr/bin/env python
"""Identify likely homozgyous variants after an initial validation run.

The truth set does not contain genotype information, so this identifies zygosity
mismatched calls after an initial validation against all heterozygous truth
sets.
"""

import glob
import gzip
import os

def get_key(line):
    chrom, pos, _, ref, alt = line.split("\t")[:5]
    return (chrom, pos, ref, alt)

for rtg_dir in glob.glob("../work/validate/*/gatk-haplotype/rtg"):
    fp = os.path.join(rtg_dir, "fp.vcf.gz")
    fn = os.path.join(rtg_dir, "fn.vcf.gz")
    if os.path.exists(fp) and os.path.exists(fn):
        with gzip.open(fp) as fp_handle:
            fp_keys = set([get_key(line) for line in fp_handle if not line.startswith("#")])
        with gzip.open(fn) as fn_handle:
            fn_keys = set([get_key(line) for line in fn_handle if not line.startswith("#")])
        overlap = fp_keys & fn_keys
        if len(overlap) > 0:
            sample = rtg_dir.split("/")[3]
            for chrom, pos, ref, alt in list(overlap):
                print ",".join([sample, chrom, pos, ref, alt])
