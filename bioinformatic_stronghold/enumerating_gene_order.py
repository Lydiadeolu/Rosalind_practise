import itertools
import math

def generate_permutations(n:int):
    if not (1 <= n <= 7):
        return "Please provide an integer n between 1 and 7."
    
    elements = list(range(1, n + 1))
    
    total_count = math.factorial(n)
    
    all_perms = list(itertools.permutations(elements))
    
    return total_count, all_perms

def format_output(n:int):
    total, perms = generate_permutations(n)
    
    print(f"n = {n}")
    print(f"Total permutations: {total}")
    print("-" * 20)
    
    for p in perms:
        print(" ".join(map(str, p)))

if __name__ == "__main__":
    user_n = int(input('Input your integer'))
    format_output(user_n)