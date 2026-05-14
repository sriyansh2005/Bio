from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
dna_sequence = Seq("ATGCTAGCTAGCTAGCTG")
record = SeqRecord(
    dna_sequence,
    id = "Seq1",
    description = "Example DNA sequence",
    annotations = {
        "molecule_type": "DNA",
        "gene":"Seq1",
        "function":"unknown"
    }
)


out_file = r"C:\sriyansh\biopython\random.gb"
with open(out_file,"w") as output_file:
    SeqIO.write(record,output_file,"genbank")
print("Stored Successfully")
with open(out_file,"r") as input_file:
    record_read = SeqIO.read(input_file,"genbank")
print("\nContents of the GenBank file:")
print(record_read)
    
    