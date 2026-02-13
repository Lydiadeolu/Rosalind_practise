def calculate_dominant_probability(k, m, n):
    
    total = k + m + n
    total_pairs = total * (total - 1)

    prob_nn = (n * (n - 1)) / total_pairs
    
    prob_nm = (n * m + m * n) / total_pairs * 0.5
    
    prob_mm = (m * (m - 1)) / total_pairs * 0.25
    
    
    prob_recessive = prob_nn + prob_nm + prob_mm
    
    prob_dominant = 1 - prob_recessive
    
    return prob_dominant

k_sample = int(input("what is the value of k? ")) 
m_sample = int(input("what is the value of m? "))
n_sample = int(input("what is the value of n? "))

# --- Execution ---
result = calculate_dominant_probability(k_sample, m_sample, n_sample)

print(f"Population: k={k_sample}, m={m_sample}, n={n_sample}")
print(f"Probability of dominant phenotype: {result:.5f}")