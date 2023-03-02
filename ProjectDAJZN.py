import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


dataset = pd.read_excel(r"C:\Users\65873\Downloads\APPLIED SCRIPTING USING PYTHON PROJECT\Project_File.xlsx")



# dimension of dataset
dataset_dim = dataset.shape

# renaming the first column to date
dataset_new = dataset.rename(columns={dataset.columns[0]:'year_month'})
print(dataset_new)

# split the year_month to year and month columns
dataset_new["year"] = dataset_new["year_month"].str.split().str[0]
dataset_new["month"] = dataset_new["year_month"].str.split().str[1]

print(dataset_new)

# creating asian region
region_df = dataset_new[['year', ' Brunei Darussalam ', ' Indonesia ', ' Malaysia ',
       ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',
       ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ',
       ' Pakistan ', ' Sri Lanka ']]

# casting it to integer
region_df = region_df.astype({'year':'int'})

# filtering to the selected year from 1998 to 2007
years_dataset = region_df[(region_df["year"] >= 1998) & (region_df["year"] <= 2007)]

years_dataset = years_dataset.astype('int')

print(years_dataset.dtypes)


# sum of the years
total_df = years_dataset.sum()

print(total_df)

# removing the unneeded year column
total_df = total_df.drop('year', axis = 0)

print(total_df)
# plotting of the graph
ps = total_df[:].sort_values()
index = np.arange(len(ps.index))
plt.xlabel("Country")
plt.ylabel("total sum")
plt.xticks(index, ps.index, fontsize=10, rotation=90)
plt.title("sum of visitor by country")
plt.bar(ps.index, ps.values)
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.show()


# top 3 of the finalised data
total_df = total_df.sort_values(ascending=False)
print(total_df.head(3))

#Hi