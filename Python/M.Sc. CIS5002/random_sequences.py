# Generate a FASTA file of 10 random sequences

'''
Task Description:
Write a program which generates 10 random sequences and saves them to a
file. This is sometimes useful when building null models to find over or under
represented amino acid residues. Each sequence should contain valid amino
acid identifiers and should be of random length between 10 and 2000. The
header can be a constant prefix (e.g. seq_) with a sequence counter, so the
first header line will be >seq_0 etc.
'''

output_name = "random_10.fasta"

with open(output_name, "w") as output_file:

    import random

    # Store the letter representation of every standard amino acid
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"

    # Iterate over each sequence 1-10
    for seq_num in range(1,11):

        # Write the sequence header
        output_file.write(f">seq_{seq_num}")

        # Initilaise a character counter
        char_count = 0

        # Generate a random sequence length between 10-2000 characters
        seq_length = random.randint(10,2000)

        # Iterate over every character in the length of the sequence
        for char in range(seq_length):

            # Write a new line every 80 characters
            if char_count % 80 == 0:
                output_file.write("\n")         

            # Write any random letter representing a standard amino acid        
            output_file.write(random.choice(amino_acids))

            # Increment the character counter 
            char_count += 1

        # Write a fresh line after every sequence but the last
        if seq_num != 10:
            output_file.write("\n")                   

# Direct the user to the location of the outputted FASTA file
print(f"\n10 random sequences have been written to {output_name}.\n")