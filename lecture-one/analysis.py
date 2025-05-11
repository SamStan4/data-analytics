import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# This loads the csv into RAM from disk
sales: pd.DataFrame = pd.read_csv(
  filepath_or_buffer="./data/sales_data.csv",
  parse_dates=["Date"]
)

# this prints the head of the data frame
# print(sales.head())

# tells us how many rows and how many columns we are dealing with
# returns tuple (rows, columns)
# print(sales.shape)

# tells us the column labels
# even tells us what data type to use to store them which is cool
# print(sales.info())

# performes statistical analysis on the data...
# mean median mode type of things
# print(sales.describe())

# This performes an analysis on a single column in the data set
# sales_unit_cost_analysis: pd.Series = sales["Unit_Cost"].describe()

# print(sales_unit_cost_analysis)

# sales_unit_cost_plot = sales["Unit_Cost"].plot(
#   kind="box",
#   vert=False,
#   figsize=(14, 6)
# )

# plt.title("Box Plot of Unit Cost")
# plt.xlabel("Unit Cost")
# plt.tight_layout()
# plt.savefig("unit_cost_boxplot.png")

sales_unit_cost_density_plot = sales["Unit_Cost"].plot(
  kind="density",
  figsize=(14, 6)
)

plt.title("Density Plot of Unit Cost")
plt.xlabel("Unit Cost")
plt.tight_layout()
plt.savefig("unit_cost_density.png")