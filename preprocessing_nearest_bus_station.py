import data_declaration

# Function to convert subway line names
def convert_eng_station(df):
    for index, row in df.iterrows():
        line_name = str(row['호선'])
        if not line_name.isdigit():
            # Change 'B' to '분당선'
            if line_name == 'B':
                line_name = '분당선'

            # Change 'K' to '중앙선'
            elif line_name == 'K':
                line_name = '중앙선'

        # Change numeric subway line names to format 'X Line'
        else:
            line_name = line_name + '호선'
        df.at[index, '호선'] = line_name


df_nearest_bus_station = data_declaration.df_nearestBusStation
df_nearest_bus_station = df_nearest_bus_station[['외부코드', '전철역명', '호선', '정류장명', '정류장ID']]
convert_eng_station(df_nearest_bus_station)
df_nearest_bus_station.to_csv("data/final_data/final_nearest_bus_station.csv", index = False)
