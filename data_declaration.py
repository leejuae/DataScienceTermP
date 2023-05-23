import pandas as pd
# 외부코드,전철역명,호선,정류장명,정류장ID,(X)좌표,(Y)좌표
df_nearestBusStation = pd.read_csv("nearest_bus_station.csv", encoding='utf-8')
df_nearestBusStation = df_nearestBusStation[['외부코드', '전철역명', '호선', '정류장명', '정류장ID']]

df_BusStation2201 = pd.read_csv("bus_station/busStation202201.csv", encoding='utf-8')
df_BusStation2202 = pd.read_csv("bus_station/busStation202202.csv", encoding='utf-8')
df_BusStation2203 = pd.read_csv("bus_station/busStation202203.csv", encoding='utf-8')
df_BusStation2204 = pd.read_csv("bus_station/busStation202204.csv", encoding='utf-8')
df_BusStation2205 = pd.read_csv("bus_station/busStation202205.csv", encoding='utf-8')
df_BusStation2206 = pd.read_csv("bus_station/busStation202206.csv", encoding='utf-8')
df_BusStation2207 = pd.read_csv("bus_station/busStation202207.csv", encoding='utf-8')
df_BusStation2208 = pd.read_csv("bus_station/busStation202208.csv", encoding='utf-8')
df_BusStation2209 = pd.read_csv("bus_station/busStation202209.csv", encoding='utf-8')
df_BusStation2210 = pd.read_csv("bus_station/busStation202210.csv", encoding='utf-8')
df_BusStation2211 = pd.read_csv("bus_station/busStation202211.csv", encoding='utf-8')
df_BusStation2212 = pd.read_csv("bus_station/busStation202212.csv", encoding='utf-8')
df_BusStation2301 = pd.read_csv("bus_station/busStation202301.csv", encoding='utf-8')
df_BusStation2302 = pd.read_csv("bus_station/busStation202302.csv", encoding='utf-8')
df_BusStation2303 = pd.read_csv("bus_station/busStation202303.csv", encoding='utf-8')
df_BusStation2304 = pd.read_csv("bus_station/busStation202304.csv", encoding='utf-8')


df_subway_202301 = pd.read_csv("subway/subway202301.csv", encoding='utf-8')
df_subway_202302 = pd.read_csv("subway/subway202302.csv", encoding='utf-8')
df_subway_202303 = pd.read_csv("subway/subway202303.csv", encoding='utf-8')
df_subway_202304 = pd.read_csv("subway/subway202304.csv", encoding='utf-8')
df_subway_2022 = pd.read_csv("subway/subway2022.csv", encoding='utf-8')
