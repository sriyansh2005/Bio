import ssl
from Bio import Entrez

# Temporary SSL fix
ssl._create_default_https_context = ssl._create_unverified_context

# Your email
Entrez.email = "yourmail@gmail.com"

# Fetch sequence data
handle = Entrez.efetch(
    db="nucleotide",
    id="NM_001301717",
    rettype="fasta",
    retmode="text"
)

# Print output
data = handle.read()
print(data)

handle.close()