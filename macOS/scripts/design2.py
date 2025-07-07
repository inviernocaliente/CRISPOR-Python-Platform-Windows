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


# def getInputs():
#     parser = argparse.ArgumentParser(
#         description="Organize guide CSV by #guideId, tss range, lowerbound, upperbound, mitSpecScore, Doench '16-Score, and offtargetCount."
#     )
#     parser.add_argument("csv_file", help="Path to input CSV file")
#     parser.add_argument(
#         "--tss", type=int, default=500,
#         help="TSS center value (default: 500)"
#     )
#     parser.add_argument(
#         "--lb", type=int, default=80,
#         help="lower bound in bp upstream of tss (default: 80)"
#     )
#     parser.add_argument(
#         "--ub", type=int, default=250,
#         help="upper bound in bp downstream of tss (default: 250)"
#     )
#     parser.add_argument(
#         "--mit", type=float, default=50.0,
#         help="Minimum mitSpecScore to keep (default: 50)"
#     )
#     parser.add_argument(
#         "--doench", type=float, default=60.0,
#         help="Minimum Doench '16-Score to keep (default: 60)"
#     )
#     parser.add_argument(
#         "--offtarget", type=int, default=100,
#         help="Maximum offtarget count to keep (default: 100)"
#     )
#     parser.add_argument(
#         "-o", "--output", dest="output_file",
#         help="Write final #guideId/targetSeq pairs to this CSV"
#     )
#     args = parser.parse_args()

#     return (args.csv_file, args.tss, args.lb, args.ub, args.mit, args.doench, args.offtarget)

# formatCSV(getInputs())
