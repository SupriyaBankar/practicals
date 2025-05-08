import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix, ConfusionMatrixDisplay,
    accuracy_score, classification_report
)

# Load data
df = pd.read_csv('Social_Network.csv')

# Features and target
x = df[['Age', 'EstimatedSalary']]
y = df['purchased']

# Normalize features
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)

# Split into training and testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=0)

# Visualize target distribution
sns.countplot(x=y)
plt.title("Purchased Class Distribution")
plt.show()

# Train Logistic Regression model
classifier = LogisticRegression()
classifier.fit(x_train, y_train)

# Predict on test data
y_pred = classifier.predict(x_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classifier.classes_)
disp.plot(cmap='Blues')
plt.title("Confusion Matrix")
plt.show()

# Accuracy and classification report
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Scatter plot of Age vs Salary colored by target
plt.scatter(x['Age'], x['EstimatedSalary'], c=y, cmap='bwr')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.title('Customer Distribution by Purchase')
plt.show()

# Predict new samples
new1 = [[26, 34000]]
new2 = [[57, 138000]]
print("Prediction for [26, 34000]:", classifier.predict(scaler.transform(new1)))
print("Prediction for [57, 138000]:", classifier.predict(scaler.transform(new2)))
