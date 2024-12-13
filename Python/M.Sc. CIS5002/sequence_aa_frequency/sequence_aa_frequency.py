# Display the amino acid frequencies in a specified FASTA file

'''
Task Description:
For each sequence in the supplied FASTA file, show a histogram of the amino
acid frequency. This histogram should look something like:

Sequence_Header_1
A 10 **********
C 5 *****
D 11 ***********
<...>
Sequence_Header_2
A 1 *
C 7 *******
D 3 ***
<...>

Once done, rotate the above ASCII histogram graph so that the * bars are shown
vertically. Which are the most and least popular amino-
'''

filename = "pfalciparum.fasta"

# Handle scenarios where specified files are not of .fasta extension
if not filename.lower().endswith(".fasta"):
    print("\nError: Please specify a file of FASTA format.\n")

else:
    try:
        with open(filename) as file:

            # Store the letter representation of every amino acid
            amino_acids = "ACDEFGHIKLMNPQRSTVWY"

            # Initialise a dictionary in which to store amino acid frequencies 
            # for each sequence
            aa_freq = {}

            for line in file:

                # Identify a sequence header by the ">" character
                if ">" in line:
                    # Extract header name
                    seq_head = line[1:].strip()

                    # Initialise an inner dictionary of frequencies for the 
                    # present sequence
                    aa_freq[seq_head] = {amino_acid: 0
                                         for amino_acid in amino_acids}

                else:
                    # Count the occurrence of each amino acid in the sequence
                    for aa in line.strip():
                        aa_freq[seq_head][aa] += 1

        print()
        # Print a representation of amino acid frequencies for each sequence
        for seq_head, inner_dict in aa_freq.items():
            print(seq_head)
            for aa, freq in inner_dict.items():
                # Print amino acid name, frequency, and a corresponding 
                # histogram representation with '*' characters
                print(f"{aa}\t{freq}\t{"*" * freq}")
            print()

        print()
        # Print a vertical histogram of amino acid frequencies for each sequence
        for seq_head, inner_dict in aa_freq.items():
            # Determine the maximum frequency observed for reference
            max_freq = max(inner_dict.values())
            
            print(seq_head)

            # Print the histogram rows from top (max frequency) to bottom
            for y in range(max_freq, 0, -1):
                for aa in inner_dict:
                    # Print '*' according to position in the plot and amino acid 
                    # frequency
                    if inner_dict[aa] < y:
                        print(" ", end=" " * 3)
                    else:
                        print("*", end=" " * 3)
                print()

            # Print the numerical frequencies below the histogram
            for aa in inner_dict:
                print(f"{inner_dict[aa]:02}", end=" " * 2)
            print()

            # Print the amino acid labels below the frequencies
            for aa in inner_dict:
                print(aa, end=" " * 3)
            print("\n")

        # Initialise a new dictionary in which to store normalised amino acid 
        # frequencies across all sequences
        aa_freq_comp = {amino_acid: 0 for amino_acid in amino_acids}

        for seq_head, inner_dict in aa_freq.items():
            
            # Calculate the length of each sequence
            seq_length = sum(inner_dict.values())
            for aa in inner_dict:
                # Accumulate normalised frequencies for each sequence
                aa_freq_comp[aa] += inner_dict[aa] / seq_length

        # Divide cumulative frequencies by the number of sequences
        seq_count = len(aa_freq)
        for aa in aa_freq_comp:
            aa_freq_comp[aa] /= seq_count

        # Sort amino acids in descending order of their normalised frequencies 
        sorted_aa_freq_comp = sorted(aa_freq_comp.items(), 
                                     key=lambda item:item[1],
                                     reverse=True)

        # Print the sorted normalised frequencies
        for aa, freq in sorted_aa_freq_comp:
            print(f"{aa}: {freq:.3f}")
        print()

    # Handle scenarios where specified files cannot be located
    except FileNotFoundError:
        print("\nError: Please specify an existing FASTA file.\n")