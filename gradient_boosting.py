from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn import metrics
import pandas as pd

# Define a function to categorize traffic level based on '유동인구수'
def traffic_level(x):
    if x > 0.75:
        return '매우혼잡'
    elif 0.5 < x <= 0.75:
        return '혼잡'
    elif 0.25 < x <= 0.5:
        return '보통'
    else:
        return '원활'

# Read the DataFrame from 'data/concat_final.csv'
df = pd.read_csv('data/concat_final.csv')

# Calculate '유동인구수' by summing '총승차승객수' and '총하차승객수'
df['유동인구수'] = df['총승차승객수'] + df['총하차승객수']

# Scale the selected features using MinMaxScaler
features_to_scale = ['유동인구수', '평균 상대습도(%)', '일강수량(mm)', '평균기온(°C)']
scaler = MinMaxScaler()
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

# Apply the 'traffic_level' function to create the '혼잡유무' column
df['혼잡유무'] = df['유동인구수'].apply(traffic_level)

# Initialize an empty dictionary to store label encoders
label_encoders = {}

# Encode categorical columns using LabelEncoder
encoding_columns = ['역명', '요일', '혼잡유무']
for column in encoding_columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le
    
# Select the features and target columns
features_columns = df.columns.drop(['일시', '총승차승객수', '총하차승객수', '유동인구수', '혼잡유무'])
target_columns = ['혼잡유무']
features = df[features_columns]
target = df[target_columns].values.ravel()

# Split the dataset into training and testing data
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.3, random_state=0)

# Define the parameter grid for RandomizedSearchCV
param_grid = {
    'n_estimators': [50, 100, 150], 
    'learning_rate': [0.1, 0.01, 0.001],
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 4, 6],
    'min_samples_leaf': [1, 2, 3],
    'subsample': [0.8, 0.9, 1.0]
}

# Initialize the Gradient Boosting classifier
model = GradientBoostingClassifier()

# Initialize RandomizedSearchCV
random_search = RandomizedSearchCV(model, param_distributions=param_grid, n_iter=10, cv=5, random_state=0)

# Fit the RandomizedSearchCV on the training data
random_search.fit(features_train, target_train)

# Print the best parameters found
print("Best Parameters:", random_search.best_params_)

# Get the best model from RandomizedSearchCV
best_model = random_search.best_estimator_

# Fit the best model on the training data
best_model.fit(features_train, target_train)

# Predict on the test data using the best model
predictions = best_model.predict(features_test)

# Evaluate the model
accuracy = metrics.accuracy_score(predictions, target_test)
print("Accuracy:", accuracy)

# Compute and display the confusion matrix
cm = metrics.confusion_matrix(predictions, target_test)
print("Confusion Matrix:")
print(cm)

# Perform cross-validation and print the scores
scores = cross_val_score(best_model, features, target, cv=5)
print("Cross-Validation Scores:", scores)
print("Mean Score:", scores.mean())

print()

# Assuming 'best_model' is a trained RandomForestClassifier or GradientBoostingClassifier
importance = best_model.feature_importances_
for i,j in enumerate(importance):
    print(features.columns[i], ":", j)