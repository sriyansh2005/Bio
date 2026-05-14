from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
dna_sequence = Seq("ATGCTAGCTAGCTAGCTG")
record = SeqRecord(
    dna_sequence,
    id = "Seq1",
    annotations = {
        "molecule_type":"DNA",
        "gene":"Seq1",
        "function:":"unknown"
    }
)
out_file = r"random.gb"
with open(out_file,"w") as f:
    SeqIO.write(record,f,"genbank")
with open(out_file,"r") as f:
    rand  = SeqIO.read(out_file,"genbank")
print(rand)

