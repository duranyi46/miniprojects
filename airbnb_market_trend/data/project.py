import pandas as pd
import numpy as np
import datetime as dt

# reviews = pd.read_csv('airbnb_last_review.tsv', sep = '\t')
reviews = pd.read_csv('C:\\Users\\deadp\\pythonProject\\airbnb_market_trend\\data\\airbnb_last_review.tsv', sep = '\t')
# prices = pd.read_csv('airbnb_price.csv')
prices = pd.read_csv('C:\\Users\\deadp\\pythonProject\\airbnb_market_trend\\data\\airbnb_price.csv')
# file = 'airbnb_market_trend/data/airbnb_room_type.xlsx'
file = 'C:\\Users\deadp\\pythonProject\\airbnb_market_trend\\data\\airbnb_room_type.xlsx'
room_type = pd.ExcelFile(file)
room_type_df = room_type.parse(0)
print(room_type_df.head())
print(reviews.head())
print(prices.head())

reviews.info() # Last reviews are not stored as dates.
reviews.isna().sum() # There are no missing values in last review column.
room_type_df.info()
room_type_df.isna().sum()
prices.info()
prices.isna().sum() 

# As there is no null entry in listing_id columns of all the dataframes, i can merge them

dF = reviews.merge(prices, on = 'listing_id', how = 'outer')
dF = dF.merge(room_type_df, on = 'listing_id', how = 'outer')


# What are the dates of the earliest and most recent reviews? Store these values as two separate variables with your preferred names.

dF['last_review'] = pd.to_datetime(dF['last_review']).dt.date


earliest_review = dF['last_review'].sort_values().iloc[0]
latest_review = dF['last_review'].sort_values(ascending = False).iloc[0]


print('Latest review is:',latest_review)
print('Earliest review is:',earliest_review)

# How many of the listings are private rooms? Save this into any variable.

dF['room_type'].unique()# As there are some different categories essentially same, i need to match them.
# There should be 3 categories which are entire home/apt, private room, shared room
dF['room_type'].isna().sum() # There is not any missing value i need to consider so
dF['room_type'] = dF['room_type'].str.lower()
dF['room_type'].unique() # Now there are 3 categories
private_room_count = dF['room_type'].value_counts().loc['private room']
private_room_count


# What is the average listing price? Round to the nearest two decimal places and save into a variable.
dF['price'] = dF['price'].str.replace('dollars','')
dF['price'] = dF['price'].str.strip()
dF['price'] = dF['price'].astype('int')
avg_listing_price = dF['price'].mean()
avg_listing_price = round(avg_listing_price, 2)
avg_listing_price = str(avg_listing_price) + ' dollars'

# Combine the new variables into one DataFrame called review_dates with four columns in the following order: first_reviewed, last_reviewed, nb_private_rooms, and avg_price. The DataFrame should only contain one row of values.
data = {'first_reviewed' : earliest_review, 'last_reviewed': latest_review, 'nb_private_rooms': private_room_count, 'avg_price' : avg_listing_price}
review_date = pd.DataFrame(data, index =['Only Row'])
print(review_date)








