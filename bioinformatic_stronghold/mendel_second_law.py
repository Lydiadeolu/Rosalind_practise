from math import comb

def calculate_independent_alleles(k: int, n: int) -> float:
    total_population = 2**k
    
    p = 0.25  
    q = 0.75 
    
    prob_at_least_n = 0
    
    for i in range(n, total_population + 1):
        probability_i = comb(total_population, i) * (p**i) * (q**(total_population - i))
        prob_at_least_n += probability_i
        
    return round(prob_at_least_n, 3)

k_sample = int(input("what is the value of k? "))
n_sample = int(input ("what is the value of n? "))

result = calculate_independent_alleles(k_sample, n_sample)

print(f"Generation (k): {k_sample}")
print(f"Target count (N): {n_sample}")
print(f"Probability of at least {n_sample} AaBb: {result}")
