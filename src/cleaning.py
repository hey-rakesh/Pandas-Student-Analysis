
import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\Liberary\git_project\data\messy.csv", encoding="UTF-8")
# print(df.head())

# print(df.tail())
# print(df.shape)
# print(df.info())
# print(df.isnull().sum())

print(df.duplicated().sum())
print(df.drop_duplicates(inplace=True))

df.replace("?", np.nan, inplace=True)
# print(df.isnull().sum().sum())

df["name"] = df["name"].str.title()
df["name"] = df["name"].str.strip()
# print(df["name"].head(10))

df["age"] = df["age"].replace("?", np.nan)
# print(df["age"].isnull().sum())
df["age"] = pd.to_numeric(df["age"])
df["age"] = df["age"].fillna(df["age"].mean()).round().astype(int)
# print(df["age"].isnull().sum())

df["gender"] = df["gender"].str.strip()
df["gender"] = df["gender"].str.title()
# print(df["gender"])


# print(df["city"].unique())

df["city"] = df["city"].str.strip()
df["city"] = df["city"].str.title()
# df["city"] = df["city"].str.replace()

# print(df["city"].unique())


# print(df["department"].unique())
df["department"] = df["department"].str.strip()
df["department"] = df["department"].replace({"aiml":"AIML",
                                             "cse":"CSE",
                                             "ece":"ECE"})

# print(df["department"].unique())

df["internship"] = df["internship"].str.strip()
df["internship"] = df["internship"].str.title()

# print(df["internship"].unique())

df["placement"] = df["placement"].str.strip()
df["placement"] = df["placement"].str.title()

# print(df["placement"].unique())

df["marks"] = df["marks"].replace("?", np.nan)
df["marks"] = pd.to_numeric(df["marks"])
df["marks"] = df["marks"].fillna(df["marks"].mean()).round()
# print(df["marks"].isnull().sum())


df["attendance"] = df["attendance"].replace("?", np.nan)
# print(df["attendance"].isnull().sum())
df["attendance"] = df["attendance"].str.replace("%", "")
df["attendance"] = pd.to_numeric(df["attendance"])
df["attendance"] = df["attendance"].fillna(df["attendance"].mean()).round()
# print(df["attendance"].head(20))


# print(df["salary"].isnull().sum())
df["salary"] = df["salary"].replace("?", np.nan)
# print(df["salary"].isnull().sum())
df["salary"] = df["salary"].str.replace("k", "")
df["salary"] = pd.to_numeric(df["salary"]) * 1000
# print(df["salary"].head())
df["salary"] = df["salary"].fillna(df["salary"].mean()).round().astype(int)
# print(df["salary"])


df["joining_date"] = df["joining_date"].replace("?", np.nan)
# print(df["joining_date"].isnull().sum())

df["joining_date"] = pd.to_datetime(df["joining_date"], 
                                    dayfirst=False,
                                    format="mixed",
                                    errors="coerce")
# print(df["joining_date"])
 


# print(df.dtypes)
# print(df.info())


df.drop_duplicates(subset="student_id", keep="first", inplace=True)

print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nDuplicate student IDs:")
print(df["student_id"].duplicated().sum())

print("\nUnique cities:")
print(df["city"].unique())

print("\nUnique departments:")
print(df["department"].unique())

print("\nUnique gender:")
print(df["gender"].unique())

print("\nUnique internship:")
print(df["internship"].unique())

print("\nUnique placement:")
print(df["placement"].unique())

df.to_csv(r"D:\Liberary\git_project\data\clean.csv", index=False)

