from Bio.Align import PairwiseAligner
from Bio.Seq import Seq
seq1 = Seq("ATGCTAGCTAGCTAGCTG")
seq2 = Seq("ATGCTAAGTAGCTAGCTG")
aligner = PairwiseAligner()
alignment = aligner.align(seq1,seq2)
print("Alignment Score:", alignment.score)
print("Aligned Sequences:",alignment[0])

