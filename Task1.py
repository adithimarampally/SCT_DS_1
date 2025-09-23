import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Step 1: Load the dataset

# Skip metadata rows (first 4)
data = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_581007.csv", skiprows=4)


#  Reshape the data

# Convert from wide format (years as columns) to long format
data_melted = data.melt(
    id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
    var_name="Year",
    value_name="Population"
)

# Drop missing values and fix datatypes
data_melted = data_melted.dropna(subset=["Population"])
data_melted["Year"] = data_melted["Year"].astype(int)


# Histogram

pop_2020 = data_melted[data_melted["Year"] == 2020]

plt.figure(figsize=(8,5))
sns.histplot(pop_2020["Population"], bins=30, kde=True, color="skyblue")
plt.title("Distribution of Country Populations in 2020")
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.show()
# Step 4: Bar Chart (Top 10 populated countries in 2020)
# -----------------------------
top10_2020 = pop_2020.sort_values(by="Population", ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x="Population", y="Country Name", data=top10_2020, palette="viridis")
plt.title("Top 10 Most Populated Countries (2020)")
plt.xlabel("Population")
plt.ylabel("Country")
plt.show()