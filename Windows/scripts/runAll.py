import getFasta
import crispordnld
import sgRNA_design
import tssO2
import argparse
import createFasta
import createDirectory as cd

"""
Input: Gene Name, Genome Name, Genome Version, TSS center value, Lower Bound in bp upstream of TSS, 
Upper Bound in bp upstream of TSS, MIT Specificity Score, Doench '16 Score, and Off-Target Count

Output: Top sgRNA sequence candidates to use for given gene, under the given thresholds.
Output: Fasta file containing the top sgRNA sequence Candidates

"""

def getInputs():
    parser = argparse.ArgumentParser(
        description="Input gene name, genome name, genome version, tss range, lowerbound, upperbound, mitSpecScore, Doench '16-Score, and offtargetCount thresholds and obtain the top gRNA candidates. "
    )

    parser.add_argument("--geneName", type=str, help="name of the gene that we want to design gRNAs for")
    
    parser.add_argument(
        "--genomeName", type=str, default="Mus musculus - Mouse (reference) - UCSC Dec. 2011 (mm10=C57BL/6J) + SNPs: C57BL/10J, C57BR/cdJ",
        help="name of the genome to search in, using keywords on the dropdown menu"
    )

    parser.add_argument("--genomeVers", default="mm10", help="genome version title (default: mm10)")
    
    parser.add_argument(
        "--tss", type=int, default=500,
        help="TSS center value (default: 500)"
    )
    parser.add_argument(
        "--lb", type=int, default=80,
        help="lower bound in bp upstream of tss (default: 80)"
    )
    parser.add_argument(
        "--ub", type=int, default=250,
        help="upper bound in bp downstream of tss (default: 250)"
    )
    parser.add_argument(
        "--mit", type=float, default=50.0,
        help="Minimum mitSpecScore to keep (default: 50)"
    )
    parser.add_argument(
        "--doench", type=float, default=60.0,
        help="Minimum Doench '16-Score to keep (default: 60)"
    )
    parser.add_argument(
        "--offtarget", type=int, default=100,
        help="Maximum offtarget count to keep (default: 100)"
    )

    args = parser.parse_args()

    return (args.geneName, args.genomeName, args.genomeVers, args.tss, args.lb, args.ub, args.mit, args.doench, args.offtarget)

geneName, genomeName, genomeVers, tss, lb, ub, mit, doench, offtarget = getInputs()

#create new directory
direc, directory_path=cd.openDir(geneName)

chro, strand, tssStart=tssO2.get_gene_tss(geneName, genomeVers)
print(chro, strand, tssStart)
start=tssStart-500
end=tssStart+500
outFile=genomeVers+"_"+chro+"_"+str(start)+"_"+str(end)
getFasta.commandLine(genomeVers, chro, str(start), str(end), '../Data/' +direc+"/"+outFile+".fa")
# wsl ./twoBitToFa mm9.2bit stdout -seq=chr17 -start=35641798 -end=35648906 > mm9_chr17_35641798_35648906.fa
crispordnld.crisporDownload('../Data/'+direc+"/"+outFile+".fa", genomeName, '../Data/' +direc+"/"+outFile, directory_path)
datafield=sgRNA_design.formatCSV('../Data/' +direc+"/"+outFile+".csv", tss, lb, ub, mit, doench, offtarget)
outFasta=geneName+"_best_sgRNA.fa"
createFasta.write(datafield, '../Data/' +direc+"/"+outFasta)

