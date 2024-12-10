import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")  # csv -> DataFrame
data_fur_color_row = data["Primary Fur Color"]  # DataFrame -> <class 'pandas.core.series.Series'>
fur_color_list = data_fur_color_row.to_list()  # Series -> List

color_of_squirrel = {"Fur Color": ["Gray", "red", "black"],
                     "Count": [0, 0, 0]}
for color in fur_color_list:  # appending the color count to the Dictionary.
    if color == "Gray":
        color_of_squirrel["Count"][0] += 1

    elif color == "Cinnamon":
        color_of_squirrel["Count"][1] += 1

    elif color == "Black":
        color_of_squirrel["Count"][2] += 1

# print(f"Gray : {color_of_squirrel['Count'][0]}")
# print(f"Red : {color_of_squirrel['Count'][1]}")
# print(f"Black : {color_of_squirrel['Count'][2]}")

# Constructing Data Frame
# Convert dictionary to DataFrame
squirrel_color_DataFrame = pandas.DataFrame(color_of_squirrel)

# Save DataFrame to a CSV file
squirrel_color_DataFrame.to_csv("./squirrel_count.csv")

