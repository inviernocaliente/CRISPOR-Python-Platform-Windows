import argparse
import pandas as pd

def formatCSV(csv_file, tss_value, lower_bound, upper_bound, mit, doench, offtc):
    # csv_file, tss_value, lower_bound, upper_bound, mit, doench, offtc=inputTuple
    #format csv file
    datafield=pd.read_csv(csv_file, header=None)
    header_rows = datafield.apply(lambda row: "#guideId" in row.values, axis=1)
    guideId_index = header_rows.idxmax()
    # meta = pd.read_csv(csv_file, header=None, nrows=8)            # rows 1–7: metadata
    df   = pd.read_csv(csv_file, skiprows=guideId_index)  
    # print(df)
    newdf=df[['#guideId','targetSeq', 'mitSpecScore', 'offtargetCount', "Doench '16-Score"]].copy()
    newdf[['location', 'direction']] = newdf['#guideId'].str.extract(r'(\d{3})([a-zA-Z]{3,4})')
    # print(newdf)
    # Convert 'Number' to int type
    newdf['location'] = pd.to_numeric(newdf['location']).astype('Int64')
    newdf=newdf[['location', 'direction','targetSeq', 'mitSpecScore', 'offtargetCount', "Doench '16-Score"]]
    #print(newdf)

    # Define tss window
    lower = tss_value - lower_bound
    upper = tss_value + upper_bound
    newdf = newdf[(newdf['location'] >= lower) & (newdf['location'] <= upper)]

    #Ensure numeric sorting on #guideId
    newdf = newdf.sort_values(by='location', ascending=True)

    # Filter by mitSpecScore threshold
    newdf = newdf[newdf['mitSpecScore'] >= mit]

    # Filter by Doench '16-Score threshold
#     Note: Column name includes an apostrophe
    newdf = newdf[newdf["Doench '16-Score"] >= doench]

#     # Sort by offtargetCount
    newdf = newdf[newdf["offtargetCount"] <= offtc]


    #reset index from 1 to whatever
    newdf = newdf.reset_index(drop=True)

    print(newdf)
    return newdf