from Bio import PDB
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
pdbl = PDB.PDBList()
pdb_id = "1TUP"
filename = pdbl.retrieve_pdb_file(pdb_id,pdir = ".",file_format = "pdb")
parser = PDB.PDBParser(QUIET = True)
structure = parser.get_structure("protein",filename)
model = structure[0]
chain = model['A']
print("Chain ID: ",chain.id)
for residue in chain:
    print(residue) 
io = PDB.PDBIO()
io.set_structure(structure)
io.save("output.pdb")
