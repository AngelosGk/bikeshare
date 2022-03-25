# Python Script
# Import libraries
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
    # get user input for city (chicago, new york city, washington). 
    city =  input('Please Select one of the following cities:chicago, new york city, washington').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input ('Not valid city').lower()
    
    # get user input for month (all, january, february, ... , june)
    month = input('Please Select a preferable month').lower()
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input('Not Valid Month ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please Select a preferable day').lower()
    while day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        day = input('Not Valid day').lower()
        
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
    #load file 
    df = pd.read_csv(CITY_DATA[city])

    #convert Time into date 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #extract month 
    df['month'] = df['Start Time'].dt.month

    #filter the month

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month
        df = df[df['month'] == month]

    # extract day from Start Time 
    df['week_days'] = df['Start Time'].dt.weekday_name
    # filter by day of week if applicable
    if day != 'all':
        # filter by day 
        df = df[df['week_days'] == day.title()]
    return df

# STATS OF TIME
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("common month is: ", df['month'].value_counts().idxmax())

    # display the most common day of week
    print(" common day is: ", df['week_days'].value_counts().idxmax())

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("common hour is: ", df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("common start station is: ", df ['Start Station'].value_counts().idxmax())

    # display most commonly used end station
    print("common end station is: ", df['End Station'].value_counts().idxmax())

    # display most frequent combination of start station and end station trip
    print("frequent combination of start station and end station trip")
    start_end_stations = df.groupby(['Start Station', 'End Station']).size()
    print(start_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    duration_total = df['Trip Duration'].sum() / 3600
    print("total travel time in hours is: ", duration_total)

    # display mean travel time
    duration_mean = df['Trip Duration'].mean() / 3600
    print("mean travel time in hours is: ", duration_mean )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

S
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    types = df['User Type'].value_counts()
    print(types)
    # Display counts of gender
    if 'Gender' in df:
     print('count gender',df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
     The_earliest_year= int(df['Birth Year'].min())
     most_recent_year= int(df['Birth Year'].max())
     most_common_year= int(df['Birth Year'].value_counts().idxmax())
     print("The earliest year :",The_earliest_year,
          ", most recent yea:",most_recent_year,
           "and the most common year: ",most_common_year)

     print("\nThis took %s seconds." % (time.time() - start_time))
     print('-'*40)

def raw_data (df):
    """Displays the data due filteration.
    5 rows will added in each press"""
    print('press enter or no to skip')
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df.head(x))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
