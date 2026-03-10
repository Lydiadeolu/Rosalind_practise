def get_codon_table():
    return {
        'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
        'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
        'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
        'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
        'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
        'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
        'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'TAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
        'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }

def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(complement.get(base, base) for base in reversed(dna))

def translate_sequence(dna_seq, start_pos, table):
    protein = []
    for i in range(start_pos, len(dna_seq) - 2, 3):
        codon = dna_seq[i:i+3]
        amino_acid = table.get(codon)
        if amino_acid == 'Stop':
            return "".join(protein)
        if amino_acid is None:
            break
        protein.append(amino_acid)
    return None

def find_all_orfs(dna):
    table = get_codon_table()
    rev_dna = reverse_complement(dna)
    sequences = [dna, rev_dna]
    results = set()

    for s in sequences:
        for i in range(len(s) - 2):
            if s[i:i+3] == "ATG":
                candidate = translate_sequence(s, i, table)
                if candidate:
                    results.add(candidate)
    return results

fasta_data = """>>Rosalind_0262
TCTCTTGCGGGCCATAGATAGAAGTCGTTACTCGGACTTAGTGTGTTTATACTAGTGTAA
AAAGTAATGGTACACGAATCGGTTCTGTTTGCACCGGGCCTACGGTTCCCTTCCTTTAGC
GTTGAGGACTACTAAACGGATATATCCGAGGGGCATTGCTTAGTTAGTAACTTCCAACAG
TAGGGACACGCGGTCGCCACAAGAAAGCAGTGCGAGCTTGTGTCCTTCAATAAGCACGCA
TGGTGGAACCTAAGCTATTTCCCTAAGATGCCGGATCCCCTCTGTTTCATGCCATGGGTC
GCAACCCGACGCGTGATCTATTCGTGTGGTCCACCCGCAGCCAATGTCGTAGAGCAAGCA
CAGCTGTGAAAAGGGTAACCGTTGGCCCCAAAAACCAGTGGCGATCATGATGGTAACATC
TGTTTCTGCATGCGACAGTGAATAGCTATTCACTGTCGCATGCAGAAACAGATGTTACCA
TCCAGCTATTGGGGTTTGCCGTCCGGTTTTGCCAGTCTCATCAACCTAAAAAGTCGGCTA
GCTCTAGCCGACGAGAGTATATCCTCTTTACGCTGTTACTAGGCCTATCAGTATAGCTTG
ATCCGTGAACCAACTATTCTGTACTGAGGCAACTCTGCGCGCGCAAGCAGTTGATCCGGA
GCATTGTCTCTTCCCACCAGGTGGTAAGTCTCTGTAAACATTCTATCGAGGCGCCAGAAG
GCCAGCTCGGATAGTCAATCAGAGGTCTATAATTGTCGATCCAAATGCATCTAAGCTGGC
CTAGCACGTGTCCGTACACCACGCGCACTTAACTCAAGCTGTAGCAACCAGTGGAGGTTG
GATGCTCTGCCCCCTTAGAGGCAGGCCACGTTGCGTATCTCAACATGAC
"""

lines = fasta_data.splitlines()
dna_sequence = "".join(line.strip() for line in lines if not line.startswith(">"))

orfs = find_all_orfs(dna_sequence)
for protein in orfs:
    print(protein)