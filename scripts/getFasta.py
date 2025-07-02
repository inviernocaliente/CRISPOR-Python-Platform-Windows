import subprocess

"""
Operating System: Windows, need WSL with Ubunbu distribution
Inputs: Genome version, chromosome #, Start site, End site, and output file name
Runs command line prompt to extract the requested sequence from the genome file of the correct version as a Fasta File
"""

def commandLine(vers, chro, st, en, outpt):
    #must have wsl downloaded
    command='wsl ./twoBitToFa '+vers+".2bit stdout -seq=" + chro+ " -start="+st+" -end="+en+" > "+outpt
    subprocess.run(command, shell=True)
    return outpt
