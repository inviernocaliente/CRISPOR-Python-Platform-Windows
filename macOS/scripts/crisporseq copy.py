import py2bit
import requests

def download_2bit(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

def extract_sequence(twobit_file, chrom, start, end):
    tb = py2bit.TwoBitFile(twobit_file)
    seq = tb.get_sequence(chrom, start, end)
    tb.close()
    return seq

# Example usage
# Step 1: Download .2bit genome file (one-time)
url = "http://hgdownload.soe.ucsc.edu/goldenPath/mm9/bigZips/mm9.2bit"
twobit_filename = "mm9.2bit"
download_2bit(url, twobit_filename)

# Step 2: Extract region from mm9
chrom = "chr17"
start = 35642506
end = 35643506
sequence = extract_sequence(twobit_filename, chrom, start, end)

# Step 3: Output FASTA-style
print(f">mm9_{chrom}_{start}_{end}")
print(sequence)