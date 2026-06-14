def parse_fasta(fasta_text):
    """
    Parses FASTA format string and returns a list of DNA strings.
    """
    lines = fasta_text.strip().split("\n")
    sequences = []
    current_seq = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if current_seq:
                sequences.append("".join(current_seq))
                current_seq = []
        else:
            current_read = line
            current_seq.append(current_read)
            
    if current_seq:
        sequences.append("".join(current_seq))
        
    return sequences

def find_subsequence_indices(s, t):
    """
    Finds one collection of 1-based indices of s in which the symbols 
    of t appear as a subsequence.
    """
    indices = []
    s_idx = 0
    
    for char in t:
        while s_idx < len(s) and s[s_idx] != char:
            s_idx += 1
            
        if s_idx < len(s):
            indices.append(s_idx + 1)
            s_idx += 1
        else:
            break
            
    return indices

def main():
    sample_fasta = """
>Rosalind_9394
TGGATTATTCTCACTTAGGGTTCCCGTTGCAAAGTCTTGTAAACAAAAGACAGCTTCGCG
AGCCTTTGGGATTGGTAAGCTCGTGGCAACCACCGACTTGAAACGGAAATCCGTACAGTC
GTGTGGACGGGGCGTTAGAAATCAACTTGAATGCCCTTCACTCCTCCGCGAAAGGGTGCC
AGATTCACACCATGTAACGATGCCCCCCTCTCTTGCCACCGAAACACCTAGCTCCTGTGG
AACCACCTATCGGCCCCTCCCTCGATACCCACAGTATCTAAATTAAGGTCTGGAACGACC
CTAAACAGCGGCAGACTTAAGGTATGCAAGTCAGGTGCCGGTTCATAGTACGGGGCGGAG
GTACCCAACTTTATGCCCAATCCTGTCTAAGGTATCATTAGGCGCCGGCATTTCCTAGTT
CTCAGAACGATATGGACGATTCTCCGCCCGACCTTAAGTTGCGGCCTCTGCCGGGACCAG
ACAACCGCGCGCGCATCAGAAAGGGGACGCACAACAATTCTCGGCGGTACTTAGATCACC
CGCCTGTAGTTCGATACCTTTAAGATCACACAAAAAGAGGTATCCTTTCGCTCCCTAAGG
CAAAAGCGGTAAGTATATCCCCGTCTCCACGATCCAGAAATTACCTCATAAGAGGGTACA
AGTTTCACATAACCCTCCCTCTTTGCTTAAATCATTCGTAAAAGTAGGGGCGCGTCGCTC
AAATCGACAGTCTGTGTGCGAATTCCGGGCACCGAACGTGGACGCTGGTCATGAGCGTTT
GCCAAGCTGTCGTCACTCTGCTTGTTAGCAATAATAATGATAGCGGGGGACATGGCAATT
GGAGCTGGGTCGGGAGCGTTGTGAATGCTCGCCAGCTCTCGCGCACGCCAGGGTACGTGG
TATCTTCTAATTCAAGTAGCGCTGACGGGAGGTAGCTATAATACCTGTCTAGAACTAGTG
GCTGAAAAGTGGTGCTGTCCAGTCTTGGCGCCAT
>Rosalind_1060
TAAACACAGGTAAGTAGTCCCGAGATACAGACCTGCAAGTGGCAGTGCGACTATAGAGGA
AGGGCTTGGGTCCTGTAGAAGGACG
"""
    sequences = parse_fasta(sample_fasta)
    if len(sequences) < 2:
        print("Error: Expected at least two sequences in FASTA format.")
        return
        
    s, t = sequences[0], sequences[1]
    result_indices = find_subsequence_indices(s, t)
    
    print("Source String (s):", s)
    print("Subsequence (t):  ", t)
    print("Matched Indices (1-based):")
    print(" ".join(map(str, result_indices)))

if __name__ == "__main__":
    main()