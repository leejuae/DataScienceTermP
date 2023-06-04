import pandas as pd
import data_declaration

# Combine bus and subway data with weather data
def concat_weather(df_bns, df_weather):
    
    df = pd.merge(df_bns, df_weather, on=['일시'], how='left')
    
    return df

df_bns = data_declaration.df_concat_bus_near_sub
df_weather = data_declaration.final_weather

# Rename '사용일자' column to '일시' for consistency
df_bns.rename(columns={'사용일자': '일시'}, inplace=True)

df_final = concat_weather(df_bns, df_weather)

df_final.to_csv("data/concat_data/concat_final.csv", index=False)
