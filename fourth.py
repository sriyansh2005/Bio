from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
def convert_fasta_to_genbank(fasta_file,genbank_file):
    records = []
    for record in SeqIO.parse(fasta_file,"fasta"):
        sequence = record.seq
        description = record.description
        genbank_record = SeqRecord(
            sequence,
            id = record.id,
            name = "Example_gene",
            description = description,
            annotations = {
                "molecule_type": "DNA",
                "gene": record.id,
                "function": "unknown"
            }
        )
        records.append(genbank_record)
    with open(genbank_file,"w") as output_file:
        SeqIO.write(records,output_file,"genbank")
fasta_file = "fasta_1 (1).fasta"
genbank_file = "converted_genbank.gb"
convert_fasta_to_genbank(fasta_file, genbank_file)
print("\nContents of the GenBank file:")
with open(genbank_file,"r") as input_file:
    for record_read in SeqIO.parse(input_file,"genbank"):
        print(record_read)
            
        
        