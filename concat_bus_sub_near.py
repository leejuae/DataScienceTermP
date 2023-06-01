import pandas as pd
import data_declaration

# 버스정류장이랑 지하철역 합침
def concat_sub_bus(df_bn, df_sub):
    
    df = pd.merge(df_sub, df_bn, on=['사용일자', '역명'], how='left')
    df.loc[:, '승차총승객수_x'] = df['승차총승객수_x'].fillna(0)
    df.loc[:, '하차총승객수_x'] = df['하차총승객수_x'].fillna(0)
    df.loc[:, '승차총승객수_y'] = df['승차총승객수_y'].fillna(0)
    df.loc[:, '하차총승객수_y'] = df['하차총승객수_y'].fillna(0)
    
    # 승차총승객수 열끼리 더하기
    df['총승차승객수'] = df['승차총승객수_x'] + df['승차총승객수_y']

    # 하차총승객수 열끼리 더하기
    df['총하차승객수'] = df['하차총승객수_x'] + df['하차총승객수_y']
    
    #x, y 드롭
    df= df[['사용일자', '역명', '총승차승객수', '총하차승객수', '요일']]
    
    return df

# --------------------------------------------------------------------

df_sub = data_declaration.df_final_subway_station
df_bn = data_declaration.df_concat_bus_near

#전철역명 -> 역명으로 통일
df_bn.rename(columns = {'전철역명' : '역명'}, inplace =True)

df_final = concat_sub_bus(df_bn, df_sub)

df_final.to_csv("concat_data/concat_bus_near_sub.csv", index = False)