import get_data
import analyze
import seaborn as sns
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

# Save a plot of the most used words in the specified file
def plot_words(words, directory, savename):

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
    plt.savefig(directory + '/' + savename)
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