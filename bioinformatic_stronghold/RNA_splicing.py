def translate_dna(dna):
    dna_codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    
    protein = ""
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if len(codon) < 3:
            break
        amino_acid = dna_codon_table.get(codon, "")
        if amino_acid == "_": 
            break
        protein += amino_acid
    return protein

def splice_and_translate(fasta_data):
    entries = [entry.strip() for entry in fasta_data.split('>') if entry.strip()]
    
    sequences = []
    for entry in entries:
        lines = entry.split('\n')
        seq = "".join(lines[1:])
        sequences.append(seq)
        
    main_dna = sequences[0]
    introns = sequences[1:]
    
    for intron in introns:
        main_dna = main_dna.replace(intron, "")
        
    return translate_dna(main_dna)

if __name__ == "__main__":
    sample_data = """>Rosalind_2834
ATGATCGGTTATTCGTCAGCCTGGTCATACGAACAGTATCTGGTGAGTTGCTATCGTTGG
TAGTGACCAGGGTTTATAGTCACCTTTGTATGGCTCGCAATCAGAAAGTTATGCGTGCCG
CGGTGTACTGCCTCGAATCTCCCGCAAATCGTCGAAATAATCACGTTTGGCCACCATGAG
CTGCTAACCGTATTGGTCACGGCGATACTCATTCGATCCCGGTTACATACAGAGCGACCG
GGAGTTGCAGGGGGTGTACTATCTCACAGACGGCACCCTACCCGAGACCCGTTCCCCGCA
GTTGGCACTGGGACCAGCCACACTGGCGAACGTGGCATTGTCCGTTAAGAGTTCCCACAA
CACCTCCTCTTCCGCGATCGCCAGATGGTTACGTGACGCGGTTGGCTCAAAGGCGACTCA
GCTTCGGGAAAGCCCCTTCAGGACCCGCCAGCCACGTTGTCGGGACGTCTTAGGACTGGT
AACTTAGTGAACCGGAAGTATCCCCTTCTGGAGTTAAGGTCTGAATCACCGGATCAGTCG
CATCCCCTCAGTATGTACTTCTTACGAATTCCCACAACCAGTGCGATACTCAGGCTGAGG
GTATTCTATTGTTGGCGCAGAACCCTACTTGGTTAGGGGCGATGGCAACCAGTTACTTAA
GGAGACGGTCGAATAACTTCGAATCCGCATCACACAATCTGCCGAGTCGTTAACTCGAAT
CATCATCTGCTATTAAAGCGGGGCTACCGTCCTAAAGTAGTAAGGACCGAGCCCGCGCCG
CGCGACAGGATAAGAGCACAATGCAAAAGATCGTATGGCTTAACTATGGACTACATCTCT
TGAAAGAAGTCCGTCCGGTAGATCCACAGGAGGAGAGATCAATGCCGAACTGGGCTCCGT
AACGGCCCCCTGCACAGTAAGGAGGTGTCTACTCGGCGACGTTCCGTAA
>Rosalind_5891
TGGTAGTGACCAGGGTTTATAGTCACC
>Rosalind_8631
TTACGTGACGCGGTTGGCTCAAAGGCGACTCAGCTTCGGGAAAG
>Rosalind_6363
ATGCCGAACTG
>Rosalind_5237
CTCCCGCAAATCGTCGAAATAATCACGTTTGGCCACCATGA
>Rosalind_5423
CTACATCTCTTG
>Rosalind_5910
CGTCTTAGGACTGGTAACTTAGT
>Rosalind_7016
ACCGGGAGTTGCAGGGGGTGTACTATCTCACAGACGGCACCCTAC
>Rosalind_0734
TGTCCGTTAAGAGTTCCCAC
>Rosalind_3713
TGAATCACCGGATCAG
>Rosalind_5750
CCCGCGCCGCGCGACAGGATAAGAGCACAATGCAA
>Rosalind_3784
ACCAGTGCGATACTCAGGCTGAGGGTATTCTATTGTTGGCGCAGAACCCT
>Rosalind_3322
GAATCCGCATCACACAATCTGCCGAGTCGTTAAC
"""

    protein_result = splice_and_translate(sample_data)
    print(f"Resulting Protein: {protein_result}")