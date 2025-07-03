import pandas as pd
def write(df, output):

    # sequences = df.iloc[:, 2]  # 3rd column
    # location = df.iloc[:, 0]        # Assume first column is guide ID

    # Optional: add chromosome/start/end info to headers
    fasta_lines = []
    for idx, row in df.iterrows():
        loc       = str(row.iloc[0])  # first column
        dir = str(row.iloc[1])  # second column
        sequences  = str(row.iloc[2])  # third column

        header = f">{loc}{dir}" 
        fasta_lines.append(str(header))
        fasta_lines.append(sequences)

    # Save to FASTA file
    with open(output, "w") as fasta_file:
        fasta_file.write("\n".join(fasta_lines))
