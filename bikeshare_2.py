import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january','february', 'march','april','may','june'] #a list of months for later use
days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday'] # a list of days for later use

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    ans = False
    while ans == False:
        try:
            city = str(input('Please choose a city from the following options:\nChicago, New York City, or Washington.\nWhat city would you like? ')).lower()
            if city not in ['chicago', 'new york city', 'washington']:
                print('\nSorry that is not a valid city. Please try again!\n')
            else:
                ans = True
        except:
            print('Sorry that is not a valid input. Please try again!')

    print('\n')
    # get user input for month (all, january, february, ... , june)
    answered = False
    while answered == False:
        try:
            month = str(input('Please choose a month from the following options:\nall, january, february, ... , june.\nWhat month would you like? ')).lower()
            if month not in ['all','january','february', 'march','april','may','june']:
                print('\nSorry that is not a valid month. Please try again!\n')
            else:
                answered = True
        except:
            print('Sorry that is not a valid input. Please try again!')
    print('\n')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    answered = False
    while answered == False:
        try:
            day = str(input('Please choose a day from the following options:\nall, sunday, monday,...saturday.\nWhat day would you like? ')).lower()
            if day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
                print('\nSorry that is not a valid day. Please try again!\n')
            else:
                answered = True
        except:
            print('Sorry that is not a valid input. Please try again!')

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
    df = pd.read_csv(CITY_DATA[city])
    
    #Adds some new columns for year, month, day, and hour
    df['year'] = pd.DatetimeIndex(df['Start Time']).year
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day'] = pd.DatetimeIndex(df['Start Time']).dayofweek
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    
    if month != 'all': #if anything other than 'all' is selected, then filter by month
        month = months.index(month) +1 #finds the numerical number of the month by adding 1 to its index
        df = df[df['month'] == month]
    
    if day != 'all': #if anything other than 'all' is selected, then filter by day
        day = days.index(day)
        df = df[df['day'] == day]
        
    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'all': #Only perform the analysis if a specific month was not selected
        highest_month = df['month'].mode()[0] #find the most common month
        highest_month_occurrences = df['month'].value_counts()[highest_month] #find the number of occurrence of the previously calculated month
        print('The most common month is',months[highest_month-1],'with',highest_month_occurrences,'occurrences.') #print results
    else:
        print('Data pulled only for',month,'Most common month of this subset will be the month you chose.') #avoid the calculation if a specific month was selected
    

    # display the most common day of week
    if day == 'all': #Only perform the analysis if a specific day was not selected
        highest_day = df['day'].mode()[0] #find the most common day
        highest_day_occurrences = df['day'].value_counts()[highest_day] #find the number of occurrence of the previously calculated day
        print('The most common day is',days[highest_day-1],'with',highest_day_occurrences,'occurrences.') #print results
    else:
        print('Data pulled only for',day,'Most common day of this subset will be the day you chose.')#avoid the calculation if a specific day was selected


    # display the most common start hour
    highest_hour = df['hour'].mode()[0] #find the most common day
    highest_hour_occurrences = df['hour'].value_counts()[highest_hour] #find the number of occurrence of the previously calculated hour
    print('The most common hour is',highest_hour,'with',highest_hour_occurrences,'occurrences.') #print results

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



#The following functions work in the same way as the function above. If there are any differences in the general syntax, it will be annotated.

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    highest_start_station = df['Start Station'].mode()[0]
    highest_start_station_occurrences = df['Start Station'].value_counts()[highest_start_station]
    print('The most common start station is',highest_start_station,'with',highest_start_station_occurrences,'occurrences.')

    # display most commonly used end station
    highest_end_station = df['End Station'].mode()[0]
    highest_end_station_occurrences = df['End Station'].value_counts()[highest_end_station]
    print('The most common end station is',highest_end_station,'with',highest_end_station_occurrences,'occurrences.')

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' -> '+df['End Station'] # Make a new column of trips separated by 'TO' so both start and end destinations are captured
    highest_trip = df['trip'].mode()[0]
    highest_trip_occurrences = df['trip'].value_counts()[highest_trip]
    print('The most common trip is',highest_trip,'with',highest_trip_occurrences,'occurrences.')
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum() #sum of all travel time is found

    # display mean travel time
    mean_travel_time = total_travel_time / df['Trip Duration'].count() #total travel time divided by number of trips
    
    print('Total travel time is',total_travel_time,' seconds, and mean travel time is',mean_travel_time,'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    try: #not all datasets have this information, so a try statement is added. If it fails, a generic statement will be printed
        user_types = df['User Type'].nunique()
        print('There are',user_types,'unique user types:')
        print(df.groupby('User Type')['User Type'].count().to_string(header=False))
        print('\n')
        
    except:
        print('This file does not have user statistics.')

    # Display counts of gender
    try: #not all datasets have this information, so a try statement is added. If it fails, a generic statement will be printed
        gender_types = df['Gender'].nunique()
        print('There are',gender_types,'unique genders:')
        print(df.groupby('Gender')['Gender'].count().to_string(header=False))
        print('\n')
        
    except:
        print('This file does not have user statistics.')
        

    # Display earliest, most recent, and most common year of birth
    try: #not all datasets have this information, so a try statement is added. If it fails, a generic statement will be printed
        earliest_year = int(df['Birth Year'].min())
        latest_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print('There earliest birth year is:',earliest_year,'\nThe latest birth year is:',latest_year,'\nThe most common birth year is:',most_common_year)
    except:
        print('This file does not have user statistics.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_data(df):
    #This function asks if you want to print out the data with 5 lines shown at a time.
    df = df.drop(['Unnamed: 0','year','month','day','hour','trip'],axis=1) #Removes the extra columns used for calculation
    stop = False #set an arbitrary parameter for the while loop to start and change once a condition is met
    number_of_rows = df.shape[0] # Pull the number of rows
    index = 0 #start the indexing at 0
    while stop == False: #while condition is false, do the following
        if index == number_of_rows-1: #If index reaches the end, force a break of the while loop
            stop = True
        
        try: #take in user input for seeing 5 rows of data
            answer = str(input('Would you like to print out 5 lines of data? yes or no?\n')).lower()
            if answer not in ['yes', 'y']: #if not yes, break the while loop
                print('No more data will be displayed. Thank you!')
                stop = True
            else: #if yes, print 5 lines of data starting with index
                print(df.iloc[index:index+5].to_string())
                
            if index+5 > number_of_rows-1: #If index has increased to greater than the end of the dataframe rows, set a condition that will break with the first line of the while loop
                index = number_of_rows -1
            else:
                index+=5 #Otherwise add 5 to the index to print the next 5 rows

        except:
            print('Sorry that is not a valid input. Please try again!')
        
    return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_data(df)

        restart = str(input('\nWould you like to restart? Enter yes or no.\n'))
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
