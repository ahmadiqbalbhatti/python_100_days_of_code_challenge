# data =[]
# with open("weather_data.csv", mode="r") as file:
#     while True:
#         data_item = file.readline()
#         if not data_item:
#             break
#         data.append(data_item)
#
# for item in data:
#     print(item)
import csv

#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if not row[1].__contains__("temp"):
#             temperatures.append(int(row[1]))
#     print(temperatures)

# conda install pandas

import pandas as pd

data = pd.read_csv("weather_data.csv")
#
# print(data)
#
# print(type(data["temp"]))
# print(data["day"])

data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].tolist()
print(temp_list)

# data_dict = data.to_dict()
# print(data_dict)
# print(data)
# # never use white spaces in the csv file while creating by your own. Means don't try to formate in your own way.
# # it won't work.
# print(f'\n{data_dict["temp"]}')
# # temp_list = data.__getitem__("temp")
# # print(temp_list)



# df = pd.DataFrame([
#     ['James', '1/1/2014', '1000'],
#     ['Michelina', '2/1/2014', '12000'],
#     ['Marc', '3/1/2014', '36000'],
#     ['Bob', '4/1/2014', '15000'],
#     ['Helena', '4/1/2014', '12000']],
#     columns=['Name', 'DOB', 'Salary'])
#
# print(df)
#
# print(df["DOB"])
