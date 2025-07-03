import os
from datetime import datetime

def openDir(gene):
    # Set up download directory

    #get current time to include in file name   
    now_str = datetime.now().strftime("%Y-%m-%d_%Hh_%Mm_%Ss")
    current_dir=os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    target_path=os.path.join(parent_dir, 'Data')
    dirName=str(gene)+"_sgRNA_search_"+now_str
    os.makedirs("../Data/"+dirName, exist_ok=True)
    
    return dirName, target_path