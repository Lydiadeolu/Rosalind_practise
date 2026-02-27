import urllib.request
import re

def get_protein_sequence(access_id: str) -> str:
    # Use the base ID for the URL (the part before the underscore if applicable)
    base_id = access_id.split('_')[0]
    url = f"https://www.uniprot.org/uniprot/{base_id}.fasta"
    
    try:
        with urllib.request.urlopen(url) as response:
            fasta_data = response.read().decode('utf-8')
            lines = fasta_data.strip().split('\n')
            sequence = "".join(lines[1:])
            return sequence
    except Exception as e:
        return ""

def find_n_glycosylation_motif(access_ids: list[str]):
    motif_regex = r'(?=(N[^P][ST][^P]))'
    
    for access_id in access_ids:
        sequence = get_protein_sequence(access_id)
        if not sequence:
            continue
            
        locations = []
        for match in re.finditer(motif_regex, sequence):
            locations.append(match.start() + 1)
            
        if locations:
            print(access_id)
            print(" ".join(map(str, locations)))

sample_access_ids = [
   "Q640N1",
   "P01374_TNFB_HUMAN",
   "P31096_OSTP_BOVIN",
   "P22891_PRTZ_HUMAN",
   "Q78PG9",
   "P07204_TRBM_HUMAN",
   "P80069_A45K_MYCBO",
   "Q5U1Y9",
   "P01189_COLI_HUMAN",
   "Q9CE42",
   "P11831_SRF_HUMAN",
   "Q5FTZ8",
   "O29347",
   "P72173"

]

if __name__ == "__main__":
    print("--- N-glycosylation Motif Locations ---")
    find_n_glycosylation_motif(sample_access_ids)

