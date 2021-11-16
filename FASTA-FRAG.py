import argparse
from Bio import SeqIO
from Bio.SeqUtils import GC


parser = argparse.ArgumentParser(description="""FASTA FRAGMENTATION SCRIPT -  Meriam Guellil  -  March 2021 v.2.0""",epilog="""Last and first fragments can be shorter.""")
parser.add_argument('-i',metavar='Input', dest='fasta', required=True, type=str, help='FASTA file to be fragmented')
parser.add_argument('-s',metavar='Fragment Length', dest='CSize', required=True, default=50, type=int, nargs='*', help='Desired fragment lengths (Default: 50 bp)')
parser.add_argument('-t',metavar='Tiling', dest='Tiling', required=True, default=1, type=int, help='Desired depth of coverage across reference (Default: 1)')
parser.add_argument('-d',metavar='Interval Length', dest='IntSize', required=True, default=0, type=int, help='Displacement length between tilings in bp (Default: 0 bp)')
parser.add_argument('-o',metavar='Output', dest='outFASTA', required=True, type=str, help='Output')
args= parser.parse_args()

ID_DICT = {}
FASTA_DICT = {}

for record in SeqIO.parse(args.fasta,'fasta'):
    ID_DICT.update({str(record.id):str(record.seq)})

#Cutting and naming
for chr,seq in ID_DICT.items(): #for each chromosome
	for bp in args.CSize: #for each fragment size
		for a in range(0,args.Tiling): # for each tiling
			for i in range((int(a)*args.IntSize), len(seq), int(bp)):
				seq_f = str(seq[i:i+bp])
				GCPerc = ("%.0f" % GC(str(seq_f)))
				LN = len(seq_f)
				header = chr + "_" + str(i) + "-" + str(i+bp) + "_" + str(GCPerc) + "GC_" + str(LN) + "bp" 
				FASTA_DICT.update({header: seq_f}) 

#Output
with open (args.outFASTA,'a') as out_fasta:
    for ID,SEQ in FASTA_DICT.items():
        out_fasta.write('>' + str(ID) + '\n' + str(SEQ) + '\n')
