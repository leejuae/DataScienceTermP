# DS preprocessing
# 버스정류장 preprocessing
# 지하철역 주변 버스정류장 data select, concat all bus stop dataset

import pandas as pd
import data_declaration


# Drop unnecessary columns
def dropCol(df):
    # Drop rows with invalid '버스정류장ARS번호'
    df = df[df['버스정류장ARS번호'] != '~']
    
    return df[['사용일자', '버스정류장ARS번호', '승차총승객수', '하차총승객수']]


# 버스 기준으로 데이터 정리되어있음!! 따라서 정류장 ID와 버스정류장 ARS 번호(둘 다 고유ID) 값을 이용해서 같은 정류장의 승하차 승객수를 합침.
# Group by '버스정류장ARS번호', '사용일자' and sum '승차총승객수' and '하차총승객수'
def groupdf(df):
    df = df.groupby(['사용일자', '버스정류장ARS번호']).sum().reset_index()
    return df

# --------------------------------------------------------------------

df_BusStation2201 = dropCol(data_declaration.df_BusStation2201)
df_BusStation2202 = dropCol(data_declaration.df_BusStation2202)
df_BusStation2203 = dropCol(data_declaration.df_BusStation2203)
df_BusStation2204 = dropCol(data_declaration.df_BusStation2204)
df_BusStation2205 = dropCol(data_declaration.df_BusStation2205)
df_BusStation2206 = dropCol(data_declaration.df_BusStation2206)
df_BusStation2207 = dropCol(data_declaration.df_BusStation2207)
df_BusStation2208 = dropCol(data_declaration.df_BusStation2208)
df_BusStation2209 = dropCol(data_declaration.df_BusStation2209)
df_BusStation2210 = dropCol(data_declaration.df_BusStation2210)
df_BusStation2211 = dropCol(data_declaration.df_BusStation2211)
df_BusStation2212 = dropCol(data_declaration.df_BusStation2212)
df_BusStation2301 = dropCol(data_declaration.df_BusStation2301)
df_BusStation2302 = dropCol(data_declaration.df_BusStation2302)
df_BusStation2303 = dropCol(data_declaration.df_BusStation2303)
df_BusStation2304 = dropCol(data_declaration.df_BusStation2304)

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

# Concatenate the datasets
df_concatenated = pd.concat([df_BusStation2201, df_BusStation2202, df_BusStation2203,
                             df_BusStation2204, df_BusStation2205, df_BusStation2206,
                             df_BusStation2207, df_BusStation2208, df_BusStation2209,
                             df_BusStation2210, df_BusStation2211, df_BusStation2212,
                             df_BusStation2301, df_BusStation2302, df_BusStation2303,  df_BusStation2304])


# 지하철 역 주변의 버스정류장만 뽑아서 만듦.
df_concatenated.to_csv("data/final_data/final_bus_station.csv", index = False)
