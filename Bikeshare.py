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
    city = {}
    while city not in ('new york city', 'chicago', 'washington'):
        city = input("Which city do you want? new york city, chicago or washington? R:\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = {}
    while month not in ('All','January', 'February', 'March', 'April',     'May', 'June'):
        month = input("Which month do you want? All, January, February, March, April, May, June? R:\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = {}
    while day not in ('All', 'Monday', 'Tuesday', 'Wednesday',             'Thursday', 'Friday', 'Saturday','Sunday'):
        day = input("Which day do you want? All, Monday, Tuesday,Wednesday, Thursday, Friday, Saturday, Sunday? R:\n")


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

# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


# filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int and filter by month to create the new dataframe
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

# filter by day of week if applicable and filter by day of week to create the new dataframe
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('most common month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_dayweek = df['day_of_week'].mode()[0]
    print('the most common day of week:', most_common_dayweek)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_starthour = df['hour'].mode()[0]
    print('the most common start hour:', most_common_starthour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #To fetch the highest count value use the pandas value_counts() and idxmax() functions simultaneously.
    # TO DO: display most commonly used start station
    Start_station = df['Start Station'].value_counts().idxmax()
    print('most Commonly used start station:', Start_station)

    # TO DO: display most commonly used end station
    End_station = df['End Station'].value_counts().idxmax()
    print('most Commonly used end station:', End_station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_start_end_station = df.groupby(['Start Station', 'End Station']).count()
    print('most frequent combination of start station and end station  trip:', Combination_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_Travel_Time = sum(df['Trip Duration'])
    print('total travel time:', total_Travel_Time)

    # TO DO: display mean travel time
    mean_travel_Time = df['Trip Duration'].mean()
    print('mean travel time:', mean_travel_Time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('most Commonly used end station:', count_user_type)

    # The try: block will generate an exception, because x is not defined:
    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print('counts of gender:', count_gender)
    except KeyError:
        print("No data available for this city:whashington.")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        print('earliest:', earliest_birth)
    except KeyError:
        print("earliest birth - No data available for this city:whashington.")
        
    try:    
        most_recent_birth = df['Birth Year'].max()
        print('most recent:', most_recent_birth)
    except KeyError:
        print("recent birth - No data available for this city:whashington.")
    
    try:
        most_common_year_birth = df['Birth Year'].mode()[0]
        print('most common year:', most_common_year_birth)
    except KeyError:
        print("year birth - No data available for this city:whashington.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    #TO DO: new function called display_data will show the data based on the location
def display_data(df):
    start_loc = 0
    while True:
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue? yes or no.\n ").lower()
        if view_data.lower() != 'yes':
            break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
