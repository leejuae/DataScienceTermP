from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the DataFrame from 'data/concat_final.csv'
df = pd.read_csv('data/concat_final.csv')

# Print the first few rows of the DataFrame
print(df.head())

# Calculate '유동인구수' by summing '총승차승객수' and '총하차승객수'
df['유동인구수'] = df['총승차승객수'] + df['총하차승객수']

# Scale the selected features using MinMaxScaler
features_to_scale = ['유동인구수', '평균 상대습도(%)', '일강수량(mm)', '평균기온(°C)']
scaler = MinMaxScaler()
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

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

# Print the updated DataFrame with encoded columns
print(df.head())

# Select the features and target columns
features_columns = df.columns.drop(['일시', '총승차승객수', '총하차승객수', '유동인구수'])
target_columns = ['혼잡유무']
features = df[features_columns]
target = df[target_columns].values.ravel()

# Split the dataset into training and testing data
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.3, random_state=0)

# Initialize the Gradient Boosting classifier
model = GradientBoostingClassifier()

# Fit the model on the training data
model.fit(features_train, target_train)

# Predict on the test data
predictions = model.predict(features_test)

# Evaluate the model
accuracy = metrics.accuracy_score(predictions, target_test)
print("Accuracy:", accuracy)

# Compute and display the confusion matrix
cm = metrics.confusion_matrix(predictions, target_test)
print("Confusion Matrix:")
print(cm)

# Perform cross-validation and print the scores
scores = cross_val_score(model, features, target, cv=10)
print("Cross-Validation Scores:", scores)
print("Mean Score:", scores.mean())

# Create a correlation matrix DataFrame
correlation_df = pd.concat([features, pd.DataFrame(target, columns=target_columns)], axis=1)

# Calculate the correlation matrix
corr = correlation_df.corr()

# Plot the correlation matrix using a heatmap
plt.figure(figsize=(10,10))
sns.heatmap(corr, annot=True, cmap='coolwarm', square=True)

# Display the plot
plt.show()