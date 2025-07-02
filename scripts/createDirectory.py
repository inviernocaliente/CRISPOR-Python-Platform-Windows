import os
from datetime import datetime

def openDir(gene):
    # Set up download directory

    #get current time to include in file name   
    now_str = datetime.now().strftime("%Y-%m-%d_%Hh_%Mm_%Ss")
    dirName=str(gene)+"_sgRNA_search_"+now_str
    download_dir = os.path.abspath(dirName)
    os.makedirs(download_dir, exist_ok=True)
    return dirName, download_dir