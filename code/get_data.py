import yfinance as yf
import pandas as pd
import os
import json
import gzip
import datetime

# Repository link:  https://github.com/medvidov/dsci510final

def get_filename(file):
    
    # Remove any reference of directory structures in the file
    filename = file.split('/')[-1]
    
    # Remove the extension
    filename = filename.split('.')[0]
    
    # If I'm using a 5-core data file, remove the _5 that denotes that it is a 5-core
    if '_5' in filename:
        filename = filename.split('_5')[0]
                
    return filename

def get_five_core_data(directory):
    five_core = {}
    
    # Iterate through the data in the given directory
    for subdir, dirs, files in os.walk(directory):

        # For each file, get the filename and extract the JSON
        for file in files:
            filename = str(os.path.join(subdir, file))
            five_core_data = []
            # Use gzip to open the .gz and extract each line using the normal file package
            with gzip.open(filename, "rb") as f:
                for line in f:
                    line = line.decode(encoding='UTF-8')
                    json_data = json.loads(line)
                    five_core_data.append(json_data)
            # Add data to the dict
            five_core[get_filename(filename)] = five_core_data
           
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

            # Convert Timestamp into dates
            times = df['Timestamp']
            for i in range(len(times)):
                times[i] = datetime.datetime.fromtimestamp(times[i]).date()
            df = df.drop(labels = 'Timestamp', axis = 1)
            df = pd.concat([df,times], axis = 1)

            # Sort the dataframe by the dates
            df = df.sort_values('Timestamp')
            ratings[get_filename(filename)] = df
           
    # Return the dict of complete ratings from each file
    return ratings

if __name__ == '__main__':

    five_core = get_five_core_data('../data/5-core')
    print(len(five_core))

    ratings = get_ratings_data('../data/ratings')
    print(len(ratings))