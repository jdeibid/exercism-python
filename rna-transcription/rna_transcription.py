def to_rna(dna_strand):
    # Check if parameter is empty.
    if dna_strand == "":
        return dna_strand
    result = str()
    # Loop through each nucleotide.
    for neuclotide in dna_strand:
        if neuclotide == "G":
            result += "C"
        if neuclotide == "C":
            result += "G"
        if neuclotide == "T":
            result += "A"
        if neuclotide == "A":
            result += "U"
    return result