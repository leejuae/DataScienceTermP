# First, we need to import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import pandas as pd
import numpy as np

# Assume that you have a DataFrame 'df' with 'n' features and 'target' as your target variable
df = pd.read_csv('data/concat_final.csv') # replace 'data.csv' with your data file

print(df.head())

df['유동인구수'] = df['총승차승객수'] + df['총하차승객수']


features_to_scale = ['유동인구수', '평균 상대습도(%)', '일강수량(mm)', '평균기온(°C)']
scaler = MinMaxScaler()
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

def traffic_level(x):
    if x > 0.75:
        return '혼잡'
    elif 0.5 < x <= 0.75:
        return '약간혼잡'
    elif 0.25 < x <= 0.5:
        return '보통'
    else:
        return '원활'

df['혼잡유무'] = df['유동인구수'].apply(traffic_level)

encoding_column = ['역명', '요일', '혼잡유무']
le = LabelEncoder()
df[encoding_column] = df[encoding_column].apply(le.fit_transform)
print(df.head())

features_columns = df.columns.drop(['일시', '총승차승객수', '총하차승객수'])
target_columns = ['혼잡유무']

features = df[features_columns]
target = df[target_columns].values.ravel()


# Split the dataset into training and testing data
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.3, random_state=0)

# Initialize the Gradient Boosting regressor
model = GradientBoostingClassifier()

# Fit the model on the training data
model.fit(features_train, target_train)

# Predict on the test data
predictions = model.predict(features_test)

# Evaluate the model
accuracy = metrics.accuracy_score(predictions, target_test)
print("Accuracy:", accuracy)

cm = metrics.confusion_matrix(predictions, target_test)
print("Confusion Matrix:")
print(cm)

scores = cross_val_score(model, features, target, cv=5)
print("Cross-Validation Scores:", scores)
print("Mean Score:", scores.mean())