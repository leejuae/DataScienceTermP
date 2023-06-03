# First, we need to import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd
import numpy as np

# Assume that you have a DataFrame 'df' with 'n' features and 'target' as your target variable
df = pd.read_csv('data/concat_final.csv') # replace 'data.csv' with your data files

print(df.head())

df['유동인구수'] = df['총승차승객수'] + df['총하차승객수']

encoding_column = ['역명', '요일']
le = LabelEncoder()
df[encoding_column] = df[encoding_column].apply(le.fit_transform)
print(df.head())

features_to_scale = ['유동인구수', '평균 상대습도(%)', '일강수량(mm)', '평균기온(°C)']
scaler = StandardScaler()
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

# Now, we split the dataset into features (independent variables) and target (dependent variable)
features_columns = df.columns.drop(['일시', '총승차승객수', '총하차승객수'])
target_columns = ['유동인구수']

features = df[features_columns]
target = df[target_columns]

# Split the dataset into training and testing data
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.3, random_state=0)

# Initialize the Linear Regression model
regressor = LinearRegression()

# Fit the model with training data
regressor.fit(features_train, target_train)

# Now, we make predictions on the testing data
target_pred = regressor.predict(features_test)

# Evaluate the model
print('Mean Squared Error:', metrics.mean_squared_error(target_test, target_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(target_test, target_pred)))
print('Mean Absolute Error:', metrics.mean_absolute_error(target_test, target_pred))  