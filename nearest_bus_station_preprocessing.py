# nearest_bus_station preprocessing
import data_declaration

#
def convert_eng_station(df):
    for index, row in df.iterrows():
        line_name = str(row['호선'])
        if not line_name.isdigit():
            # B -> 분당선으로 이름변경
            if line_name == 'B':
                line_name = '분당선'
                
            # K -> 중앙선으로 이름변경
            elif line_name == 'K':
                line_name = '중앙선'
                
        # 숫자로 저장되어있는 호선을 '0호선'으로 이름변경
        else:
            line_name = line_name + '호선'
        df.at[index, '호선'] = line_name
        

df_nearest_bus_station = data_declaration.df_nearestBusStation
df_nearest_bus_station = df_nearest_bus_station[['전철역코드', '외부코드', '전철역명', '호선', '정류장명', '정류장ID']]
convert_eng_station(df_nearest_bus_station)
df_nearest_bus_station.to_csv("final_nearest_bus_station.csv", index = False)