# Data Format
## 5-core
The 5-core data is initially stored as a .json.gz (compressed JSON) file. Each line of the file is a single JSON object representing a complete review. Each review contains an overall score, user verification status, the time the review was made, the reviewer ID, the item ID, the reviewer name, the review text, review summary, and Unix review time. Additional data is included as applicable. 
---
After saving the data, it is stored in a dictionary with each key being the file name and values being a list of the parsed JSON objects.
## Ratings
The ratings data is initially stored as a CSV file. The CSV has 4 columns: Item ID, User ID, Rating, and Unix Timestamp. 
---
After saving the data, it is stored in a dictionary with each key being the file name and values being a dataframe made from reading the CSV.saving