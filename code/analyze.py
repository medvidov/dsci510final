import get_data
import pandas as pd
import re

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

        file = get_data.get_filename(key)
        print(file)

        # For each review in each file
        for i in range(len(five_core[file])):

            # Get the review text and there is review text
            review_text = five_core[file][i].get('reviewText')
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

# Returns the 10 least used words across all data, almost identical to get_most_used_words++
def get_least_used_words(directory):

    # Get the 5-core data for processing and get the keys (filenames)
    five_core = get_data.get_five_core_data(directory)
    five_core_keys = list(five_core.keys())

    # Counts of each word
    counts = {}
    
    # For each file
    for key in five_core_keys:

        file = get_data.get_filename(key)

        # For each review in each file
        for i in range(len(five_core[file])):

            # Get the review text and there is review text
            review_text = five_core[file][i].get('reviewText')
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
    
    # Return the 10 least used words
    return counts_list[:10]

# Get the average rating across all data
def get_average_ratings(directory):

    # Get the ratings data and get the keys (filenames)
    ratings = get_data.get_ratings_data(directory)
    ratings_keys = list(ratings.keys())

    # Make a dict for average ratings
    all_average_ratings = {}
    
    # For each file
    for key in ratings_keys:

        file = get_data.get_filename(key)
        
        # Get the dataframe associated with each category
        df = ratings[file]
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
        all_average_ratings[file] = average_ratings
     
    # Convert each dict to a dataframe for later use/graphing
    for category in all_average_ratings:
        df = pd.DataFrame(data = all_average_ratings[category]['Average Rating'], columns = ['Average Rating'], index = all_average_ratings[category]['Date'])     
        all_average_ratings[category] = df

    # Return all average ratings
    return all_average_ratings