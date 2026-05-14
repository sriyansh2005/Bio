from Bio import AlignIO
from Bio.Align.Applications import MuscleCommandline

# Define sequences
seq1 = """>seq1
ATGCGTACGTA
"""
seq2 = """>seq2
ATGCGTACGTC
"""
seq3 = """>seq3
ATGCGTACGAG
"""

# Write sequences to file
with open("fasta8.fasta", "w") as f:
    f.write(seq1)
    f.write(seq2)
    f.write(seq3)

# MUSCLE executable
muscle_exe = r"muscle copy.exe.exe"  # or full path like r"C:\muscle.exe"

# Create command
import subprocess


subprocess.run([
    muscle_exe,
    "-align", "fasta8.fasta",
    "-output", "aligned_sequences.fasta"
], check=True)



# Read alignment
alignment = AlignIO.read("aligned_sequences.fasta", "fasta")

# Print result
print(alignment)