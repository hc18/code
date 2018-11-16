import pysam
samfile = pysam.AlignmentFile("tiny.bam", "rb")
for read in samfile:
     print (read)
