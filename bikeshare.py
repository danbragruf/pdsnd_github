import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input ("Enter city (Chicago, New York City, or Washington): ").strip().lower()
        if city in ('chicago','new york city','washington'):
            break
        else:
            print('invalid input')

    # TO DO: get u-ser input for month (all, january, february, ... , june)
    while True:
        month = input ("Enter month (all, January, Febraury,...,June): ").strip().lower()
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        else:
            print('invalid input')
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input ("Enter Day (all, Monday, Tuesday, Wednesday,...,Sunday): ").strip().lower()
        if day in('all', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            break
        else:
            print('invalid input')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time and end time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    #converting trip duration from seconds to hours
    df['Trip Duration'] = ((df['Trip Duration']/60/60).round(2))
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    #create something do display 'all' vs. 'specific month'
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        common_month = df['month'].value_counts().idxmax()   
        print(f'overall, the most common month is {common_month}')
    else:
        print(f'in {month}')
    
    # TO DO: display the most common day of week
    if day == 'all':
        common_day = df['day_of_week'].value_counts().idxmax()    
        print(f'the most frequent day is {common_day}')
    else:
        print(f'on {day}s')

    # TO DO: display the most common start hour
    df['start_hour']= df['Start Time'].dt.hour
    common_hour = df['start_hour'].value_counts().idxmax()
    print(f'the most common start hour is {common_hour}')
    print()
    
    if day == 'all' and month =='all':
        print('The following overview applies to the whole dataset (all months and days) for the selcted city')
    elif day =='all':
        print(f'The following overview is a subset for {month} (all days)')
    elif month =='all':
        print(f'the following overview is a subset for all {day}s across all months')
    else:
        print(f'the following overview shows data for all {day}s across {month}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    count_start = df['Start Station'].value_counts().max()
    print(f'The most commonly used start station is {common_start_station} with {count_start} trips')
    
    # TO DO: display most commonly used end station
    common_end = df['End Station'].value_counts().idxmax()
    count_end = df['End Station'].value_counts().max()
    print(f'The most commonly used end station is {common_end} with {count_end} trips')

    # TO DO: display most frequent combination of start station and end station trip
    freq_combination = (df.groupby(['Start Station','End Station']).size().idxmax())
    print(f"The most frequent trip is: {freq_combination[0]} -> {freq_combination[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time =  df['Trip Duration'].sum().round(2)
    count_trips = df['Trip Duration'].value_counts().sum()
    print(f'Total travel duration is {total_time} hours across {count_trips} trips')

    # TO DO: display mean travel time
    average_time = df['Trip Duration'].mean().round(2)
    print(f'Average travel time is {average_time} hours')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types= df['User Type'].value_counts()
    nan_user = df['User Type'].isnull().sum()
    print(f'there are {user_types.iloc[0]} {user_types.index[0]}(s) and {user_types.iloc[1]} {user_types.index[1]}(s). {nan_user} have not a specified user type')
    print()
    # TO DO: Display counts of gender
    try: 
        gender = df['Gender'].value_counts()
        nan_gen = df['Gender'].isnull().sum()
        print(f'{gender.iloc[1]} of users are {gender.index[1]} and {gender.iloc[0]} are {gender.index[0]}. For {nan_gen} no specific information on gender is available')
    except KeyError:
        print('there is no data on gender available in the data frame')
    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        birth_common = int(df['Birth Year'].value_counts().idxmax()) 
        nan_birth = df['Birth Year'].isnull().sum()
        print(f'\nThe earliest birth year is: {earliest}\nThe most recent birth year is: {recent}, \nThe most common birth year is: {birth_common}')
        print(f'{nan_birth} did not indicate their birth year')
    except KeyError:
        print('there is no birth year available in the data frame')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city,month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        # asking to show the raw data as a dataframe
        s_row = 0
        
        while True:
            raw_data = input('\ndo you want to see the first 5 rows of the raw data? Enter yes or no.\n').lower()
            if raw_data.lower() != 'yes':
                break
            
            print(df.iloc[s_row:s_row + 5])
            s_row += 5
            
            while True:
                raw_data_plus = input('\nwould you like to see the next 5 rows? Enter yes or no.\n').lower()
                if raw_data_plus == 'yes':
                    print(df.iloc[s_row:s_row + 5])
                    s_row += 5
                else:
                    break
 
        # restarting the search for data
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


