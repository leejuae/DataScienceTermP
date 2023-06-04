import data_declaration
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Set display option to show all columns
pd.set_option('display.max_columns', None)

# Import data
df = data_declaration.df_concat_final

# Drop '일시' column
df = df[['역명', '총승차승객수', '총하차승객수', '요일', '평균기온(°C)', '일강수량(mm)', '평균 상대습도(%)']]

# Print the initial DataFrame
print(df)

# Label encoding for '역명'
encoder = LabelEncoder()
df_encoded = encoder.fit_transform(df['역명'].values)

# Replace '역명' column with encoded values
df['역명'] = df_encoded

# Print DataFrame after label encoding for '역명'
print(df)

# One-hot encoding for '역명'
onehot_encoder = OneHotEncoder(sparse=False)
encoded_columns = onehot_encoder.fit_transform(df_encoded.reshape(-1, 1))
df = pd.concat([df.drop('역명', axis=1), pd.DataFrame(encoded_columns)], axis=1)

# Print DataFrame after one-hot encoding for '역명'
print("After One-hot encoding")
print(df)

# Label encoding for '요일'
encoder = LabelEncoder()
df['요일'] = encoder.fit_transform(df['요일'].values)

# One-hot encoding for '요일'
onehot_encoder = OneHotEncoder(sparse=False)
encoded_columns = onehot_encoder.fit_transform(df[['요일']])
df = pd.concat([df.drop('요일', axis=1), pd.DataFrame(encoded_columns)], axis=1)

# Min-max scaling for '일강수량(mm)' and '평균 상대습도(%)'
minmax_scaler = MinMaxScaler()
df[['일강수량(mm)', '평균 상대습도(%)']] = minmax_scaler.fit_transform(df[['일강수량(mm)', '평균 상대습도(%)']].values)

# Standard scaling for '평균기온(°C)'
standard_scaler = StandardScaler()
df['평균기온(°C)'] = standard_scaler.fit_transform(df[['평균기온(°C)']])

# Apply standard scaling to '평균기온(°C)' in the test dataset
df['평균기온(°C)'] = standard_scaler.transform(df[['평균기온(°C)']])

# Print the final DataFrame
print(df)