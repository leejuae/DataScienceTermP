import pandas as pd
import data_declaration

# Drop unnecessary columns
def drop_columns(df):
    # Drop rows with invalid '버스정류장ARS번호'
    df = df[df['버스정류장ARS번호'] != '~']
    
    return df[['사용일자', '버스정류장ARS번호', '승차총승객수', '하차총승객수']]

# Group by '버스정류장ARS번호', '사용일자' and sum '승차총승객수' and '하차총승객수'
def group_df(df):
    df = df.groupby(['사용일자', '버스정류장ARS번호']).sum().reset_index()
    return df

# Drop unnecessary columns and group the datasets
df_bus_station_2201 = group_df(drop_columns(data_declaration.df_BusStation2201))
df_bus_station_2202 = group_df(drop_columns(data_declaration.df_BusStation2202))
df_bus_station_2203 = group_df(drop_columns(data_declaration.df_BusStation2203))
df_bus_station_2204 = group_df(drop_columns(data_declaration.df_BusStation2204))
df_bus_station_2205 = group_df(drop_columns(data_declaration.df_BusStation2205))
df_bus_station_2206 = group_df(drop_columns(data_declaration.df_BusStation2206))
df_bus_station_2207 = group_df(drop_columns(data_declaration.df_BusStation2207))
df_bus_station_2208 = group_df(drop_columns(data_declaration.df_BusStation2208))
df_bus_station_2209 = group_df(drop_columns(data_declaration.df_BusStation2209))
df_bus_station_2210 = group_df(drop_columns(data_declaration.df_BusStation2210))
df_bus_station_2211 = group_df(drop_columns(data_declaration.df_BusStation2211))
df_bus_station_2212 = group_df(drop_columns(data_declaration.df_BusStation2212))
df_bus_station_2301 = group_df(drop_columns(data_declaration.df_BusStation2301))
df_bus_station_2302 = group_df(drop_columns(data_declaration.df_BusStation2302))
df_bus_station_2303 = group_df(drop_columns(data_declaration.df_BusStation2303))
df_bus_station_2304 = group_df(drop_columns(data_declaration.df_BusStation2304))

# Concatenate the datasets
df_concatenated = pd.concat([df_bus_station_2201, df_bus_station_2202, df_bus_station_2203,
                             df_bus_station_2204, df_bus_station_2205, df_bus_station_2206,
                             df_bus_station_2207, df_bus_station_2208, df_bus_station_2209,
                             df_bus_station_2210, df_bus_station_2211, df_bus_station_2212,
                             df_bus_station_2301, df_bus_station_2302, df_bus_station_2303,
                             df_bus_station_2304])

# Save the concatenated dataset to a CSV file
df_concatenated.to_csv("final_bus_station.csv", index=False)