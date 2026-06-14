import os
def generate_lexv(alphabet, n, current_str, results):
    """
    Recursively generates all strings of length at most n from the given 
    ordered alphabet, naturally preserving lexicographical order.
    """
    if len(current_str) > 0:
        results.append(current_str)
        
    if len(current_str) == n:
        return
        
    for char in alphabet:
        generate_lexv(alphabet, n, current_str + char, results)

def solve_lexv(input_text):
    """
    Parses the alphabet and maximum length n from the input, then 
    generates and returns all lexicographically ordered strings.
    """
    lines = input_text.strip().split("\n")
    if len(lines) < 2:
        return []
        
    alphabet = lines[0].strip().split()
    n = int(lines[1].strip())
    
    results = []
    generate_lexv(alphabet, n, "", results)
    return results

def main():
    sample_input = """C V N H I U D G A M T
4"""
    output_path = os.path.join(os.path.dirname(sample_input), "chromosome_reconstruction_output.txt")
    
    ordered_strings = solve_lexv(sample_input)
    
    with open(output_path, "w") as out_file:
        out_file.write(ordered_strings + "\n")
    print(f"\nSuccess! Reconstructed chromosome of length {len(chromosome)} bp.")    
    print(f"Your accurate answer has been saved to:\n{output_path}")

if __name__ == "__main__":
    main()