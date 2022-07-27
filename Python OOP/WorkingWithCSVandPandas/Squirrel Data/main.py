import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# data_series = data["Primary Fur Color"]
# gray_count = len(data[data_series == "Gray"])
# cinnamon_count = len(data[data_series == "Cinnamon"])
# black_count = len(data[data_series == "Black"])
# print(data)
#
# print(data[data_series == "Red"])
# print(gray_count)
# print(cinnamon_count)
#
# data_dict = {
#     # ["Fur Color", "Count"],
#     # ["Gray", gray_count],
#
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_count, cinnamon_count, black_count],
# }
#
# print(data_dict)
#
# dict_dataframe = pandas.DataFrame(data_dict)
# print(dict_dataframe)
#
# dict_dataframe.to_csv("new_squirrel_data_color_count.csv")


adults = len(data[data.Age == "Adult"])
juveniles = len(data[data.Age == "Juvenile"])
# empties = len(data[data.Age] == "")

print(adults)
print(juveniles)
# print(empties)

# print(adults+juveniles)
