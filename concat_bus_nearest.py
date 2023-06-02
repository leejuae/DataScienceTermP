# 버스정류장이랑 nearest bus station만 합침. (지하철역 데이터 안합침.)
import pandas as pd
import data_declaration

# Select rows from df_nearestBusStation where '정류장ID' matches with '버스정류장ARS번호' in df_BusStation
# 전철역 주변 버스정류장 데이터(nearest_busStation)을 이용해서 지하철역 주변 버스정류장만 뽑아냄.
def mergedf(df_bus, df_nearest):

    # Convert '정류장ID' column to int type
    df_bus['버스정류장ARS번호'] = df_bus['버스정류장ARS번호'].astype(int)

    # merge the same bus station
    df_bus = pd.merge(df_nearest, df_bus, left_on='정류장ID', right_on='버스정류장ARS번호')

    # Group by '전철역코드', '전철역명', '호선', '사용일자' and sum '승차총승객수' and '하차총승객수'
    df_bus = df_bus.groupby(['전철역코드', '외부코드', '전철역명', '호선', '사용일자'], as_index=False)['승차총승객수', '하차총승객수'].sum().reset_index()

    return df_bus


# --------------------------------------------------------------------


df_bus = data_declaration.final_bus_station
df_nearest = data_declaration.final_nearest_bus_station

df_final = mergedf(df_bus, df_nearest)

# 호선 drop
# 환승역 처리 위함\
df_final = df_final[['전철역명', '사용일자', '승차총승객수', '하차총승객수']]

# 동일 역명 다른위치를 제외하고 역명이 같으면 승하차 승객수 더함 -> 환승역 처리
# 버스정류장 데이터 합치는거임
df_final = df_final.groupby(['사용일자', '전철역명']).sum().reset_index()

# 총신대입구(이수) --> 이수로 명칭변경
df_final.loc[df_final['전철역명'] == '총신대입구(이수)', '전철역명'] = '이수'

df_final.to_csv("concat_data/concat_near_bus.csv", index = False)