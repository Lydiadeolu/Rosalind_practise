def calculate_protein_mass(protein_string:str):
    
    mass_table = {
        'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'L': 113.08406,
        'K': 128.09496,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'V': 99.06841,
        'W': 186.07931,
        'Y': 163.06333
    }

    total_mass = 0.0
    
    clean_string = "".join(protein_string.split())
    
    for aa in clean_string:
        if aa in mass_table:
            total_mass += mass_table[aa]
        else:
            print(f"Warning: Character {aa} is not a valid amino acid.")
            
    return round(total_mass, 3)

if __name__ == "__main__":
    target_protein = str(input(" Input string "))
    
    result = calculate_protein_mass(target_protein)
    print(f"Total Monoisotopic Mass: {result}")