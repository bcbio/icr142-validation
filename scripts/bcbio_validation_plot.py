import sys
from bcbio.variation import validateplot

title="ICR142: GATK HaplotypeCaller, FreeBayes, VarDict, Platypus"
validateplot.classifyplot_from_valfile(sys.argv[1], outtype="png", title=title)
