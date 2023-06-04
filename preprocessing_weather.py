import data_declaration
import pandas as pd
import matplotlib.pyplot as plt

# Remove hyphens from the '일시' column
def remove_hyphens(df):
    df = df.copy()
    df.loc[:, '일시'] = df['일시'].str.replace('-', '')
    return df

# Data for years 2022 and 2023
def delete_data_2223(df):
    df = df.copy()
    df['일시'] = df['일시'].astype(int)
    df = df[(df['일시'] >= 20220000) & (df['일시'] <= 20231231)]
    return df

# Replace NaN values in '일강수량(mm)' column with 0
def nan2zero(df):
    df = df.copy()
    df.loc[:, '일강수량(mm)'] = df['일강수량(mm)'].fillna(0)
    return df

# Apply preprocessing steps to the weather data
def weather_preprocessing(df):
    df = remove_hyphens(df)
    df = delete_data_2223(df)
    df = nan2zero(df)
    return df

# Get the weather data
df_weather = data_declaration.df_weather

# Select relevant columns for analysis
df_weather = df_weather[['일시', '평균기온(°C)', '일강수량(mm)', '평균 상대습도(%)']]

# Apply weather preprocessing
df_weather = weather_preprocessing(df_weather)

# Save the preprocessed weather data to a CSV file
df_weather.to_csv("data/final_data/final_weather.csv", index = False)

# Display the first few rows of the preprocessed weather data
print(df_weather.head())

# Create histograms to visualize precipitation and average temperature
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].hist(df_weather['일강수량(mm)'], bins=5)
axs[0].set_title('Histogram of daily precipitation(mm)')
axs[0].set_xlabel('precipitation(mm)')
axs[0].set_ylabel('Frequency')

axs[1].hist(df_weather['평균기온(°C)'], bins=5, color='orange')
axs[1].set_title('Histogram of average temperature(°C)')
axs[1].set_xlabel('temperature(°C)')
axs[1].set_ylabel('Frequency')

plt.show()