"""
The code below would import the libraries necessary for this project.
"""
from ucimlrepo import fetch_ucirepo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Load the Iranian Churn dataset
iranian_churn = fetch_ucirepo(id=563)
X = iranian_churn.data.features
y = iranian_churn.data.targets

# Concatenate features and targets into Pandas DataFrame
churn_df = pd.concat([X, y], axis=1, ignore_index=False)
print(churn_df.head(5))

# Rename and display all columns of the dataframe
churn_df = churn_df.rename(columns={
    "Call  Failure": "call_failure", "Complains": "complains", "Subscription  Length": "subs_len", "Charge  Amount": "charge_amount",
    "Seconds of Use": "seconds_of_use", "Frequency of use": "freq_of_use", "Frequency of SMS": "freq_of_sms", "Distinct Called Numbers": "distinct_call_nums",
    "Age Group": "age_group", "Tariff Plan": "tariff_plan", "Status": "status", "Age": "age", "Customer Value": "customer_value"})
print(churn_df.columns)

"""
Exploratory Data Analysis
"""
# Get a tuple representing the dimensionality of the dataframe
print(churn_df.shape)

# Displays the rows, columns, data types and memory used by the dataframe
print(churn_df.info())

# Displays summary statistics for each numerical column in the dataframe
print(churn_df.describe())

# Checks the sum of missing values for each column
print(churn_df.isnull().sum())

#Checks the number of unique values for each column
print(churn_df.nunique())

# Bar Plot for evaluating the count of the class label with its rate.
churn_counts = churn_df['Churn'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(churn_counts.index, churn_counts, color='skyblue')
plt.title('Count Plot of Churn')
plt.xlabel('Churn')
plt.ylabel('Count')
plt.show()

# Calculate and display the correlation matrix
plt.figure(figsize=(15, 10))
sns.heatmap(churn_df.corr(), annot=True, fmt='.2f', cmap='Pastel2', linewidths=2)
plt.title('Correlation Heatmap')
plt.show()