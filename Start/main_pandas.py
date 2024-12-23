import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()  # convert DataFrame to dictionary

total_temperature = 0
for temp in data_dict["temp"]:  # looping temperature columns
    total_temperature += data_dict["temp"][temp]  # add each temperature

average = total_temperature / len(data_dict["temp"])  # finding Average
print(f"[method 1] Average Temperature : {average}")

# OR
print(f"[method 2] Average Temperature : {data['temp'].mean()}")  # Use .mean() function. 
