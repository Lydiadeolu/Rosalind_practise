def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(complement.get(base, base) for base in reversed(dna))

def find_reverse_palindromes(dna_string, min_len=4, max_len=12):
    results = []
    n = len(dna_string)
    
    for length in range(min_len, max_len + 1):
        for i in range(n - length + 1):
            substring = dna_string[i:i+length]
            if substring == reverse_complement(substring):
                results.append((i + 1, length))
    
    return results

def parse_fasta(fasta_data):
    lines = fasta_data.strip().split('\n')
    sequence = ""
    for line in lines:
        if not line.startswith(">"):
            sequence += line.strip()
    return sequence

if __name__ == "__main__":
    sample_fasta = """>Rosalind_7492
CGCGGGCCGCTTGCGTATTCAGAGTTGCCGGTGCGCTTGTTTCCAGCATCGGTGACCATA
GGAGTTGCAAATATCACTTGTTGTCGAATAAAAAGTAGCCATGCTTAGTCTGCGATTTCC
TGAGAAAACGCCGCGCTCCCACCATTGTAACCTTGATCGAGCCGCCAGACGGACGGGGAA
TAATGGGTGAGACGACTCGGTGTTACATCAAAAGAAGGTGTAATAGATTCATCTCCGTTC
CACACCACGTTAACGATTTAGGTCCGAATATGAATTAAGTGCCCAAGGATTATCCTTCCG
TGGCCAGATCTACACACACGCGAGGGGCTTTTTGATCTGACCGTCCGTGGAATGCGCGCT
TCTGGATTAGTCAAGACAACCGGCACAATCCATCAGTAGTAATAAACTATGGACGCATCG
AGCCGGCTCGGAAAGTAGACCGGCGACCACGAACCCACATAAGAGCTTAAGGTTAAGATG
GTTAACAGGGACAGTCCGATCTCCCCTATACCACGGGAAGCTCATCGGTTGTCGTCGTGC
ATCTTGTAATGGAAGGCCACGTGCTCCGTGTCCATATACACCTCAACATTAGTTAGGTCG
CGACCAATAGCCGACAAACGTAATATAGATTGGAACCTGGGAGATTGCACAACAAATCTG
CCTGTTAACCCTAGGCCGGTAAATTTTGAGGGATTCTTACCACTCTTATACTATCAGTAG
TTGGTTGCTTCACCCCACCAGCTCCCGGTCGCGCTTAGCAACTGGGGGTCTTCCCCGCCT
GAGAAAGGTGGGTAAAGGTCTAGGGTTAAAATATAGTTCGTCATCAGTTTATTCGTAAAG
GAAATATA
"""
    
    dna = parse_fasta(sample_fasta)
    palindromes = find_reverse_palindromes(dna)
    palindromes.sort()
    
    print("Position Length")
    for pos, length in palindromes:
        print(f"{pos} {length}")