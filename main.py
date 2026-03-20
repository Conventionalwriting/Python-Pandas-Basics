import pandas as pd

# Series = A Pandas 1-Dimensional labeled aray that can hold any data type
#          Like a single column in excel or like an appartment floor with many rooms

#    Basic Example:
# data_1 = [100, 205,300]
# series_1 = pd.Series(data_1)
# print(series_1)

# Can also use Booleans, strings, and floating point numbers too
#   Examples:
#        data = [China, Brazil, Germany]
#        data = [True, False, True]
#        data = [102.5,100.9,209.1]

# Setting an custom index by adding an keyword argument called index:
# data_2 = ["Mark Ruffle","John Layne", "Laura Epson"]
# series_2 = pd.Series(data_2, index=["Room 102:","Room 106:", "Room 208:"])
# print(series_2)

# If needed to access data within series use the .loc (location by label) property
# print(series_2.loc["Room 208:"])

# Note: if label does not exist you get a key error
# To update one of the values you need to use also the loc property but in this way
# series_2.loc["Room 208:"] = "Jonathon Taylor"
# print(series_2)

# Locate by integer position through .iloc(location by integer)
# print(series_2.iloc[0])
# print(series_2.iloc[1])
# print(series_2.iloc[2])

# Filter by values
#data_3 = [100, 102, 150, 200, 206, 250]
#series_3 = pd.Series(data_3, index = ["a","b","c","d","e","f"])
#print(series_3[series_3 > 100])
#print(series_3[series_3 <150])
#print(series_3[series_3 >= 206])
#print(series_3[series_3 <= 200])

# Using a dictionary instead of a list and applying my learning
"""
meters_run = {"Day 1": 100, "Day 2": 200, "Day 3": 500}
series_4 = pd.Series(meters_run)
print("Printing Series")
print(series_4)
print("")
print("Using .loc property")
print(series_4.loc["Day 1"])
print("")
print("Using .iloc property")
print(series_4.iloc[2])
print("")
print("Filtering by values")
print("Greater than")
print(series_4[series_4 > 100])
print("Less than")
print(series_4[series_4 < 500])
print("Greater than 'or' equal")
print(series_4[series_4 >= 200])
print("Less than 'or' equal")
print(series_4[series_4 <= 500])
"""

# DataFrame = A tabular data structure with rows and Columns
#             2-Dimensional like an Excel sheet

#    Basic Example:
#data_5 = {"Name": ["Spongebob","Patrick","Squidward"],
        "Age":[30, 35, 50]
}

#df = pd.DataFrame(data_5)
#print(df)

# Indexing
#df = pd.DataFrame(data_5, index =["Employee 1","Employee 2","Employee 3"])
#print(df)

# loc property
#print(df.loc["Employee 1"])
#print(df.loc["Employee 2"])
#print(df.loc["Employee 3"])

#Select by integer location (.iloc property)
#print(df.iloc[1])
#print(df.iloc[2])

# Add new column
#df["Job"] = ["Cook","N/A","Cashier"]
#print(df)

# Add new row
# (the easiest way is to create a new dataframe and concatinate it)
#new_row = pd.DataFrame([{"Name":"Sandy","Age":28,"Job":"Engineer"}],
#                        index=["Employee 4"])
#df = pd.concat([df, new_row])
#print(df)

# Add new rows
#new_rows = pd.DataFrame([{"Name":"Sandy","Age":28,"Job":"Engineer"},
#                         {"Name":"Eugene","Age":60,"Job":"Manager"}],
#                        index=["Employee 4","Employee 5"])

#df = pd.concat([df, new_rows])
#print(df)

# Importing files: more specifically CSV(Comma-Separated values) and
# JSON(JavaScript Object Notation) files

# Selection =

# Filtering =

# Aggregation =

# Data Cleaning =