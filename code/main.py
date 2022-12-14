import analyze
import get_data
import make_visuals
import yfinance as yf

# Repository link:  https://github.com/medvidov/dsci510final

if __name__ == '__main__':

    # Data source
    five_core_directory = 'data/5-core/'
    ratings_directory = 'data/ratings'
    results = 'result'

    print('NOTE: This code will take a while to run due to the amount of data being processed.\n')

    # AMZN data for analysis
    AMZN = yf.download(tickers = 'AMZN', start="2014-01-01", end="2018-01-01", interval = '1d')
    make_visuals.plot_timeseries(AMZN['Adj Close'], 'Time', 'Stock Price', 'AMZN Adjusted Closing Price', 'AMZN Adjusted Closing Price Over Time', 'result', 'AMZN.pdf')


    # Analyze data
    most_used_words = analyze.get_most_used_words(five_core_directory)
    print("Most used words:\n",most_used_words)
    least_used_words = analyze.get_least_used_words(five_core_directory)
    print("Least used words:\n",least_used_words)
    average_ratings = analyze.get_average_ratings(ratings_directory)
    print("Average ratings found for", len(average_ratings),"datasets.")

    # Use data to make/output visuals
    make_visuals.plot_words(most_used_words, 'Most Used Words', results, 'most_used_words.pdf')
    make_visuals.plot_words(least_used_words, 'Least Used Words', results, 'least_used_words.pdf')
    make_visuals.plot_all_timeseries(average_ratings, results)
    make_visuals.plot_all_scatterplots(average_ratings, results)