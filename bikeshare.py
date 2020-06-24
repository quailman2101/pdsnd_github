import time
import pandas as pd

def seperator(x = '=', y = 40):
    """
    Seperator function used for aesthetic purposes.
    Args:
        (str) x - The symbol to be repeatedly printed, '=' by default.
        (int) y - The number of times for x to be printed, 40 by default.
    """
    print(x * y)


def get_filters():
    """
    Asks user to input which city they want to see data for, and asks if they
    would like to filter by month and day.
    Returns:
        chosen city, month, day
    """
    city_data = { 'chicago': 'chicago.csv',
                  'new york city': 'new_york_city.csv',
                  'washington': 'washington.csv' }

    print('Hello!  Let\'s explore some US bikeshare data!')
    seperator('-')

    #Get user to pick which city they want data on
    while True:
        city = input('''Which cities data would you like to explore?
Enter 'chicago', 'new york city', or 'washington': ''').lower()
        if city in city_data.keys():
            break
        else:
            print('\nInvalid input.  Please try again.\n')
            continue
    seperator('-')

    #Get user to pick whether to filter by a specific month or not
    while True:
        month = input('''Which month would you like to explore?  Enter 'all',
'january', 'february', 'march', 'april', 'may', or 'june': ''').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month == 'all':
            print('\nLets get the data for all months.')
            break
        elif month in months:
            print('\nLets get the data for {}.'.format(month.title()))
            break
        else:
            print('\nInvalid input.  Please try again.\n')
            continue
    seperator('-')

    #Get user to pick whether to filter by a specific day or not
    while True:
        day = input('''Which day of the week would you like to explore?
Enter 'all', 'monday', 'tuesday', etc: ''').lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        'saturday', 'sunday']
        if day == 'all':
            print('\nLets get the data for everyday.')
            break
        elif day in days:
            print('\nLets get the data for all {}s.'.format(day.title()))
            break
        else:
            print('Invalid input.  Please try again.')
            continue
    seperator()
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the requested city and filters by month and day if requested
    Args:
        (str) city - the name of the city to analyze
        (str) month - the name of the month to filter by or 'all' for no filter
        (str) day - the name of the day to filter by or 'all' for no filter
    Returns:
        df - Panda DataFrame containing the city data, filtered if requested

    """
<<<<<<< HEAD
    #Load csv into DataFrame and add needed columns
    df = pd.read_csv(CITY_DATA[city])
||||||| 68fb774
    #Load csv into DataFrame and add need columns
    df = pd.read_csv(CITY_DATA[city])
=======
    city_data = { 'chicago': 'chicago.csv',
                  'new york city': 'new_york_city.csv',
                  'washington': 'washington.csv' }
    #Load csv into DataFrame and add need columns
    df = pd.read_csv(city_data[city])
>>>>>>> 81965ce3a227db016759f3bfec94c887480584c2
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour

    #Filter by month only
    if month != 'all' and day == 'all':
        mdf = df[(df['Month']==month.title())]
        return mdf

    #Filter by day only
    elif day != 'all' and month == 'all':
        ddf = df[(df['Day']==day.title())]
        return ddf

    #Filter by month and day
    elif month != 'all' and day != 'all':
        mddf = df[(df['Month']==month.title()) & (df['Day']==day.title())]
        return mddf

    #No filter
    else:
        return df


def totals_no_filter(df):
    """
    Function only called if the user did not request a month or day filter,
    displays some overall statistics on the data.
    Args:
        df - Panda DataFrame that was produced in previous function.
    """
    print('\nNo filter?  Lets calculate some overall statistics first...\n')
    time.sleep(2)
    start_time = time.time()
    seperator('-')

    #Calculate trips per month
    tm = df['Month'].value_counts()
    print('The following shows the trip count per month:\n')
    for k, v in tm.iteritems():
        print('{:10} : {:,}'.format(k, v))
    seperator('-')

    #Calculate trips per days
    td = df['Day'].value_counts()
    print('The following shows the trip count per day:\n')
    for k, v in td.iteritems():
        print('{:10} : {:,}'.format(k, v))
    seperator('-')

    #Display how long it took for above calculations to run
    print('These calculations took {:.5f} seconds to complete.'
    .format(time.time() - start_time))
    seperator()



def time_stats(df):
    """
    Calculates and displays statistics relating to the busiest times.
    Args:
        df - Panda DataFrame that was produced earlier in program.
    """

    print('\nLets calculate the most frequent times of travel...\n')
    time.sleep(2)
    start_time = time.time()
    seperator('-')

    #Calculate the busiest month
    busiest_month = df['Month'].value_counts().idxmax()
    print('The busiest month in this data set is {}.'.format(busiest_month))
    seperator('-')

    #Calculate the busiest day
    busiest_day = df['Day'].value_counts().idxmax()
    print('The busiest day in this data set is {}.'.format(busiest_day))
    seperator('-')

    #Calculate the busiest hour
    busiest_hour = df['Hour'].value_counts().idxmax()
    print('The busiest hour in this data set is {}.'.format(busiest_hour))
    seperator('-')

    #Display how long it took for above calculations to run
    print('These calculations took {:.5f} seconds to complete.'
    .format(time.time() - start_time))
    seperator()


def station_stats(df):
    """
    Calculates and displays statistics relating to the most popular stations.
    Args:
        df - Panda DataFrame that was produced earlier in program.
    """
    print('\nLets calculate the most popular station and trip...\n')
    time.sleep(2)
    start_time = time.time()
    seperator('-')

    #Calculate the busiest start station
    bss = df['Start Station'].value_counts().idxmax()
    print('The busiest starting station in this data set is {}.'.format(bss))
    seperator('-')

    #Calculate the busiest ending station
    bes = df['End Station'].value_counts().idxmax()
    print('The busiest ending station in this data set is {}.'.format(bes))
    seperator('-')

    #Calculate the most frequent round trip
    stations = df.groupby(['Start Station', 'End Station']).count()
    print('The most common route is between {} and {}.'\
    .format(stations.idxmax()[0][0], stations.idxmax()[0][1]))
    seperator('-')

    #Display how long it took for above calculations to run
    print('These calculations took {:.5f} seconds to complete.'
    .format(time.time() - start_time))
    seperator()


def trip_duration_stats(df):
    """
    Calculates and displays statistics relating to the length of trips.
    Args:
        df - Panda DataFrame that was produced earlier in program.
    """
    print('\nLets calculate the total and the average trip duration...\n')
    time.sleep(2)
    start_time = time.time()
    seperator('-')

    #Calculate the total time of all trips in data set
    s_sum = df['Trip Duration'].sum()
    print('The total time of all trips in this data set is {:,.0f} seconds.'
    .format(s_sum))
    print('That is {:,.2f} minutes.'.format(s_sum/60))
    print('That is {:,.2f} hours.'.format(s_sum/60/60))
    print('That is {:,.2f} days.'.format(s_sum/60/60/24))
    seperator('-')

    #Calculate the average time of all trips in this data set
    s_mean = df['Trip Duration'].mean()
    print('The average time of all trips in this data is {:,.2f} seconds.'
    .format(s_mean))
    print('That is {:,.2f} minutes.'.format(s_mean/60))
    seperator('-')

    #Display how long it took for above calculations to run
    print('These calculations took {:.5f} seconds to complete.'
    .format(time.time() - start_time))
    seperator()


def user_stats(df):
    """
    Calculates and displays statistics relating to bikeshare users.
    Args:
        df - Panda DataFrame that was produced earlier in program.
    """
    print('\nLets calculate some statistics on bikeshare users...\n')
    time.sleep(2)
    start_time = time.time()
    seperator('-')

    #Calculate the count of each user Type
    u = df['User Type'].value_counts()
    print('The following shows the count of each user type:\n')
    for k, v in u.iteritems():
        print('{:10} : {:,}'.format(k, v))
    seperator('-')

    #Calculate the counts of male and female user_stats
    if 'Gender' in df.columns:
        g = df['Gender'].value_counts()
        print('The following shows the count of male and female users:\n')
        for k, v in g.iteritems():
            print('{:7} : {:,}'.format(k, v))
        seperator('-')

    #Find the earliest year of birth
    if 'Birth Year' in df.columns:
        eb = df['Birth Year'].min()
        print('Our oldest users were born in {:.0f}.'.format(eb))
        if eb < 1900:
            print('Looks like someone entered their date of birth incorrectly.')
        seperator('-')

    #Find the most recent year of birth
        rb = df['Birth Year'].max()
        print('Our youngest users were born in {:.0f}.'.format(rb))
        if rb > 2011:
            print('Looks like someone entered their date of birth incorrectly.')
        seperator('-')

    #Find the most common year of birth
        cb = df['Birth Year'].value_counts().idxmax()
        print('The most common birth year for our users is {:.0f}.'.format(cb))
        seperator('-')

    #Display how long it took for above calculations to run
    print('These calculations took {:.5f} seconds to complete.'
    .format(time.time() - start_time))
    seperator()

def raw_data(df):
    """
    Displays raw data at the users request.
    Args:
        df - Panda DataFrame that was produced earlier in program.
    """
    #Drop columns I earlier inserted and sort by Start Time
    df = df.drop(['Month', 'Day', 'Hour'], axis = 1)
    df = df.fillna('Unknown')
    df = df.sort_values(by=['Start Time'])
    df_stacked = df.stack()

    #Display the next 5 lines until user is satisfied
    count = 0
    columns = df.shape[1]
    while True:
        r_data = input('''\nWould you like to see some raw data?
Enter 'y' or 'n': ''').lower()
        if r_data != 'y':
            break
        else:
            print(df_stacked[(columns*count*5):(columns*(count*5+5))])
            count += 1
    seperator()

#Main function controlling flow of program
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if month == 'all' and day == 'all':
            totals_no_filter(df)
            input("\nPress 'enter' to continue: \n")


        time_stats(df)
        input("\nPress 'enter' to continue: \n")

        station_stats(df)
        input("\nPress 'enter' to continue: \n")

        trip_duration_stats(df)
        input("\nPress 'enter' to continue: \n")

        user_stats(df)
        input('\nPress \'enter\' to continue: \n')

        raw_data(df)

        restart = input('''\nWould you like to restart?
Enter 'y' or 'n': ''').lower()
        if restart != 'y':
            break

#Don't run if module is imported
if __name__ == '__main__':
    main()
