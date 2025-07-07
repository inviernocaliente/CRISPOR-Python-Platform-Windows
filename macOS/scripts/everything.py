import getFasta
import crispordnld
import xlsTocsv
import design2
import tssO2
import argparse
from pathlib import Path

def getInputs():
    parser = argparse.ArgumentParser(
        description="Design gRNAs for a gene based on TSS location and score filters."
    )

    parser.add_argument("--geneName", type=str, required=True,
                        help="Name of the gene to design gRNAs for")

    parser.add_argument("--genomeName", type=str, default="Mus musculus - Mouse (reference) - UCSC Dec. 2011 (mm10=C57BL/6J) + SNPs: C57BL/10J, C57BR/cdJ",
                        help="Genome label for CRISPOR (must match CRISPOR dropdown options)")

    parser.add_argument("--genomeVers", default="mm10", help="Genome version title (e.g., mm10 or mm9)")

    parser.add_argument("--tss", type=int, default=500, help="TSS center value (default: 500)")
    parser.add_argument("--lb", type=int, default=80, help="Lower bound upstream of TSS")
    parser.add_argument("--ub", type=int, default=250, help="Upper bound downstream of TSS")

    parser.add_argument("--mit", type=float, default=50.0, help="Minimum MIT specificity score")
    parser.add_argument("--doench", type=float, default=60.0, help="Minimum Doench 2016 score")
    parser.add_argument("--offtarget", type=int, default=100, help="Maximum allowed off-target count")

    args = parser.parse_args()
    return (args.geneName, args.genomeName, args.genomeVers,
            args.tss, args.lb, args.ub, args.mit, args.doench, args.offtarget)

# === Main Program ===

geneName, genomeName, genomeVers, tss, lb, ub, mit, doench, offtarget = getInputs()

# Step 1: Get TSS info
chro, strand, tssStart = tssO2.get_gene_tss(geneName, genomeVers)
print(f"🧬 Gene {geneName} found at: {chro} {strand} {tssStart}")

# Step 2: Define target region around TSS
start = tssStart - 500
end = tssStart + 500
outFile = f"{genomeVers}_{chro}_{start}_{end}"

# Step 3: Extract FASTA
getFasta.commandLine(genomeVers, chro, str(start), str(end), outFile + ".fa")

# Step 4: Run CRISPOR to download .xls to download directory
crispordnld.crisporDownload(outFile + ".fa", genomeName, outFile)

# Step 5: Get latest downloaded .xls file
download_dir = Path.home() / "Desktop" / "crispor_downloads"

def get_latest_xls(download_dir):
    xls_files = sorted(download_dir.glob("*.xls"), key=lambda f: f.stat().st_mtime, reverse=True)
    if not xls_files:
        raise FileNotFoundError(f"No .xls files found in {download_dir}")
    return xls_files[0]

xls_path = get_latest_xls(download_dir)
print(f"✅ Using downloaded XLS: {xls_path}")

# Step 6: Convert .xls → .csv
csv_path = Path(outFile + ".csv")
xlsTocsv.convert(str(xls_path), str(csv_path))

# Step 7: Filter for top guides
design2.formatCSV(str(csv_path), tss, lb, ub, mit, doench, offtarget)
