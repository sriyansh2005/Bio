from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord 
dna_sequence = Seq("ATGCTAGCTAGCTAGCTG")
record = SeqRecord(
    dna_sequence,
    id = "Seq1",
    name = "Example_gene",
    description = "Example DNA sequence"
)
record.annotations["gene"] = "Seq1"
record.annotations["function"] = "hypothetical protein"
record.annotations["organism"] = "Synthetic organism"
from Bio.SeqFeature import SeqFeature,FeatureLocation
gene_feature = SeqFeature(
    FeatureLocation(0,21),
    type = "gene"
)
record.features.append(gene_feature)
record.annotations["function"] = "Hypothetical protein with modified function"
print(f"ID: {record.id}")
print(f"Name: {record.name}")
print(f"Description: {record.description}")
print(f"Annotations: {record.annotations}")
print(f"Features: {record.features}")
