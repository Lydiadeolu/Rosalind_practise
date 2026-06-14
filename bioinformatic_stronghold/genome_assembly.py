import os

def parse_fasta_file(file_path):
    """Reads a local FASTA file and extracts the DNA strings."""
    reads = set()
    current_read = []
    
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_read:
                    reads.add("".join(current_read))
                    current_read = []
            else:
                current_read.append(line)
        if current_read:
            reads.add("".join(current_read))
            
    return list(reads)

def get_overlap(s1, s2):
    """Returns the length of the maximum suffix of s1 that matches a prefix of s2."""
    # Since the problem guarantees overlap > half length:
    min_overlap = max(len(s1), len(s2)) // 2 + 1
    
    for i in range(len(s1) - min_overlap + 1):
        suffix = s1[i:]
        if s2.startswith(suffix):
            return len(suffix)
    return 0

def reconstruct_chromosome(reads):
    """Safely merges pairs with the maximum overlap until one superstring remains."""
    while len(reads) > 1:
        max_overlap_len = 0
        best_pair = (None, None)
        
        # Check every pair to find the absolute highest overlap
        for i in range(len(reads)):
            for j in range(len(reads)):
                if i == j:
                    continue
                
                overlap = get_overlap(reads[i], reads[j])
                if overlap > max_overlap_len:
                    max_overlap_len = overlap
                    best_pair = (reads[i], reads[j])
        
        s1, s2 = best_pair
        
        # If no significant overlap is found (should not happen based on constraints)
        if s1 is None or s2 is None:
            break
            
        # Remove the two individual strings
        reads.remove(s1)
        reads.remove(s2)
        
        # Merge them and add the new superstring back into the pool
        merged_string = s1 + s2[max_overlap_len:]
        reads.append(merged_string)
        
    return reads[0]

def main():
    input_path = r"C:\Users\adeolu\Downloads\rosalind_long (5).txt"
    output_path = os.path.join(os.path.dirname(input_path), "chromosome_reconstruction_output.txt")
    
    if not os.path.exists(input_path):
        print(f"Error: Could not find the file at {input_path}")
        return

    print("Reading FASTA dataset...")
    dna_reads = parse_fasta_file(input_path)
    print(f"Loaded {len(dna_reads)} unique DNA sequences.")
    
    print("Reassembling chromosome accurately...")
    chromosome = reconstruct_chromosome(dna_reads)
    
    # Save output
    with open(output_path, "w") as out_file:
        out_file.write(chromosome + "\n")
        
    print(f"\nSuccess! Reconstructed chromosome of length {len(chromosome)} bp.")
    print(f"Your accurate answer has been saved to:\n{output_path}")

if __name__ == "__main__":
    main()