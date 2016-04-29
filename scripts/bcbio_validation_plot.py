import sys
from bcbio.variation import validateplot

title="ICR142 initial validation: GATK HaplotypeCaller, FreeBayes, VarDict"
validateplot.classifyplot_from_valfile(sys.argv[1], outtype="png", title=title)
