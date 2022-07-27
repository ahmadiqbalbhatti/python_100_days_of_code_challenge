import pandas as pd

# first  we will test series

array = [1, 3, 5, 2, 6]

# print(array)
# # array to series
# series = pd.Series(array, index=['a', 'b', 'c', 'd', 'e'])
# print(series)
# print(series[3])


# dictionary to series

# calories = {"day1": 420, "day2": 380, "day3": 390, "day4": 520, "day5": 280, "day6": 310}
# print(calories)
# print(type(calories))
# calories_series = pd.Series(calories)
# print(calories_series)


# series to data frame

# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }
#
# print(data)
#
# df = pd.DataFrame(data)
# print(df)
#
# print(df.loc[[0,1]])
#
# # lets label our data frame
# df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
#
# print(df)

data = pd.read_csv("weather_data.csv")
# print(data)
#
# print(f'max rows in df = {pd.options.display.max_rows}')
# print(data.info())
#
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].tolist()
# print(temp_list)
#
# average = sum(temp_list)/len(temp_list)
# print(average.__format__(".4f"))

# print(data["temp"].tolist())
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].mode())
# print(data["temp"].median())
# print(data.day)
# print(data[data.day == "Friday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday)
# print(monday.condition)
#
# temp = data[data.temp == data.temp.max()]
# max_temp = int(temp.temp)
# print(max_temp*(9/5) + 32)


# How to create a Data frame

data_dict = {
    "Roll#": [1, 2, 3, 4, 5],
    "Students": ["Ahmed", "Umair", "Uzair", "Saba", "Eman"],
    "Scores": [19, 21, 15, 12,14],
    "%": [80, 84, 60, 56, 59]


}

print(data_dict)

dataframe = pd.DataFrame(data_dict)
print(dataframe)

dataframe.to_csv("new_data.csv")

