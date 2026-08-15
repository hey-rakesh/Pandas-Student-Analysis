
import pandas as pd

df = pd.read_csv(r"D:\Liberary\practice\Pandas_1\pd_revision\data_clean\cleaned_students.csv", encoding="UTF-8")
# print(df.head())

print(df.shape)
print(df["department"].value_counts())
print(df["city"].value_counts())
print(df["marks"].mean())
print(df["marks"].max())
print(df["attendance"].mean())
print(df["salary"].mean())


print(df[df["placement"] == "Placed"].shape[0])
print(df[df["placement"] == "Not Placed"].shape[0])


print(df[df["marks"]>80])
print(df[df["attendance"]>90])
print(df[df["department"]=="AIML"])
print(df[df["internship"]=="Yes"])

print(df[(df["marks"]>80) & (df["attendance"]>90)])
print(df[(df["department"]=="AIML") | (df["department"]=="CSE")])

print(df[(df["city"]=="Indore") | (df["city"]=="Bhopal")])


print(df.groupby("city")["marks"].mean().round(2))
print(df.groupby("department")["marks"].mean().round(2))
print(df.groupby("city")["marks"].max())
print(df.groupby("department")["marks"].max())
print(df.groupby("city")["name"].count())
print(df.groupby("department")["name"].count())
print(df.groupby("city")["salary"].mean().round(2))
print(df.groupby("department")["salary"].mean().round(2))


city_avg_marks = df.groupby("city")["marks"].mean()
# print(city_avg_marks.nlargest(1))

dept_avg_marks = df.groupby("department")["marks"].mean()
# print(dept_avg_marks.nlargest(1))

topper = df.nlargest(1, "marks")["name"].iloc[0]
# print(topper)

high_salary = df.nlargest(1, "salary")["name"].iloc[0]
# print(high_salary)

city_Avg_Salary = df.groupby("city")["salary"].mean()
# print(city_Avg_Salary.nlargest(1))

dept_high_Avg_Salary = df.groupby("department")["salary"].mean()
# print(dept_high_Avg_Salary.nlargest(1))




top_5_Stds_marks = df.nlargest(5, "marks")[["name", "marks"]]
# print(top_5_Stds_marks)

bottom_5_Stds_marks = df.nsmallest(5, "marks")[["name", "marks"]]
# print(bottom_5_Stds_marks)

top_5_stds_salary = df.nlargest(5, "salary")[["name", "salary"]]
# print(top_5_stds_salary)

high_Stds_attend = df.nlargest(1, "attendance")[["name", "attendance"]]
# print(high_Stds_attend)

placed_Stds = df[df["placement"]=="Placed"]
# print(placed_Stds)
avg_marks_placed = placed_Stds["marks"].mean()
# print(avg_marks_placed)

not_placed_Stds = df[df["placement"]=="Not Placed"]
avg_marks_not_placed = not_placed_Stds["marks"].mean()
# print(avg_marks_not_placed)

intern_stds = df[df["internship"]=="Yes"]
avg_marks_inter = intern_stds["marks"].mean()
# print(avg_marks_inter)

result = df.groupby("city").filter(lambda x: len(x) >= 5).groupby("city")["marks"].mean()

print(result)