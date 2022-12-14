import analyze
import get_data
import make_visuals
import yfinance as yf

if __name__ == '__main__':

    # Data source
    five_core_directory = '../data/5-core/'
    ratings_directory = '../data/ratings'

    # AMZN data for analysis
    AMZN = yf.download(tickers = 'AMZN', start="2017-01-01", end="2018-01-01", interval = '1d')
    make_visuals.plot_timeseries(AMZN['Adj Close'], 'Time', 'Stock Price', 'AMZN Adjusted Closing Price', 'AMZN Adjusted Closing Price Over Time', '../result', 'AMZN.pdf')


    # Analyze data
    most_used_words = analyze.get_most_used_words(five_core_directory)
    print("Most used words:\n",most_used_words)
    least_used_words = analyze.get_least_used_words(five_core_directory)
    print("Least used words:\n",least_used_words)
    average_ratings = analyze.get_average_ratings(ratings_directory)
    print("Average ratings found for", len(average_ratings),"datasets.")

    # Use data to make/output visuals
    make_visuals.plot_words(most_used_words, '../result', 'most_used_words.pdf')
    make_visuals.plot_words(least_used_words, '../result', 'least_used_words.pdf')
    make_visuals.plot_all_timeseries(average_ratings, '../result')