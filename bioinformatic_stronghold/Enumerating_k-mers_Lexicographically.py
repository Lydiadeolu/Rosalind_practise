import itertools

def generate_lexicographical_strings(alphabet, n):
    perms = itertools.product(alphabet, repeat=n)
    
    result = ["".join(p) for p in perms]
    return result

if __name__ == "__main__":
    alphabet_input = "A B C D"
    n_input = 4
    
    alphabet = alphabet_input.split()
    
    ordered_strings = generate_lexicographical_strings(alphabet, n_input)
    
    for s in ordered_strings:
        print(s)