def calculate_expected_dominant_offspring(counts):
    
    probabilities = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    
    expected_value = 0
    
    offspring_per_couple = 2
    
    for i in range(len(counts)):
        expected_value += counts[i] * offspring_per_couple * probabilities[i]
        
    return expected_value


sample_counts = [17448, 17297, 16462, 17678, 17179, 18531]

result = calculate_expected_dominant_offspring(sample_counts)

print(f"Genotype Pairing Counts: {sample_counts}")
print(f"Expected number of dominant offspring: {result}") 
