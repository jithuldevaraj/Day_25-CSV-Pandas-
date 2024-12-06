import pandas

data_dict = {"Name": ["Jithu", "Christy", "Manoge"],
             "Age": [28, 22, 34]}

data = pandas.DataFrame(data_dict)  # Convert dictionary to DataFrame
data.to_csv("./data_csv.csv")  # Convert DataFrame to csv file and create .csv file
