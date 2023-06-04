import pandas as pd
from datetime import datetime
import data_declaration
import re

def dropCol(df):
    return df[['사용일자', '노선명', '역명', '승차총승객수', '하차총승객수']]

# Function to remove bracketed data from the station name column
def remove_bracketed_data(df, column_name):
    pattern = r'\([^)]*\)'  # Regular expression pattern to find data within brackets
    df[column_name] = df[column_name].apply(lambda x: re.sub(pattern, '', str(x)))
    
    return df

# Function to get the day of the week from the '사용일자' column and store it in a new column called '요일'
def get_day_of_week(df):
    # Convert integer values to strings
    df['사용일자'] = df['사용일자'].astype(str)
        
    # Iterate over the column values and convert them to datetime objects
    dates = [datetime.strptime(date, "%Y%m%d") for date in df['사용일자']]
    
    # Get the day of the week for each date
    day_of_weeks = [date.strftime("%A") for date in dates]
        
    # Add a new column for the day of the week
    df['요일'] = day_of_weeks
        
    return df
    
# Function to rename stations as '양평(5호선)' and '양평(중앙선)' instead of just '양평'
# and to rename '서울역' to '서울' as there is no specific station named '서울역' in nearest_busStation data.
def rename_stations(df):
    # Rename '서울역' to '서울'
    df.loc[df['역명'] == '서울역', '역명'] = '서울'
    
    # Rename '총신대입구' to '이수' as it is a transfer station between Line 7 and Line 4
    df.loc[df['역명'] == '총신대입구', '역명'] = '이수'
    
    # Rename '양평' to '양평(5호선)' for Line 5 and '양평(중앙선)' for Jungang Line
    df.loc[(df['노선명'] == '5호선') & (df['역명'] == '양평'), '역명'] = '양평(5호선)'
    df.loc[(df['노선명'] == '중앙선') & (df['역명'] == '양평'), '역명'] = '양평(중앙선)'
        
    return df

# Function to drop the '노선명' column for handling transfer stations
def drop_line_name(df):
    return df[['사용일자', '역명', '승차총승객수', '하차총승객수']]
    
# Function to combine the passenger counts for stations with the same name, excluding different locations
def combine_same_name(df):
    df = df.groupby(['사용일자', '역명']).sum().reset_index()
    return df

# --------------------------------------------------------------------

df_subway2022 = data_declaration.df_subway_2022
df_subway202301 = data_declaration.df_subway_202301
df_subway202302 = data_declaration.df_subway_202302
df_subway202303 = data_declaration.df_subway_202303
df_subway202304 = data_declaration.df_subway_202304

df_subway2022 = dropCol(df_subway2022)
df_subway202301 = dropCol(df_subway202301)
df_subway202302 = dropCol(df_subway202302)
df_subway202303 = dropCol(df_subway202303)
df_subway202304 = dropCol(df_subway202304)

df_subway2022 = remove_bracketed_data(df_subway2022, '역명')
df_subway202301 = remove_bracketed_data(df_subway202301, '역명')
df_subway202302 = remove_bracketed_data(df_subway202302, '역명')
df_subway202303 = remove_bracketed_data(df_subway202303, '역명')
df_subway202304 = remove_bracketed_data(df_subway202304, '역명')

df_subway2022 = rename_stations(df_subway2022)
df_subway202301 = rename_stations(df_subway202301)
df_subway202302 = rename_stations(df_subway202302)
df_subway202303 = rename_stations(df_subway202303)
df_subway202304 = rename_stations(df_subway202304)

df_subway2022 = drop_line_name(df_subway2022)
df_subway202301 = drop_line_name(df_subway202301)
df_subway202302 = drop_line_name(df_subway202302)
df_subway202303 = drop_line_name(df_subway202303)
df_subway202304 = drop_line_name(df_subway202304)

df_subway2022 = combine_same_name(df_subway2022)
df_subway202301 = combine_same_name(df_subway202301)
df_subway202302 = combine_same_name(df_subway202302)
df_subway202303 = combine_same_name(df_subway202303)
df_subway202304 = combine_same_name(df_subway202304)

df_subway2022 = get_day_of_week(df_subway2022)
df_subway202301 = get_day_of_week(df_subway202301)
df_subway202302 = get_day_of_week(df_subway202302)
df_subway202303 = get_day_of_week(df_subway202303)
df_subway202304 = get_day_of_week(df_subway202304)

# Concatenate the datasets
df_concatenated = pd.concat([df_subway2022, df_subway202301, df_subway202302,
                             df_subway202303, df_subway202304])

df_concatenated.to_csv("data/final_data/final_subway_station.csv", index=False)