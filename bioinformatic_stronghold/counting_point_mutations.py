def calculating_hamming_distance(s, t):
    if len(s) != len(t):
        raise ValueError("Strings length must be equal")
    distance = 0
    for char_s, char_t in zip(s, t):
        if char_s != char_t:
            distance += 1
    return distance
s_sample = str(input("what is the first string? "))
t_sample = str(input("what is the second string? "))

result = calculating_hamming_distance(s_sample, t_sample)

print(f" String s: {s_sample}")
print(f"String t: {t_sample}")
print(f"Hamming Distance: {result}")