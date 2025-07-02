import os
import time
import pandas as pd

def get_latest_download(download_directory):
    time.sleep(3)
    files = [f for f in os.listdir(download_directory) 
             if not f.startswith('.') and not f.endswith('.download')]
    paths = [os.path.join(download_directory, f) for f in files]
    return max(paths, key=os.path.getmtime)

def convert(download_dir, output_basename):
    latest_file = get_latest_download(download_dir)
    print(f"📄 Latest file detected: {latest_file}")

    try:
        if latest_file.endswith('.xls'):
            df = pd.read_excel(latest_file, engine='xlrd')
        elif latest_file.endswith('.xlsx'):
            df = pd.read_excel(latest_file, engine='openpyxl')
        else:
            raise ValueError("File is not .xls or .xlsx")

        output_path = output_basename + ".csv"
        df.to_csv(output_path, index=False)
        print(f"✅ Saved as CSV: {output_path}")
    except Exception as e:
        print(f"❌ Error: {e}")