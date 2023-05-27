#weather Preprocessing
import data_declaration

def remove_hyphens(df):
    df['일시'] = df['일시'].str.replace('-', '')

df_weather = data_declaration.df_weather
df_weather = df_weather[['일시', '평균기온(°C)', '강수 계속시간(hr)', '일강수량(mm)', '평균 상대습도(%)', '평균 전운량(1/10)']]
remove_hyphens(df_weather)
print(df_weather.head())