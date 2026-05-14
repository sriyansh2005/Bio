from Bio.Seq import Seq
dna_sequence = Seq("ATGCTAGCTAGCTAGCTG")
dna_slice = dna_sequence[2:10]
print("dna_slice:", dna_slice)
dna_sequence2 = Seq("GGCTAG")
merged_dna = dna_slice + dna_sequence2
print("merged_dna:", merged_dna)
rma_sequence = merged_dna.transcribe()
print("rma_sequence:", rma_sequence)
protein_sequence = rma_sequence.translate()
print(protein_sequence)