import pandas as pd

df = pd.read_csv("data/customer_churn.csv")
df.head()

# =====



# =====

df["Churn"].value_counts()

# =====

df.info()

# =====

df.shape

# =====

df.columns

# =====

df.isnull().sum()

# =====

df["Churn"].value_counts()

# =====

df["Churn"].value_counts(normalize=True) * 100


# =====

df["Contract"].unique()

# =====

df.dtypes

# =====

print("hib")

# =====

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# =====

df.isnull().sum()

# =====

df = df.dropna()

# =====

df = df.drop("customerID", axis=1)

# =====

df.info()

# =====

import matplotlib.pyplot as plt
import seaborn as sns

# =====

sns.countplot(x="Churn", data=df)
plt.title("Customer Churn Count")
plt.show()

# =====

sns.countplot(x="Contract", hue="Churn", data=df)
plt.title("Contract Type vs Churn")
plt.xticks(rotation=15)
plt.show()

# =====

sns.countplot(x="InternetService", hue="Churn", data=df)
plt.title("Internet Service vs Churn")
plt.show()

# =====

plt.figure(figsize=(8,5))
sns.histplot(df["MonthlyCharges"], bins=30, kde=True)
plt.title("Monthly Charges Distribution")
plt.show()

# =====

plt.figure(figsize=(8,5))
sns.histplot(df["MonthlyCharges"], bins=30, kde=True)
plt.title("Monthly Charges Distribution")
plt.show()

# =====

plt.figure(figsize=(8,5))
sns.boxplot(x="Churn", y="MonthlyCharges", data=df)
plt.title("Monthly Charges vs Churn")
plt.show()

# =====

plt.figure(figsize=(8,5))
sns.boxplot(x="Churn", y="tenure", data=df)
plt.title("Tenure vs Churn")
plt.show()

# =====

X = df.drop("Churn", axis=1)
y = df["Churn"]
y = y.map({"No": 0, "Yes": 1})
X = pd.get_dummies(X, drop_first=True)

# =====

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# =====

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# =====

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# =====

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# =====

model = LogisticRegression(max_iter=1000)

# =====

model.fit(X_train, y_train)

# =====

y_pred = model.predict(X_test)

# =====

print(y_pred[:10])

# =====

acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.4f}")