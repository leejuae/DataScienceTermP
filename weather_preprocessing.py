# weather Preprocessing
# import data_declaration

# df_weather = data_declaration.df_weather
# df_weather = df_weather[['일시', '평균기온(°C)', '강수 계속시간(hr)', '일강수량(mm)', '평균 상대습도(%)', '평균 전운량(1/10)']]
import pandas as pd
import matplotlib.pyplot as plt

def remove_hyphens(df):
    df = df.copy()
    df.loc[:, '일시'] = df['일시'].str.replace('-', '')
    return df

def delete_data_2223(df):
    df = df.copy()
    df['일시'] = df['일시'].astype(int)
    df = df[(df['일시'] >= 20220000) & (df['일시'] <= 20231231)]
    return df

def nan2zero(df):
    df = df.copy()
    df.loc[:, '일강수량(mm)'] = df['일강수량(mm)'].fillna(0)
    return df

def weather_preprocessing(df):
    df = remove_hyphens(df)
    df = delete_data_2223(df)
    df = nan2zero(df)
    return df

df_weather = pd.read_csv("data/weather.csv", encoding='euc-kr')

df_weather = df_weather[['일시', '평균기온(°C)', '일강수량(mm)', '평균 상대습도(%)']]
df_weather = weather_preprocessing(df_weather)

print(df_weather.head())


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