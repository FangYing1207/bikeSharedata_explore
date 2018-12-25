
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image


# In[2]:


CITY_DATA = { 'chicago': 'F:\\Udacity\\pro2_ExploreBikeShareData\\bikeshare_data\\chicago.csv',
         'new york': 'F:\\Udacity\\pro2_ExploreBikeShareData\\bikeshare_data\\new_york_city.csv',
         'washington': 'F:\\Udacity\\pro2_ExploreBikeShareData\\bikeshare_data\\washington.csv' }


# In[3]:


def input_mod(input_print,error_print,enterable_list):
    ret = input(input_print).lower()
    while ret not in enterable_list:
        ret = input(error_print).lower()
    return ret


# In[4]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (int) day - number of the day of week to filter by, or 0 to apply no day filter
    """
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input_mod('Would you like to see data for chicago,new york,or washington?\nType a city name:',
               '\nDid you spell it correctly? Check and Try again...',
                ['chicago','new york','washington'])   
    print(city)
    month = 'all'
    day = 0
        # TO DO: get user input for month and day of week
    while True:
        choice = input_mod('Would you like to filter data by month,day or both?\nType month,day,or both:',
                     "\nSeems like you type something that isn't wanted...",
                      ['both','month','day'])         
#         print(choice)

        # TO DO: get user input for month (all, january, february, ... , june)
        if choice == 'both' or choice == 'month':
         
            month = input_mod('Which month? Jan,Feb,March,April,May,June,or all?:',
                        '\nDid you spell it correctly? Check and Try again...',  
                         ['all','jan','feb','march','april','may','june'])   
#         print(month)
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        if choice == 'both'or choice == 'day':
            
            day = input_mod('Which day? Please type your response as an integer(e.g.1=Sunday),0 represents no filter:',
                       "\nDid you type it right? Use number 0-7(e.g.1='Sunday')",
                        ['0','1','2','3','4','5','6','7'])
            day = int(day)  
#             print(day)
        return city,month,day    
        break  
    print('-'*40)


# In[5]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (int) day - index of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert Start Time and End Time into datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month,day_of_week,hour from Start Time and cerate columns
    df['month'] = df['Start Time'].dt.month #df['month']的值为int64
    df['day_of_week'] = df['Start Time'].dt.weekday_name ##df['day_of_week']的值为object类型，Monday,Tuesday...
    df['hour'] = df['Start Time'].dt.hour
   # 按照用户输入的month得到需要进行“计算”的dataframe
    month_list = ['all','jan','feb','march','april','may','june']
    if month != 'all':
        df = df[df['month']== month_list.index(month)]
    
   # 按照用户输入的day(数字1=Sunday)得到需要进行“计算”的dataframe
    weekday_list = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    if day !=0:
          df = df[df['day_of_week'] == weekday_list[day-1]]           
    return df


# In[6]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most popular month to travel is:{}'.format(popular_month))
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day to travel is:{}'.format(popular_day))
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour to travel is:{}'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The Most Popular Start Stations: {}'.format(df['Start Station'].mode()[0]))
#     print('-'*40)
#     print(df['Start Station'].value_counts())
#     print('-'*40)
     
    # TO DO: display most commonly used end station
    print('The Most Popular End Stations: {}'.format(df['End Station'].mode()[0]))
#     print('-'*40)
#     print(df['End Station'].value_counts())
    # TO DO: display most frequent combination of start station and end station trip
    df['combined_station'] = df['Start Station'] + " -> "+ df['End Station']
    print('The most frequent combination of start station and end station trip: {}'.format(df['combined_station'].mode()[0]))
#     top = df.groupby(['Start Station', 'End Station']).size().idxmax()
#     print("The most frequent combination of start station and end station trip is {} to {}".format(top[0], top[1])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total trip duration is: {} seconds'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The average trip duration is: {}seconds'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[9]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
        
    # TO DO: Display counts of gender
        

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("The youngest user's birth year is: {}".format(int(df['Birth Year'].max())))
        print("The oldest user's birth year is: {}".format(int(df['Birth Year'].min())))
        print("The most frequent user's birth year is: {}".format(int(df['Birth Year'].mode()[0])))
        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[10]:


def main():
    while True:
        print('Hello! Let\'s explore some US bikeshare data!')
#         img = image.imread('img_bikeshare')#读取图片文件
#         plt.imshow(img)#显示图片
#         plt.axis('off')#不显示坐标轴
#         plt.show()
        city,month,day = get_filters()
        df = load_data(city,month,day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()

