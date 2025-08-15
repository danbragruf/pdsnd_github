# Bikeshare Project Information for the README

### Date created
Date created _2025-08-15_

### Project Title
Bikeshare Project - An interactive experience

### Description
The goal of the **Bikeshare project** is to use Python to explore data related to bike share systems. It includes one Python file and one or more .csv data files.

### Files used in the repository
- bikeshare.py
- new_york_city.csv

### Credits
#### Loading the data: 
Parts from the code from _'practice problem #3'_ and the solution have been used and slightly adapted. For example converting the End Time `to_datetime` as well. Furthermore "duration" has been recalculated from seconds to hours. As both columns are now "date time" an alternative approach coud be to calculate the duration via End Time - Start Time to get more Precise results (days, hours, minutes, seconds), however as duration was already given in the data frames, I used this approach for now as most efficient method.

I am using `.idxmax()` to extract the most common start and end stations, as well as the most frequent trip combination and other insights from the DataFrame. Using `.idxmax` according to the documentation on panday.pydata.org:
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html

Instead of `dt.weekday_name` in the part: 
`df['day_of_week'] = df['Start Time'].dt.weekday_name`
I used `dt.day_name()` as used in more recent versions of pandas
- https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_name.html 

For the messages on the statistics instead of `.format()` I used **f-strings**
`print(f'some message {some_variable}')`
- https://docs.python.org/3/library/stdtypes.html#formatted-string-literals-f-strings
- https://www.w3schools.com/python/python_string_formatting.asp

To show the first 5 rows of the data frame I used `'iloc'` and tested multiple approaches while
Referring to the pandas documentation: 
- https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#
Furthermore I utilised this tutorial:
- https://www.datacamp.com/tutorial/loc-vs-iloc 

