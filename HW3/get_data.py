import yfinance as yf
import pandas as pd
import os
import json
import gzip

def get_five_core_data(directory):
    five_core = {}
    five_core_data = []
    
    # Iterate through the data in the given directory
    for subdir, dirs, files in os.walk(directory):

        # For each file, get the filename and extract the JSON
        for file in files:
            filename = str(os.path.join(subdir, file))
            # Use gzip to open the .gz and extract each line using the normal file package
            with gzip.open(filename, "rb") as f:
                for line in f:
                    line = line.decode(encoding='UTF-8')
                    json_data = json.loads(line)
                    five_core_data.append(json_data)
            # Add data to the dict
            five_core[filename] = five_core_data
           
    # Return the dict of complete ratings from each file
    return five_core

def get_ratings_data(directory):
    ratings = {}
    col_names = ['Item ID', 'User ID', 'Rating', 'Timestamp']
    
    # Iterate through the data in the given directory
    for subdir, dirs, files in os.walk(directory):

        # For each file, get the filename and extract the DF
        for file in files:
            filename = str(os.path.join(subdir, file))
            # Create a DF of the data and add it to the dict
            df = pd.read_csv(filename, names = col_names)
            ratings[filename] = df
           
    # Return the dict of complete ratings from each file
    return ratings

if __name__ == '__main__':

    AMZN = yf.download(tickers = 'AMZN', period = '10Y', interval = '1d')
    print(len(AMZN))

    five_core = get_five_core_data('../data/5-core/')
    print(len(five_core))

    ratings = get_ratings_data('../data/ratings')
    print(len(ratings))