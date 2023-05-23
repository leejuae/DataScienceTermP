# 지하철 데이터 preprocessing
# 요일 feature 추가 -> 파이썬 라이브러리 사용
# 지하철 데이터에 ()부분 제외해야함!!!!! 이부분을 어떻게 처리해야할지 모르겠음..

import pandas as pd

df_nearestBusStation = pd.read_csv("D:\git\DataScienceTermP\subway\subway202301.csv", encoding='utf-8')
print(df_nearestBusStation.head())