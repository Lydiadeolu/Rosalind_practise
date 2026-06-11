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
            current_seq.append(line)
            
    if current_seq:
        sequences.append("".join(current_seq))
        
    return sequences

def find_lcs(s, t):
    """
    Computes the Longest Common Subsequence (LCS) of two strings s and t
    using dynamic programming.
    
    Returns:
        str: One longest common subsequence.
    """
    m, n = len(s), len(t)
    
    # Initialize DP table of size (m+1) x (n+1) with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    # Backtrack to reconstruct the LCS string
    lcs_chars = []
    i, j = m, n
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            lcs_chars.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    # The characters were gathered in reverse order during backtracking
    return "".join(reversed(lcs_chars))

def main():
    # Sample Dataset
    sample_fasta = """
>Rosalind_4616
AATGGAGAATCACGCCTGCTATTGTCCCCTGTTAGTCGCGATCAATCAGTCTTCTTAGCG
GAGGCAGCAACATGCGGCAACCGGAACCCGTAAAACCTAGCACTGATAATGTGCCGTTAA
ACTGTCCAATTCTAGTAGGCACCGGCCACAAACAGGTTGCTGGCGCTTCCTCTGCTTGAA
TCAACATTTGACTTGCCTGATGCTGTAAATGGGACGGTGCTTTGGCTTTACCACCCCCAT
GCGCGACCGAGCTTTATAACCTTGCCGGGACAGCAACAATTGAAATGCCCGAGGGACGTT
ATCGCACTGGCCCCGGATCATTCGGATGTCCTGCGAGAGCAACTGTCTTCTTGTGTCCTA
CACCACGACTGGCTTAGTACCTGATTTGCGGTCAACATTAAGTCGTTGCAGTAGGTTATC
TCAAGAAAAGGCGACACCTTTCCGAGGAATAAGCTACACGTCAATTCCTGCAGCACATCC
CCCGATAAAGAGCAGTTTACGTACAGGAAAACCTGACACATGATTCCAGCCCCTAGGCTC
ACTAGAAGTGAATTCGTAAACGCCCGGTATACAAGGGAGATCTCGCTTTTATAGCTATAT
TGCTGCCGAAAAACCGAGATATACCTTGTATTTCAGCGAGCCGAGACCAGTTTAGGTTCG
TCTTCGCTGGCCAAGTGCAATCAACTCAACTGAAACAATAGTTTGAATTGGGCTATAAAG
TATGCCTATCTATCTGTTTCAGGAACTGCGAGGAGGGTGCCTGGCACAATTCGTAAGCAA
ATATAACCTCTCCCTTCAGTAACCGGTCGTCCAAGTTTGCGTCATGCACAAACTGAACTC
TCAATTTCCTCCAGAGCCATAATCGAACGTCTTAGTGC
>Rosalind_9726
CGTTAGTCGCTTGCATAACGTCCGCCGAGAGTCCCCATCCACTACCTCAATCGTAAATTT
TGTCGGTTCAGCCGGTAGCTAGCGGGCCACCTCTCGTGCCCTCACACAGAACGCCGTTAT
TTGCAAGGATGATCAACCATGGCGCGTATGATGGGATGACATTGCAAACGTCGCAAGTTG
ACACGGTGCCGCAAAGCCTACTACGGTATTAGCCGGACGAGCTCTAGGGCTGTCATACGC
TAAAAAACAGAAATGCCTGGGCGCCATTACAGCGTGATCTAATTAGATCGGGGGCACACG
GGCAAGCGATGTACTGTAGGGCCATAGGTCATTGACCACCAGGAGCCTAGCACGCTCATG
TAAGCGGCATCCGAACGTGCGAACCTGTTGATGATTAGGGTACCGTGGCTCAGATATGTT
CTGAGGTCAAGTAGATAAGTTGGAGTCCAGGAGTGTTCTCCGCAGTACAACGAAAATAGG
CCATACTGGCTGTCTAAAGTATCTAGCCGTCTTGCAACCGTCACACTCAGTCTCACCAGC
GGCCTTCGGGTGAAATGCTCGCTGTTATTTCTCGGATCTTTCTTGGCTTCAGCTGAAAGG
CTGTCGTGCGCGACTGTCCACCTGTCAAAGTATACCCGTTGTCCACTTAATCTCCGATTC
TTTAAGGTAGAGTTGAATAGTGGCACCTTCTCGGGCTGCAATGAAACCACAAGCCGTAGG
TCAGTAGCCTGACCAAAATTTGCGCCCGGCTGGTTTGATAAAAGGAATCAAGCGACCTGT
TGGAAACCGCTGACCCGGCTTGTTAAACCCTGCGTCCCTAGGCTTGGAAAACATTACCAG
TTGTGTCTTTTATCATCCATCTGTGGGGTTTCTCGATAAAAGCTGCTTGTGACTCACGTG
"""
    sequences = parse_fasta(sample_fasta)
    if len(sequences) < 2:
        print("Error: Please provide at least two FASTA records.")
        return
        
    s, t = sequences[0], sequences[1]
    result_lcs = find_lcs(s, t)
    
    print(f"String s: {s}")
    print(f"String t: {t}")
    print(f"LCS:      {result_lcs}")

if __name__ == "__main__":
    main()