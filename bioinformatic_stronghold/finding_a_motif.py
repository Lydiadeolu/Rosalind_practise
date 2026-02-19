def find_motif_locations(s: str, t: str):
    locations = []
    
    for i in range(len(s) - len(t) + 1):
        if s[i : i + len(t)] == t:
            locations.append(i + 1)
            
    return locations

s_sample = str(input("What is the dataset for s? "))
t_sample = str(input("What is the dataset for t? "))

results = find_motif_locations(s_sample, t_sample)

print("--- Motif Search Results ---")
print(f"Main String: {s_sample}")
print(f"Motif:       {t_sample}")
print(f"Locations:   {' '.join(map(str, results))}")

