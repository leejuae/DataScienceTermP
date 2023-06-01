import pandas as pd

#concat 자료들
df_concat_bus_near = pd.read_csv("data/concat_data/concat_near_bus.csv", encoding='utf-8')
df_concat_bus_near_sub = pd.read_csv("data/concat_data/concat_bus_near_sub.csv", encoding='utf-8')
df_concat_final = pd.read_csv("data/concat_data/concat_final.csv", encoding='utf-8')

# nearest_bus_station 자료
df_nearestBusStation = pd.read_csv("data\\nearest_busStation.csv", encoding='euc-kr')
final_nearest_bus_station = pd.read_csv("data\\final_data\\final_nearest_bus_station.csv", encoding='utf-8')

# weather 자료
df_weather = pd.read_csv("data\weather.csv", encoding='euc-kr')
final_weather = pd.read_csv("data/final_data/final_weather.csv", encoding='utf-8')

# df_final_bus_station
final_bus_station = pd.read_csv("data\\final_data\\final_bus_station.csv", encoding='utf-8')

df_BusStation2201 = pd.read_csv("data\\busStation\\busStation202201.csv", encoding='euc-kr')
df_BusStation2202 = pd.read_csv("data\\busStation\\busStation202202.csv", encoding='euc-kr')
df_BusStation2203 = pd.read_csv("data\\busStation\\busStation202203.csv", encoding='euc-kr')
df_BusStation2204 = pd.read_csv("data\\busStation\\busStation202204.csv", encoding='euc-kr')
df_BusStation2205 = pd.read_csv("data\\busStation\\busStation202205.csv", encoding='euc-kr')
df_BusStation2206 = pd.read_csv("data\\busStation\\busStation202206.csv", encoding='euc-kr')
df_BusStation2207 = pd.read_csv("data\\busStation\\busStation202207.csv", encoding='euc-kr')
df_BusStation2208 = pd.read_csv("data\\busStation\\busStation202208.csv", encoding='euc-kr')
df_BusStation2209 = pd.read_csv("data\\busStation\\busStation202209.csv", encoding='euc-kr')
df_BusStation2210 = pd.read_csv("data\\busStation\\busStation202210.csv", encoding='euc-kr')
df_BusStation2211 = pd.read_csv("data\\busStation\\busStation202211.csv", encoding='euc-kr')
df_BusStation2212 = pd.read_csv("data\\busStation\\busStation202212.csv", encoding='euc-kr')
df_BusStation2301 = pd.read_csv("data\\busStation\\busStation202301.csv", encoding='euc-kr')
df_BusStation2302 = pd.read_csv("data\\busStation\\busStation202302.csv", encoding='euc-kr')
df_BusStation2303 = pd.read_csv("data\\busStation\\busStation202303.csv", encoding='euc-kr')
df_BusStation2304 = pd.read_csv("data\\busStation\\busStation202304.csv", encoding='euc-kr')


df_subway_202301 = pd.read_csv("data\subway\subway202301.csv", encoding='utf-8')
df_subway_202302 = pd.read_csv("data\subway\subway202302.csv", encoding='utf-8')
df_subway_202303 = pd.read_csv("data\subway\subway202303.csv", encoding='utf-8')
df_subway_202304 = pd.read_csv("data\subway\subway202304.csv", encoding='utf-8')
df_subway_2022 = pd.read_csv("data\subway\subway2022.csv", encoding='utf-8')
df_final_subway_station = pd.read_csv("data\\final_data\\final_subway_station.csv", encoding='utf-8')
