# Comparing Amazon Product Ratings against Amazon Stock Price
## Repository link:  [https://github.com/medvidov/dsci510final](https://github.com/medvidov/dsci510final)

This project uses the [Amazon Review Data](https://nijianmo.github.io/amazon/index.html) to analyze the correlation between Amazon product ratings and Amazon stock prices.
The 5-cores data is used to determine the most commonly used words across reviews. The ratings data is used to produce line and scatter plots to aid in understanding
the relationship between Amazon product ratings and Amazon stock price.

# Citation
Justifying recommendations using distantly-labeled reviews and fined-grained aspects

Jianmo Ni, Jiacheng Li, Julian McAuley

Empirical Methods in Natural Language Processing (EMNLP), 2019

# Dependencies

- yfinance >= 0.1.86
- pandas >= 1.4.2
- matplotlib >= 3.5.1

To install this project's dependencies, run
```
pip install -r requirements.txt
```

# Running the project

To run the project, ensure you have the following directory structure. Other folders used for previous HW assignments are present in this repository but will not impact running the code.

```
.
|   README.md
|   requirements.txt
|   .gitignore
|
└───code
|   |   main.py
|   |   get_data.py
|   |   analyze.py
|   |   make_visuals.py
|
└───data
|   └───5-core
|       |   ...
|   └───ratings
|       |   ...
|
└───result
|   |   ...
|
|   ...

```

The contents of `data` and `result` will depend on which datasets you have downloaded. For the purposes of this demonstration I have provided the `Appliances` and `Magazine Subscriptions` datasets. Once you have verified that you have the proper directory structure, run
```
python code/main.py
```
Please note that you are running this command in the top level directory. If you run this command in `code` you will get errors.

# Data

I downloaded the Amazon Review Data k-cores data, the Amazon Review Data complete ratings data and used [yfinance](https://pypi.org/project/yfinance/) to access Amazon’s historical stock data. The Amazon Review Data k-cores data contains minimized datasets of complete reviews for sparse sets of
items in various categories. This is stored in a JSON format. The complete ratings data contains CSVs with user IDs, item IDs, the user’s item rating, and the timestamp of
when that item was bought. Amazon’s historical stock data from yfinance is a dataset that can include information on opening, closing, and adjusted closing prices (among
other things). From the Amazon Review Data I collected a few million data points, but I could not use all of them due to the constraints of my available computing power.
For the historical stock data, I collected about 1000 rows of data corresponding to various Amazon stock metrics. These rows encompass the years 2014 to 2018, which is the
same timeframe as the Amazon Review Data (per the description). The biggest change from my original plan was that I literally could not use all of the available data (I
intended to try). As a result I used a subset of the data to perform my analysis while writing modular code to be able to extend my analysis to additional data.


# Methodology

The bulk of my analyses focused on processing the data to be able to see trends in the data.
The corresponding visualizations were charts made using `pyplot` to effectively communicate the data.
On the whole, my methodology for this project remained the same as I had planned it with two exceptions. First, it was not feasible to plot or perform linear regression
on the ratings data versus the stock price. I adapted by creating separate graphs which can be viewed together to achieve a similar result to my intended analysis.
The more problematic change to my methodology was that reading the line graphs of average rating over time was almost impossible. I made scatterplots to supplement the
line graphs so as to illustrate the trends in average rating over time.

## Analyses

### Least and most used words

Because the words in an Amazon review are a useful indicator of a person's feelings in that review even without a rating, I decided to determine the most and least
used words in the 5-cores data. This proved to be less useful than anticipated because words such as "this" and "it" were commonly used and I did not have an
effective way to filter prepositions and the like. Notably the least used words were all used only once (1 time) each. They may also have been typos, which would require
further filtering.

### Average rating per day

Because my initial vision of this project involved a comparison of Amazon rating data and Amazon stock price, I found the average rating given per day for the ratings data.
Because some days had fewer ratings than others, this resulted in skewed data. Additionally, the relatively small number of possible values for an average rating meant that
this data was hard to graph effectively.

## Visualizations

### Pie charts

To effectively communicate the most and least used words, I used matplotlib to create and save pie charts of the 10 least and most used words. I found that this was easy to
read and provided an idea of how much given words were used relative to others. As noted previously, the words found were not the most useful data due to my inability to 
filter prepositions and the like. The least used words were all used once (1 time) each. Each slice of the pie represented a word with a size proportional to the relative use of that word in the most or least used words list. Each slice was also individually color coded.

![Least used words pie chart](/assets/pie.png)

### Line graphs

Line graphs are the easiest way to communicate changes in stock values over time. Because of my initial intent for this project, I also created line plots of average rating
over time. However, this was harder to read than I would have liked. In the case of the line graphs, the x-axis represents time and the y-axis represents the numerical
variable (either average rating or stock price).

![Average rating line graph](/assets/line.png)

### Scatterplots

To compensate for the difficulty of reading line graphs for average rating, I instead made scatterplots of the average rating of products over time. While still dense,
these were easier to read and communicated the data more clearly. As with the line graphs, the x-axis represents time and the y-axis represents the average rating of products
on that day.

![Average rating scatterplot](/assets/scatter.png)

### Interactive line graphs

In `Bonus.ipynb` I have included code for interactive line graphs to help users understand the relationship between stock price and average rating.
Due to the sheer density information of the average rating graphs, they are slightly hard to use, but this code provides a useful proof of concept for comparing such data.
Additionally, the average rating graph becomes much more accessible to the user, even if it is still not perfect. This code was different than anticipated because I initially
had a much more ambitious plan where the stock price would be overlayed with the ratings data. Ultimately my computer could not process all the data so I opted for a simpler
approach. To run this code, simply run the Jupyter notebook.

# Future Work

In the future I would like to use the 5-cores data for its intended purpose and perform sentiment analysis on this new Amazon reviews.
Unfortunately, for the scope of this project it was not feasible to label the necessary data to actually perform sentiment analysis.
That said, given more time and more resources, further exploring natural language processing would benefit my career and deepen my data science skillset.
In terms of changes that are more related to the project as is, I would also like to create plots showing AMZN stock price against average product rating over time. 
Given the different scales of the numerical data in these two datasets, I was not able to superimpose the graphs to show the relationship between rating and stock price.
I am uncertain that such a visualization would be terribly useful, but this was part of my original vision for this project.
I think this project would also benefit from creating a more comprehensive API to be able to do things like filtering dataframes by date to make more readable graphs.
Finally, I would figure out an effective way to filter the most and least used words to glean more relevant results (as opposed to listing prepositions). While this data
is not useful without sentiment analysis, I find it quite interesting and it is one of the  most easily understood aspects of the data.
This all being said, I am happy with how this project turned out relative to the scope of what I could realistically do singlehandedly.
