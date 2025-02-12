import pandas as pd
from ucimlrepo import fetch_ucirepo

# fetch dataset
iranian_churn = fetch_ucirepo(id=563)

# data (as pandas dataframes)
X = iranian_churn.data.features
y = iranian_churn.data.targets

# metadata
print(iranian_churn.metadata)

# variable information
print(iranian_churn.variables)