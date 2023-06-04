from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the DataFrame from 'data/concat_final.csv'
df = pd.read_csv('data/concat_final.csv')  

# Calculate '유동인구수' by summing '총승차승객수' and '총하차승객수'
df['유동인구수'] = df['총승차승객수'] + df['총하차승객수']

# Encode categorical columns using OneHotEncoder
onehot_encoders = {}

encoding_columns = ['역명', '요일']
for column in encoding_columns:
    onehot_encoders[column] = OneHotEncoder(sparse=False)
    df_encoded = onehot_encoders[column].fit_transform(df[[column]])
    df_encoded = pd.DataFrame(df_encoded, columns=[f'{column}_{i}' for i in range(df_encoded.shape[1])])
    df = pd.concat([df, df_encoded], axis=1)
    df.drop(columns=[column], inplace=True)

# Scale the selected features using StandardScaler
features_to_scale = ['평균 상대습도(%)', '일강수량(mm)', '평균기온(°C)']
scaler = StandardScaler()
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

# Split the dataset into features (independent variables) and target (dependent variable)
target_columns = ['유동인구수']
features_columns = df.columns.drop(['일시', '총승차승객수', '총하차승객수', '유동인구수'])
features = df[features_columns]
target = df[target_columns]

# Split the dataset into training and testing data
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.3, random_state=0)

# Initialize the Linear Regression model
regressor = LinearRegression()

# Fit the model with training data
regressor.fit(features_train, target_train)

# Make predictions on the testing data
target_pred = regressor.predict(features_test)

# Evaluate the model
print('Mean Squared Error:', metrics.mean_squared_error(target_test, target_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(target_test, target_pred)))
print('Mean Absolute Error:', metrics.mean_absolute_error(target_test, target_pred))

print('R-squared:', metrics.r2_score(target_test, target_pred))

# Draw the model
plt.figure(figsize=(10,6))

plt.scatter(target_test, target_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs. Predicted Values")

plt.plot([min(target_test.values), max(target_test.values)], [min(target_test.values), max(target_test.values)], color='red') # A red line representing perfect prediction
plt.tight_layout()
plt.show()
