import sys

sys.setrecursionlimit(2000)

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

def count_noncrossing_perfect_matchings(rna_seq):
    """
    Calculates the total number of noncrossing perfect matchings of basepair edges
    in the bonding graph of s, modulo 1,000,000.
    """
    memo = {}
    n = len(rna_seq)
    
    allowed_pairs = {('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')}
    
    def dp(i, j):
        if i > j:
            return 1
        
        if (j - i + 1) % 2 != 0:
            return 0
            
        state = (i, j)
        if state in memo:
            return memo[state]
            
        total_matchings = 0
        char_i = rna_seq[i]
        
        for k in range(i + 1, j + 1, 2):
            if (char_i, rna_seq[k]) in allowed_pairs:
                left_matchings = dp(i + 1, k - 1)
                right_matchings = dp(k + 1, j)
                
                total_matchings += left_matchings * right_matchings
                total_matchings %= 1000000
                
        memo[state] = total_matchings
        return total_matchings

    return dp(0, n - 1)

def main():
    sample_fasta = """
>Rosalind_4444
AGUCUUAAGCGCGCGCGAAUUUUAAUAAUUAGCAAGAGCUCAUGCUCCGCGGGCCGCCGC
AUGUGCUGAGCUCAUAUAACUAGCGCGGUAUACCACGUGCGUGCGCGCACUAGUGCGUAU
AGCUACGCCCCGGGAGGUGCAUACCCGGGCGCUUAAGCGUACCUAUAUCUAAUGUUAAAG
CUAUAUCGCGCCGGCGGCGAUCUAUGCAAUAGCGUACUCCGUAAUGCCGGCGCGCGGCCG
AGUACUCG
"""
    rna_seq = parse_fasta(sample_fasta)
    result = count_noncrossing_perfect_matchings(rna_seq)
    
    print("RNA Sequence:", rna_seq)
    print("Total Noncrossing Perfect Matchings (modulo 1,000,000):")
    print(result)

if __name__ == "__main__":
    main()