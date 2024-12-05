import pandas

data = pandas.read_csv("weather_data.csv")  # convert to an object <class 'pandas.core.frame.DataFrame'>

# Get data in columns
print(data["condition"])  # Treating it as a dictionary
print(data.condition)  # Treating it as an Object

# Get data in Row
print(data[data.day == "Monday"])
print(data[data.temp == 14])
print(data[data.condition == "Sunny"])

print(data[data.temp == data.temp.max()])  # filter the column by condition

