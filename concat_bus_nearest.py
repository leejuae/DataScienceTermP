import pandas as pd
import data_declaration

# Select rows from df_nearestBusStation where '정류장ID' matches with '버스정류장ARS번호' in df_BusStation
# Extract bus stations near subway stations by using the nearest_busStation data
def mergedf(df_bus, df_nearest):

    # Convert '정류장ID' column to int type
    df_bus['버스정류장ARS번호'] = df_bus['버스정류장ARS번호'].astype(int)

    # Merge the same bus stations
    df_bus = pd.merge(df_nearest, df_bus, left_on='정류장ID', right_on='버스정류장ARS번호')

    # Group by '전철역코드', '외부코드', '전철역명', '호선', '사용일자' and sum the '승차총승객수' and '하차총승객수'
    df_bus = df_bus.groupby(['전철역코드', '외부코드', '전철역명', '호선', '사용일자'], as_index=False)['승차총승객수', '하차총승객수'].sum().reset_index()

    return df_bus


df_bus = data_declaration.final_bus_station
df_nearest = data_declaration.final_nearest_bus_station

df_final = mergedf(df_bus, df_nearest)

# Drop the '호선' column for transfer station handling
df_final = df_final[['전철역명', '사용일자', '승차총승객수', '하차총승객수']]

# Combine the passenger counts for the same station names and exclude different locations
# Handle transfer stations by summing the passenger counts for the same station names
df_final = df_final.groupby(['사용일자', '전철역명']).sum().reset_index()

# Rename '총신대입구(이수)' to '이수'
df_final.loc[df_final['전철역명'] == '총신대입구(이수)', '전철역명'] = '이수'

df_final.to_csv("concat_data/concat_near_bus.csv", index=False)
