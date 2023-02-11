#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:26:55 2023

@author: shougfahad
"""


import time
import pandas as pd
import numpy as np
#modify data location to run the code on your device 
CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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
    while True:
        city = input(
            '\nhich city would you like to see data for? (chicago, new york city, washington) ').lower()
        if str(city).title() not in CITY_DATA.keys():
            print('\nSorry that\'s not a failed option, try again!\n')
            continue
        else:
            print("Got it")
            break


    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            '\nWhich month would you like to see data for? (January, February, March, April, May, June or all) ').lower()
        if str(month) not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
            print('\nSorry that)\'s not a failed option, try again!')
            continue
        else:
            print("Got it")
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            'Which day would you like to see data for? (Sunday, Monday, Tuesday, Wenseday, Thursday, Friday, or all) ').lower()
        if str(day) not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            print('\nSorry that)\'s not a failed option, try again!')
            continue
        else:
            print("\nGot it")
            break

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
    df = pd.read_csv(CITY_DATA[city.title()])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('\n The most common month is: ', df['month'].mode()[0])


    # display the most common day of week
    print('\n The most common day of the week is: ', df['day_of_week'].mode()[0])


    # display the most common start hour
    print('\n The most common start hour is: ', df['Start Time'].dt.hour.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\n The most commonly used start station is: ', df['Start Station'].mode()[0])


    # display most commonly used end station
    print('\n The most commonly used end station is: ', df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+"-"+df['End Station']
    print('\n The most  frequent combination of start station and end station tripis: ',df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # display total travel time
    print('Total travel time:', sum(df['Trip Duration'])/86400, " Days")

    # display mean travel time
    print('Mean travel time:', df['Trip Duration'].mean()/60, " Hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print('User Types:\n', df['User Type'].value_counts())
    
    # Display counts of gender
    try:
        print('\n Count of gender\n',df['Gender'].value_counts())
    except KeyError:
        print("\nGender Types:\nNo data available for this month\ city.")

    # Display earliest, most recent, and most common year of birth
    try:
        print('\nEarlist year of birth: \n', df['Birth Year'].min())
        print('\Most recent year of birth: \n', df['Birth Year'].max())
        print('\nMost common year of birth: \n', df['Birth Year'].mode())
    except KeyError:
        print("\n Birth year data is not avaliable for this city\n.")
    
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def see_date(df):
   y = 0
   x = 5
    # Take input from user if they want to see raw data
   while True:
       while True:
           see_data = input('Would you like to see raw data?(yes or no), each time you will see 5 extra row of data ').lower()
           if see_data not in ('yes','no'):
               continue
           else:
               break
    
       if (see_data != 'no'):
           
           print(df.iloc[y:x])
           y += 5
           x += 5
           continue
       else:
            break
         
           
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_date(df)
     
        
       
        
        while True:
          restart = input('\nWould you like to restart? Enter yes or no.\n')
          if restart.lower() not in ('yes','no'):
              continue
          else:
              break
          
        if restart.lower() != 'yes':
          print("Bye Bye")
          break
        
 

if __name__ == "__main__":
	main()

