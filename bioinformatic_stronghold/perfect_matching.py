import math

def parse_fasta(fasta_text):
    """
    Parses FASTA format string and returns the combined RNA string.
    """
    lines = fasta_text.strip().split("\n")
    sequence_parts = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            continue
        sequence_parts.append(line)
    return "".join(sequence_parts)

def count_perfect_matchings(rna_seq):
    """
    Calculates the total number of perfect matchings of basepair edges
    for the given RNA sequence.
    """
    num_A = rna_seq.count('A')
    num_C = rna_seq.count('C')
    
    # Total matchings = (num_A)! * (num_C)!
    return math.factorial(num_A) * math.factorial(num_C)

def main():
    # Sample Dataset
    sample_fasta = """
>Rosalind_2967
GAUAAUUCCGCAUCAGCCGCGACAUAGAAGAGGCGAAGCGCUGCUAGCCUUAUGGUUCCU
AAUCUUGCAGUUUCUAAGCG
"""
    rna_seq = parse_fasta(sample_fasta)
    result = count_perfect_matchings(rna_seq)
    
    print(f"RNA Sequence: {rna_seq}")
    print(f"Number of A (and U): {rna_seq.count('A')}")
    print(f"Number of C (and G): {rna_seq.count('C')}")
    print(f"Total Perfect Matchings: {result}")

if __name__ == "__main__":
    main()