#날씨데이터까지 합침!!!!!!! 찐찐 최종
import pandas as pd
import data_declaration

# 버스정류장이랑 지하철역 합침
def concat_weather(df_bns, df_weather):
    
    df = pd.merge(df_bns, df_weather, on=['일시'], how='left')
    
    return df

# --------------------------------------------------------------------

df_bns = data_declaration.df_concat_bus_near_sub
df_weather = data_declaration.final_weather

#사용일자 -> 일시로 통일
df_bns.rename(columns = {'사용일자' : '일시'}, inplace =True)

df_final = concat_weather(df_bns, df_weather)

df_final.to_csv("data/concat_data/concat_final.csv", index = False)

