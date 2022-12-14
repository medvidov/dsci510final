import matplotlib.pyplot as plt

# Repository link:  https://github.com/medvidov/dsci510final

# Save a plot of analyzed words in the specified file
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
    print("Saved", directory + '/' + savename)

# Plot and save timeseries, very similar to the above code
def plot_timeseries(df, x, y, data_label, title, directory, savename):
    plt.figure(figsize=(10, 10))
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.plot(df, label = data_label)
    plt.legend()
    plt.savefig(directory + '/' + savename)
    print("Saved", directory + '/' + savename)

# Plot all timeseries possible
def plot_all_timeseries(average_ratings, directory):
    for key in average_ratings:
        plot_timeseries(average_ratings[key], 'Time', 'Average Rating', key + 'Average Ratings Over Time', key + 'Average Rating', directory, key + '_timeseries.pdf')

# Plot and save scatterplots, very similar to the above code
def plot_scatterplot(df, x, y, title, directory, savename):
    plt.figure(figsize=(10, 10))
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.scatter(x = df.index, y = df)
    plt.savefig(directory + '/' + savename)
    print("Saved", directory + '/' + savename)

# Plot all scatterplots possible
def plot_all_scatterplots(average_ratings, directory):
    for key in average_ratings:
        plot_scatterplot(average_ratings[key], 'Time', 'Average Rating', key + 'Average Ratings Over Time', directory, key + '_scatterplot.pdf')
