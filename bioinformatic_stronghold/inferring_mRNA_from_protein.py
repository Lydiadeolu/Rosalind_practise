def solve_rna_combinations(protein_seq : str):
    codon_counts = {
        'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2,
        'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4,
        'A': 4, 'D': 2, 'E': 2, 'G': 4,
        'STOP': 3 
    }
    
    MOD = 1_000_000
    
    total_combinations = codon_counts['STOP']
    
    for amino_acid in protein_seq:
        total_combinations = (total_combinations * codon_counts[amino_acid]) % MOD
        
    return total_combinations

sample_input = str(input(" Input your string "))
result = solve_rna_combinations(sample_input)

print(f"Protein: {sample_input}")
print(f"Total RNA combinations (modulo 1,000,000): {result}")