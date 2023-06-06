from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Example aligned sequence data
aligned_sequences = {
    'Seq1': 'AGCCG',
    'Seq2': 'AGACG',
    'Seq3': 'ATAAG',
    'Seq4': 'ATGAG',
    'Seq5': 'ACGAG',
    'Seq6': 'ACTAG'
}

# Convert the aligned sequence data to a MultipleSeqAlignment object
alignment = MultipleSeqAlignment([
    SeqRecord(Seq(seq), id=name)
    for name, seq in aligned_sequences.items()
])

# Calculate the distance matrix
calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(alignment)

# Construct the neighbor-joining tree
constructor = DistanceTreeConstructor()
tree = constructor.nj(distance_matrix)

# Print and visualize the tree
Phylo.draw(tree)





