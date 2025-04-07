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

"""
Explore: Which age groups send more SMS messages than make phone calls?
"""
# Calculate the total SMS and call frequency per age group
freq_sms = churn_df.groupby('age_group')['freq_of_sms'].sum()
freq_calls = churn_df.groupby('age_group')['freq_of_use'].sum()

# List to store the age groups that send more SMS than make calls
sends_more_sms = []

# Iterate over each unique age group
for group in churn_df['age_group'].unique():
    if freq_sms[group] > freq_calls[group]:
        sends_more_sms.append(group.item())

# Output the result
print("These age groups send more SMS messages than make phone calls:\n", sends_more_sms)

"""
Visualize: Create a plot visualizing the number of distinct phone calls by age group. Within the chart, differentiate between short, medium, and long calls (by the number of seconds).
"""
# Calculate mean of 'seconds_of_use' to differentiate short, medium, and long calls
mean_use = churn_df['seconds_of_use'].mean()

# Function to categorize the call duration
def get_call_rate(value):
    if value < mean_use:
        return 'low'  # short call
    elif mean_use <= value < churn_df['seconds_of_use'].max():
        return 'medium'  # medium-length call
    else:
        return 'high'  # long call

# Apply the function to the 'seconds_of_use' column
churn_df['call_duration'] = churn_df['seconds_of_use'].apply(get_call_rate)

# Group data by 'age_group' and 'call_duration' (after applying the 'get_call_rate' function)
phone_calls_grouped = churn_df.groupby(['age_group', 'call_duration']).size().unstack()

# Define colors for different call durations
colors = {'low': 'green', 'medium': 'orange', 'high': 'red'}

# Plot the stacked bar chart
phone_calls_grouped.plot(kind='bar', stacked=True, cmap='viridis', legend=False)
plt.xlabel('Age Group')
plt.ylabel('Number of Distinct Phone Calls')
plt.title('Number of Distinct Phone Calls by Age Group')
plt.legend(colors.keys(), title='Call Duration')
plt.tight_layout()
plt.show()

"""
Analyze: Are there significant differences between the length of phone calls between different tariff plans?
"""
# Create a barplot to compare call durations across tariff plans
churn_df.groupby('tariff_plan')['seconds_of_use'].mean().plot.bar()
plt.title('Call Duration Distribution by Tariff Plan')
plt.xlabel('Tariff Plan')
plt.ylabel('Call Duration (Seconds)')
plt.show()

# Based on the exploratory analysis, we can conclude that the difference between the average call duration for the "Pay As You Go" and "Contractual" tariff plans is significant.
# As a result, the average call length is considerably higher in the premium tariff plan.