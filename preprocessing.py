#DS preprocessing

import pandas as pd

df_nearestBusStation = pd.read_csv("D:\git\DataScienceTermP\\nearest_busStation.csv", encoding='euc-kr')
df_nearestBusStation = df_nearestBusStation[['전철역코드', '외부코드', '전철역명', '호선', '정류장명', '정류장ID']]

df_BusStation2201 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202201.csv", encoding='euc-kr')
df_BusStation2202 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202202.csv", encoding='euc-kr')
df_BusStation2203 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202203.csv", encoding='euc-kr')
df_BusStation2204 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202204.csv", encoding='euc-kr')
df_BusStation2205 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202205.csv", encoding='euc-kr')
df_BusStation2206 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202206.csv", encoding='euc-kr')
df_BusStation2207 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202207.csv", encoding='euc-kr')
df_BusStation2208 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202208.csv", encoding='euc-kr')
df_BusStation2209 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202209.csv", encoding='euc-kr')
df_BusStation2210 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202210.csv", encoding='euc-kr')
df_BusStation2211 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202211.csv", encoding='euc-kr')
df_BusStation2212 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202212.csv", encoding='euc-kr')
df_BusStation2301 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202301.csv", encoding='euc-kr')
df_BusStation2302 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202302.csv", encoding='euc-kr')
df_BusStation2303 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202303.csv", encoding='euc-kr')
df_BusStation2304 = pd.read_csv("D:\git\DataScienceTermP\\busStation\\busStation202304.csv", encoding='euc-kr')


# Drop unnecessary columns
def dropCol(df):
    return df[['사용일자', '버스정류장ARS번호', '승차총승객수', '하차총승객수']]

df_BusStation2201 = dropCol(df_BusStation2201)
df_BusStation2202 = dropCol(df_BusStation2202)
df_BusStation2203 = dropCol(df_BusStation2203)
df_BusStation2204 = dropCol(df_BusStation2204)
df_BusStation2205 = dropCol(df_BusStation2205)
df_BusStation2206 = dropCol(df_BusStation2206)
df_BusStation2207 = dropCol(df_BusStation2207)
df_BusStation2208 = dropCol(df_BusStation2208)
df_BusStation2209 = dropCol(df_BusStation2209)
df_BusStation2210 = dropCol(df_BusStation2210)
df_BusStation2211 = dropCol(df_BusStation2211)
df_BusStation2212 = dropCol(df_BusStation2212)
df_BusStation2301 = dropCol(df_BusStation2301)
df_BusStation2302 = dropCol(df_BusStation2302)
df_BusStation2303 = dropCol(df_BusStation2303)
df_BusStation2304 = dropCol(df_BusStation2304)

# Group by '버스정류장ARS번호', '사용일자' and sum '승차총승객수' and '하차총승객수'
def groupdf(df):
    df = df.groupby(['사용일자', '버스정류장ARS번호']).sum().reset_index()
    return df

df_BusStation2201 = groupdf(df_BusStation2201)
df_BusStation2202 = groupdf(df_BusStation2202)
df_BusStation2203 = groupdf(df_BusStation2203)
df_BusStation2204 = groupdf(df_BusStation2204)
df_BusStation2205 = groupdf(df_BusStation2205)
df_BusStation2206 = groupdf(df_BusStation2206)
df_BusStation2207 = groupdf(df_BusStation2207)
df_BusStation2208 = groupdf(df_BusStation2208)
df_BusStation2209 = groupdf(df_BusStation2209)
df_BusStation2210 = groupdf(df_BusStation2210)
df_BusStation2211 = groupdf(df_BusStation2211)
df_BusStation2212 = groupdf(df_BusStation2212)
df_BusStation2301 = groupdf(df_BusStation2301)
df_BusStation2302 = groupdf(df_BusStation2302)
df_BusStation2303 = groupdf(df_BusStation2303)
df_BusStation2304 = groupdf(df_BusStation2304)

# Select rows from df_nearestBusStation where '정류장ID' matches with '버스정류장ARS번호' in df_BusStation
def mergedf(df):
    # Drop rows with invalid '버스정류장ARS번호'
    df = df[df['버스정류장ARS번호'] != '~']
    
    # Convert '정류장ID' column to int type
    df['버스정류장ARS번호'] = df['버스정류장ARS번호'].astype(int)
    
    # merge the same bus station
    df = pd.merge(df_nearestBusStation, df, left_on='정류장ID', right_on='버스정류장ARS번호')
    
    # Group by '전철역코드', '전철역명', '호선', '사용일자' and sum '승차총승객수' and '하차총승객수'
    df = df.groupby(['전철역코드', '전철역명', '호선', '사용일자'], as_index=False)['승차총승객수', '하차총승객수'].sum().reset_index()
    
    return df

df_BusStation2201 = mergedf(df_BusStation2201)
df_BusStation2202 = mergedf(df_BusStation2202)
df_BusStation2203 = mergedf(df_BusStation2203)
df_BusStation2204 = mergedf(df_BusStation2204)
df_BusStation2205 = mergedf(df_BusStation2205)
df_BusStation2206 = mergedf(df_BusStation2206)
df_BusStation2207 = mergedf(df_BusStation2207)
df_BusStation2208 = mergedf(df_BusStation2208)
df_BusStation2209 = mergedf(df_BusStation2209)
df_BusStation2210 = mergedf(df_BusStation2210)
df_BusStation2211 = mergedf(df_BusStation2211)
df_BusStation2212 = mergedf(df_BusStation2212)

# Concatenate the datasets
df_concatenated = pd.concat([df_BusStation2201, df_BusStation2202, df_BusStation2203, 
                             df_BusStation2204, df_BusStation2205, df_BusStation2206, 
                             df_BusStation2207, df_BusStation2208, df_BusStation2209,
                             df_BusStation2210, df_BusStation2211, df_BusStation2212,
                             df_BusStation2301, df_BusStation2302, df_BusStation2303, df_BusStation2304])


df_concatenated.to_csv("D:\git\DataScienceTermP\concatBusStation.csv")