#데이터셋 test file
import data_declaration
import pandas as pd

df = data_declaration.df_nearestBusStation
non_int = df[~df['호선'].astype(str).str.isdigit()]
for _, row in non_int.iterrows():
    print(f"전철역명: {row['전철역명']}, 호선: {row['호선']}")