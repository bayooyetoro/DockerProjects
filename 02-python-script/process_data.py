import pandas as pd

data = {
    "Customer_ID": [1001, 1002, 1003, 1004, 1005],
    "Customer_Name": ["John Doe", "Jane Smith", "Michael Brown", "Emily Davis", "Robert Wilson"],
    "Account_Type": ["Savings", "Checking", "Savings", "Checking", "Savings"],
    "Account_Balance": [12500.75, 3420.50, 9800.00, 150.25, 22000.90],
    "Currency": ["USD", "USD", "USD", "USD", "USD"],
    "Branch": ["New York", "Chicago", "San Francisco", "Boston", "Seattle"],
    "Account_Status": ["Active", "Active", "Inactive", "Active", "Active"]
}

df = pd.DataFrame(data)

df.to_csv("data/bank_customers.csv", index=False)

print(df)
