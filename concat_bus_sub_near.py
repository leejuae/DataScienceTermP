import pandas as pd
import data_declaration

# Combine bus stations and subway stations
def concat_sub_bus(df_bn, df_sub):
    
    df = pd.merge(df_sub, df_bn, on=['사용일자', '역명'], how='left')
    df.loc[:, '승차총승객수_x'] = df['승차총승객수_x'].fillna(0)
    df.loc[:, '하차총승객수_x'] = df['하차총승객수_x'].fillna(0)
    df.loc[:, '승차총승객수_y'] = df['승차총승객수_y'].fillna(0)
    df.loc[:, '하차총승객수_y'] = df['하차총승객수_y'].fillna(0)
    
    # Sum the passenger counts for the same columns
    df['Total Boarding'] = df['승차총승객수_x'] + df['승차총승객수_y']
    df['Total Alighting'] = df['하차총승객수_x'] + df['하차총승객수_y']
    
    # Drop unnecessary columns
    df = df[['사용일자', '역명', 'Total Boarding', 'Total Alighting', '요일']]
    
    return df

df_sub = data_declaration.df_final_subway_station
df_bn = data_declaration.df_concat_bus_near

# Rename '전철역명' column to '역명' for consistency
df_bn.rename(columns={'전철역명': '역명'}, inplace=True)

df_final = concat_sub_bus(df_bn, df_sub)

df_final.to_csv("concat_data/concat_bus_near_sub.csv", index=False)
