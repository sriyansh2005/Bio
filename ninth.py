from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor,DistanceCalculator
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
alignment = MultipleSeqAlignment([
    SeqRecord(Seq("ATGCTAGCTAG"),id="Seq1"),
    SeqRecord(Seq("ATGCTAGCTAG"),id="Seq2"),
    SeqRecord(Seq("ATGCTAGCTAG"),id="Seq3")
])
calculator = DistanceCalculator()
distance_matrix = calculator.get_distance(alignment)
constructor = DistanceTreeConstructor()
tree = constructor.upgma(distance_matrix)
Phylo.draw(tree)