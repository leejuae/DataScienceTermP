# 지하철 데이터 preprocessing
import pandas as pd
from datetime import datetime
import data_declaration
import re

def dropCol(df):
    return df[['사용일자', '노선명', '역명', '승차총승객수', '하차총승객수']]

# 역명(부멱명) 데이터에서 부역명 데이터를 삭제함(nearrest_busStation data에는 부역명 정보가 없기 때문)
def remove_bracketed_data(df, column_name):
    pattern = r'\([^)]*\)'  # 괄호로 묶인 데이터를 찾는 정규표현식 패턴
    df[column_name] = df[column_name].apply(lambda x: re.sub(pattern, '', str(x)))
    
    return df

# 사용일자(20220303)같은 데이터를 기준으로 해당 날짜의 요일을 구해 새로운 feature인 '요일'에 저장하는 함수.
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
    
# 양평역(5호선), 양평역(중앙선)
# 서울역 데이터 서울로 바꿔야 함.
def yang(df):
    # 서울역 데이터만 역이 붙어 있어서 '서울'로 역명 변경
    df.loc[df['역명'] == '서울역', '역명'] = '서울'
    
    # 이수역(7호선)과 총신대역(4호선) 환승역임에도 불구하고 명칭이 다름. 따라서 총신대역 이름 '이수'로 변경
    df.loc[df['역명'] == '총신대입구', '역명'] = '이수'
    
    df.loc[(df['노선명'] == '5호선') & (df['역명'] == '양평'), '역명'] = '양평(5호선)'
    df.loc[(df['노선명'] == '중앙선') & (df['역명'] == '양평'), '역명'] = '양평(중앙선)'
        
    return df

# 노선명 drop
# 환승역 처리 위함
def drop_line_name(df):
    return df[['사용일자', '역명', '승차총승객수', '하차총승객수']]
    
# 동일 역명 다른위치를 제외하고 역명이 같으면 승하차 승객수 더함 -> 환승역 처리

def concat_same_name(df):
   
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
df_subway202301 = dropCol(df_subway202302)
df_subway202302 = dropCol(df_subway202303)
df_subway202303 = dropCol(df_subway202304)

df_subway2022 = remove_bracketed_data(df_subway2022, '역명')
df_subway202301 = remove_bracketed_data(df_subway202301, '역명')
df_subway202302 = remove_bracketed_data(df_subway202302, '역명')
df_subway202303 = remove_bracketed_data(df_subway202303, '역명')
df_subway202304 = remove_bracketed_data(df_subway202304, '역명')

df_subway2022 = yang(df_subway2022)
df_subway202301 = yang(df_subway202301)
df_subway202302 = yang(df_subway202302)
df_subway202303 = yang(df_subway202303)
df_subway202304 = yang(df_subway202304)

df_subway2022 = drop_line_name(df_subway2022)
df_subway202301 = drop_line_name(df_subway202301)
df_subway202302 = drop_line_name(df_subway202302)
df_subway202303 = drop_line_name(df_subway202303)
df_subway202304 = drop_line_name(df_subway202304)

df_subway2022 = concat_same_name(df_subway2022)
df_subway202301 = concat_same_name(df_subway202301)
df_subway202302 = concat_same_name(df_subway202302)
df_subway202303 = concat_same_name(df_subway202303)
df_subway202304 = concat_same_name(df_subway202304)

df_subway2022 = get_day_of_week(df_subway2022)
df_subway202301 = get_day_of_week(df_subway202301)
df_subway202302 = get_day_of_week(df_subway202302)
df_subway202303 = get_day_of_week(df_subway202303)
df_subway202304 = get_day_of_week(df_subway202304)

# Concatenate the datasets
df_concatenated = pd.concat([df_subway2022, df_subway202301, df_subway202302,
                             df_subway202303, df_subway202304])


df_concatenated.to_csv("data/final_data/final_subway_station.csv", index = False)