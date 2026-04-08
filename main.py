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
#        "Age":[30, 35, 50]
#}

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

# CSV Example:
# df = pd.read_csv("OG_Pokemon_database.csv")

# JSON Example:
# df = pd.read_json("")
# print(df)

# To print entire data frame and not a truncated version do as follows:
# just add .to_string() at the end
# print(df.to_string())

# Selection

# df = pd.read_csv("OG_Pokemon_database.csv")

# Selection by Column/s

# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())

# To Select multiple lists:
# print(df[["Name","Height","Weight"]].to_string())

# Selection by Row/s
# df = pd.read_csv("OG_Pokemon_database.csv", index_col="Name")
# print(df.loc["Pikachu"])

# If you do not want all the data then do as follows:
#    Pass in a second argument or a Python list of what
#    you want to display
# print(df.loc["Charizard",["Height", "Weight"]])

# You can select a bunch of rows as well by using a :
# print(df.loc["Charizard":"Blastoise",["Height", "Weight"]])

# You can use integer based indexing:
# print(df.iloc[0:11])
# for every other row add another :
# print(df.iloc[0:11:2])

# Select indices of what columns you would like
# print(df.iloc[0:11:2, 0:3])

# Simple Exercise:
"""
df = pd.read_csv("OG_Pokemon_database.csv", index_col="Name")
pokemon = input("Enter a Pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")
"""

# Filtering = Keeping the rows that match a condition

# df = pd.read_csv("OG_Pokemon_database.csv")

# Examples:
#
# Filter Pokemon that is 2 meters or above:
# tall_pokemon = df[df["Height"] >= 2]
# print(tall_pokemon)
#
# Filter heavy Pokemon:
# heavy_pokemon = df[df["Weight"] > 100 ]
# print(heavy_pokemon)
#
# Filtering Legendary Pokemon:
# legendary_pokemon = df[df["Legendary"] == True]
# print(legendary_pokemon)
#
# Filter with the or ( | ) operator:
# water_pokemon = df[(df["Type1"] == "Water") |
#                   (df["Type2"] == "Water")]
# print(water_pokemon)
#
# Filter with the and operator:
# ff_pokemon = df[(df["Type1"] == "Fire") &
#                (df["Type2"] == "Flying")]
# print(ff_pokemon)


# Aggregation
# Aggregate functions = Reduces a set of values into a single summary value
#                       Used to summarize and analyze data
#                       Often used with the groupby() function

# df = pd.read_csv("OG_Pokemon_database.csv")

# Functions that apply to whole Dataframe
# Mean
# print(df.mean(numeric_only = True))

# Sum
# print(df.sum(numeric_only = True))

# Minimum
# print(df.min(numeric_only=True))

# Maximum
# print(df.max(numeric_only=True))

# Count
# print(df.count())


# Functions for a Single column
#print(df["Height"].mean())
#print(df["Height"].sum())
#print(df["Height"].min())
#print(df["Height"].max())
#print(df["Type2"].count())

# groupby() function: Arranging dataframe into different goups
#                     We can do this if they have something in common

# group = df.groupby("Type1")

#print(group["Height"].mean())
#print(group["Height"].sum())
#print(group["Height"].min())
#print(group["Height"].max())
#print(group["Height"].count())

# Data Cleaning = the process of fixing/removing:
#                 incomplete,incorrect, or irrelevant data
#                 ~75% of work done with Pandas is data cleaning

df = pd.read_csv("OG_Pokemon_database.csv")

# 1. Drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])

# 2. Handle missing data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2": "None"})

# 3. Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                    "Fire": "FIRE",
#                                   "Water": "WATER"})

# 4. Standardize text
# df["Name"] = df["Name"].str.lower()

# 5. Fix data types
# df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicate values
#df = df.drop_duplicates()

#print(df.to_string())