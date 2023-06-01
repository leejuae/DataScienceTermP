#데이터 normalization
import data_declaration
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

# 역명: label encoder
# 요일은 라벨 인코더 수행 안하고 직접 부과하는 방식으로 할 예정
# 방식은 같지만 좀 더 직관성을 확보하기 위해
# 최종 자료에서도 굳이 원래값으로 변환하지 않아도 바로 이해가 가능하게 하고싶어서
# ex) sun = 0, mon = 1, tue = 2, wed = 3, ...
# 온도 decimal scaling
# 강수량, 상대습도는 min-max

# Import data
df = data_declaration.df_concat_final

# drop '일시' column
df = df[['역명','총승차승객수','총하차승객수','요일','평균기온(°C)','일강수량(mm)','평균 상대습도(%)']]

# Label encoding
encoder = LabelEncoder()
df_encoded = encoder.fit_transform(df['역명'].values)

# One-hot encoding
onehot_encoder = OneHotEncoder(sparse=False)
encoded_columns = onehot_encoder.fit_transform(df_encoded[['역명']])
df = pd.concat([df.drop('역명', axis=1), pd.DataFrame(encoded_columns)], axis=1)


# 요일도 똑같이 수행
# Label encoding
encoder = LabelEncoder()
df = encoder.fit_transform(df['요일'].values)

# One-hot encoding
onehot_encoder = OneHotEncoder(sparse=False)
encoded_columns = onehot_encoder.fit_transform(df[['요일']])
df = pd.concat([df.drop('요일', axis=1), pd.DataFrame(encoded_columns)], axis=1)

# MinMaxScaler 선언 및 Fitting
mMscaler = MinMaxScaler()
mMscaler.fit(df['일강수량(mm)','평균 상대습도(%)'].values)

# 데이터 변환
df = mMscaler.transform(df['일강수량(mm)','평균 상대습도(%)'].values)

# standard scaler 선언 및 학습
standardScaler = StandardScaler().fit(df['평균기온(°C)'])

# test셋 내 feature들에 대하여 standard scaling 수행
df = standardScaler.transform(df['평균기온(°C)'])