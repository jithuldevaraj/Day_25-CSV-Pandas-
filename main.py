# 190 Reading CSV Data in Python

# with open("./weather_data.csv", mode="r") as weather_data:
#     weather_list = weather_data.readlines()  # convert to list ['day,temp,condition\n', .....]
#     print(weather_list)
#     print(weather_list[0].strip())  # Returns a trimmed version of the string


import csv
with open("./weather_data.csv", mode="r") as weather_date:
    # we can loop this data 👇.
    data = csv.reader(weather_date)  # convert weather_data.csv file to an Object. (<_csv.reader object at 0x...F7520>)
    temperature = []
    for row in data:  # row :- ['Monday', '12', 'Sunny'] ....
        if row[1] != "temp":
            temperature.append(row[1])
    print(temperature)
