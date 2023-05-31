# Import necessary libraries
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics
import pandas as pd
import numpy as np

# Assume that you have a DataFrame 'df' with 'n' features and 'target' as your target variable
df = pd.read_csv('data.csv') # replace 'data.csv' with your data file

# Now, we split the dataset into features (independent variables) and target (dependent variable)
features = df.drop('target', axis=1) # replace 'target' with your target column name
target = df['target']

# Split the dataset into training and testing data
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.3, random_state=0)

# Initialize the Decision Tree Regressor model
regressor = DecisionTreeRegressor(random_state=0)

# Fit the model with training data
regressor.fit(features_train, target_train)

# Now, we make predictions on the testing data
target_pred = regressor.predict(features_test)

# Evaluate the model
print('Mean Absolute Error:', metrics.mean_absolute_error(target_test, target_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(target_test, target_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(target_test, target_pred)))
print('Accuracy:', regressor.score(target_test, target_pred))