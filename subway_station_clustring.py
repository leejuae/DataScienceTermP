import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import DBSCAN

df = pd.read_csv('station_coordinate.csv', encoding='utf-8')
X = df['lat']
y = df['lng']

X = np.array(X).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
y_scaled = scaler.fit_transform(y)

plt.figure(figsize=(10, 10))

plt.scatter(X_scaled, y_scaled)
plt.show()

eps = 0.1  # 이웃 거리 범위 조정
min_samples = 5  # 클러스터에 속하는 최소 샘플 수

dbscan = DBSCAN(eps=eps, min_samples=min_samples)
labels = dbscan.fit_predict(np.concatenate((X_scaled, y_scaled), axis=1))

plt.scatter(X_scaled, y_scaled, c=labels)
plt.show()