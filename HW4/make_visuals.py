import matplotlib.pyplot as plt
import pandas as pd
import datetime
import yfinance as yf
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
import get_data

# Repository link:  https://github.com/medvidov/dsci510final

# Suppress warnings for chained assignment. It is faster than using replace()
pd.options.mode.chained_assignment = None 

# Returns the 10 most used words across all data
def get_most_used_words(directory):

    # Get the 5-core data for processing and get the keys (filenames)
    five_core = get_data.get_five_core_data(directory)
    five_core_keys = list(five_core.keys())

    # Counts of each word
    counts = {}
    
    # For each file
    for key in five_core_keys:

        # For each review in each file
        for i in range(len(five_core[key])):

            # Get the review text and there is review text
            review_text = five_core[key][i].get('reviewText')
            if review_text is not None:

                # Get every word in the review
                review_words = review_text.split()

                # For each word, make it lowercase and remove punctuation
                for word in review_words:
                    lower_word = re.sub(r'[^\w\s]', '', word.lower())

                    # Count the number of times that word appears
                    counts[lower_word] = counts.get(lower_word, 0) + 1

    # Sort the list by number of times a word appears
    counts_list = sorted(counts.items(), key=lambda x:x[1])
    
    # Return the 10 most used words
    return counts_list[-10:]

# Get the average rating across all data
def get_average_ratings(directory):

    # Get the ratings data and get the keys (filenames)
    ratings = get_data.get_ratings_data(directory)
    ratings_keys = list(ratings.keys())

    # Make a dict for average ratings
    all_average_ratings = {}
    
    # For each file
    for key in ratings_keys:
        
        # Get the dataframe associated with each category
        df = ratings[key]
        # Get the number of unique dates
        dates = df['Timestamp'].unique()

        # Prepare to calculate average ratings
        average_ratings = {}
        average_ratings["Date"] = []
        average_ratings["Average Rating"] = []
        
        # For each unique date
        for date in dates:

            # Get the ratings for that date and take their mean
            values = df.loc[df['Timestamp'] == date]
            average_rating = values['Rating'].mean()

            # Add the date and the average rating to the proper dictionary index
            average_ratings['Date'].append(date)
            average_ratings['Average Rating'].append(average_rating)
        
        # For that file, add the dicts to the average rating list
        all_average_ratings[key] = average_ratings
     
    # Convert each dict to a dataframe for later use/graphing
    for category in all_average_ratings:
        df = pd.DataFrame(data = all_average_ratings[category]['Average Rating'], columns = ['Average Rating'], index = all_average_ratings[category]['Date'])     
        all_average_ratings[category] = df

    # Return all average ratings
    return all_average_ratings

# Save a plot of the most used words in the specified file
def plot_most_used_words(words, savename):

    # Create two separate lists for the plt.pie data
    counts = []
    labels = []
    for i in range(len(words)):
        counts.append(words[i][1])
        labels.append(words[i][0])

    # Use the black magic that is plt to make the figure and save it
    plt.figure(figsize=(10, 10))
    plt.pie(counts, labels = labels)
    plt.legend()
    plt.savefig(savename)
    print("Saved", savename)

# Plot and save timeseries, very similar to the above code
def plot_timeseries(df, x, y, data_label, title, savename):
    plt.figure(figsize=(10, 10))
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.plot(df, label = data_label)
    plt.legend()
    plt.savefig(savename)
    print("Saved", savename)

# Plot all timeseries possible
def plot_all_timeseries(average_ratings):
    for key in average_ratings:
        plot_timeseries(average_ratings[key], 'Time', 'Average Rating', key + 'Average Ratings Over Time', key + 'Average Rating', key + '.pdf')

if __name__ == '__main__':

    AMZN = yf.download(tickers = 'AMZN', period = '10Y', interval = '1d')
    plot_timeseries(AMZN['Adj Close'], 'Time', 'Stock Price', 'AMZN Adjusted Closing Price', 'AMZN Adjusted Closing Price Over Time', 'AMZN.pdf')

    most_used_words = get_most_used_words('../data/5-core/')
    plot_most_used_words(most_used_words, 'words.pdf')

    # Please note: this takes a while to run due to the amount of data being processed
    average_ratings = get_average_ratings('../data/ratings')
    plot_all_timeseries(average_ratings)