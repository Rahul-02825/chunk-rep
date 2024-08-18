##1###
# Gradient descent with two independent variable
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('/content/sample_data/california_housing_train.csv')

#df.corr()["median_house_value"]

# Scale the data using RobustScaler
scaler = RobustScaler()
df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Define independent variables and the target variable
X1 = df[["median_income"]].values  # Convert to numpy array
X2 = df[["total_rooms"]].values  # Convert to numpy array
Y = df[["median_house_value"]].values  # Convert to numpy array

# Plot the data
plt.scatter(X1, Y)
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.show()

plt.scatter(X2, Y)
plt.xlabel("Total Rooms")
plt.ylabel("Median House Value")
plt.show()

# Initialize coefficients
x0 = 0
x1 = 0
x2 = 0

# Learning rate and number of epochs
L = 0.0001
epoch = 100000
m = len(Y)  # Number of samples

# Gradient Descent
for i in range(epoch):
    y_pred = x1 * X1 + x2 * X2 + x0  # Predicted values
    D0 = (-2/m) * np.sum(Y - y_pred)  # Derivative with respect to x0
    D1 = (-2/m) * np.sum((Y - y_pred) * X1)  # Derivative with respect to x1
    D2 = (-2/m) * np.sum((Y - y_pred) * X2)  # Derivative with respect to x2
    x1 = x1 - L * D1  # Update x1
    x2 = x2 - L * D2  # Update x2
    x0 = x0 - L * D0  # Update x0

# Print the final coefficients
print("x1:", x1)
print("x2:", x2)
print("x0:", x0)

test=pd.read_csv('/content/sample_data/california_housing_test.csv')
# Scale the data using RobustScaler
scaler = RobustScaler()
test = pd.DataFrame(scaler.fit_transform(test), columns=test.columns)

# Define independent variables and the target variable
X1_test = test[["median_income"]].values  # Convert to numpy array
X2_test = test[["total_rooms"]].values  # Convert to numpy array
Y_test = test[["median_house_value"]].values  # Convert to numpy array

Y_pred = x1 * X1_test + x2 * X2_test + x0  # Predicted values

mse=mean_squared_error(Y_test, Y_pred)
r2=r2_score(Y_test, Y_pred)
print("MSE:", mse)
print("R2:", r2)


# Interpreting the results:

# MSE: Lower values of MSE indicate better model performance.
# It represents the average squared difference between the predicted and actual values.

# R-squared: This value ranges from 0 to 1, with higher values indicating a better fit.
# It represents the proportion of variance in the target variable explained by the model.



##################2####################

# Gradient descent with one independent variable
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


# Load the dataset
df = pd.read_csv('/content/sample_data/california_housing_train.csv')

# Scale the data using RobustScaler
scaler = RobustScaler()
df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

#removing outliers
Q1 = df['median_house_value'].quantile(0.25)
Q3 = df['median_house_value'].quantile(0.75)
IQR = Q3 - Q1
lowerbound = Q1 - 1.5*IQR
upperbound = Q3 + 1.5*IQR
df = df[(df['median_house_value'] >= lowerbound) & (df['median_house_value'] <= upperbound)]

print(df.corr()["median_house_value"])

# Define independent variables and the target variable
X1 = df[["median_income"]].values  # Convert to numpy array
Y = df[["median_house_value"]].values  # Convert to numpy array


# Initialize coefficients
x0 = 0
x1 = 0

# Learning rate and number of epochs
L = 0.001
epoch = 10000
m = len(Y)  # Number of samples

# Gradient Descent
for i in range(epoch):
    y_pred = x1 * X1 + x0  # Predicted values
    D0 = (-2/m) * np.sum(Y - y_pred)  # Derivative with respect to x0
    D1 = (-2/m) * np.sum((Y - y_pred) * X1)  # Derivative with respect to x1
    x1 = x1 - L * D1  # Update x1
    x0 = x0 - L * D0  # Update x0

# Print the final coefficients
print("x1:", x1)
print("x0:", x0)

test=pd.read_csv('/content/sample_data/california_housing_test.csv')
# Scale the data using RobustScaler
scaler = RobustScaler()
test = pd.DataFrame(scaler.fit_transform(test), columns=test.columns)

Q1 = test['median_house_value'].quantile(0.25)
Q3 = test['median_house_value'].quantile(0.75)
IQR = Q3 - Q1
lowerbound = Q1 - 1.5*IQR
upperbound = Q3 + 1.5*IQR
test = test[(test['median_house_value'] >= lowerbound) & (test['median_house_value'] <= upperbound)]

# Define independent variables and the target variable
X1_test = test[["median_income"]].values  # Convert to numpy array
Y_test = test[["median_house_value"]].values  # Convert to numpy array

Y_pred = x1 * X1_test + x0  # Predicted values

mse=mean_squared_error(Y_test, Y_pred)
r2=r2_score(Y_test, Y_pred)
print("MSE:", mse)
print("R2:", r2)

# Plot the regression line
plt.scatter(X1, Y)
plt.plot(X1, x1 * X1 + x0, color='red')
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.show()

# Interpreting the results:

# MSE: Lower values of MSE indicate better model performance.
# It represents the average squared difference between the predicted and actual values.

# R-squared: This value ranges from 0 to 1, with higher values indicating a better fit.
# It represents the proportion of variance in the target variable explained by the model.

##############################3############################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('/content/sample_data/DIABETICS DATASET.csv')

# # Calculate the correlation matrix and get the attributes most correlated to the Outcome
# correlation_matrix = data.corr()
# correlated_features = correlation_matrix["Outcome"].abs().sort_values(ascending=False)
# top_features = correlated_features.index[1:4]  # Select top 3 features (you can adjust the number)

# # Print top features
# print(f"Top correlated features: {list(top_features)}")

top_features=['Glucose', 'BMI']

# Create feature matrix X and target vector y
X = data[top_features].values
y = data['Outcome'].values

# Under-sampling for balancing the number of zero and one outcomes
class_0 = data[data["Outcome"] == 0]
class_1 = data[data["Outcome"] == 1]
class_0 = class_0.sample(n=len(class_1), random_state=42)
data_balanced = pd.concat([class_0, class_1])

X = data_balanced[top_features].values
y = data_balanced['Outcome'].values

print(Counter(y))

# Split the data using sklearn's train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Logistic Regression Implementation ---

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Cost function (binary cross-entropy)
def cost_function(X, y, theta):
    m = len(y)
    h = sigmoid(X @ theta)
    epsilon = 1e-15  # Small constant to prevent log(0)
    cost = (1/m) * (-y.T @ np.log(h + epsilon) - (1-y).T @ np.log(1-h + epsilon))
    return cost


# Gradient descent
def gradient_descent(X, y, theta, learning_rate, num_iterations):
    m = len(y)
    cost_history = []
    for i in range(num_iterations):
        h = sigmoid(X @ theta)
        gradient = (1/m) * X.T @ (h - y)                        
        theta -= learning_rate * gradient
        cost = cost_function(X, y, theta)
        cost_history.append(cost)
    return theta, cost_history


# Add a bias term to the features
X_train = np.c_[np.ones(X_train.shape[0]), X_train]

# Initialize parameters
theta = np.zeros(X_train.shape[1])

# Set hyperparameters
learning_rate = 0.01
num_iterations = 1000

# Perform gradient descent
theta, cost_history = gradient_descent(X_train, y_train, theta, learning_rate, num_iterations)

# Print the learned parameters
print("Learned parameters (theta):", theta)

# Predicting on test set
X_test_bias = np.c_[np.ones(X_test.shape[0]), X_test]
y_predict = sigmoid(X_test_bias @ theta)
y_pred = (y_predict >= 0.5).astype(int)

print(y_pred)

# Manual confusion matrix
def confusion_matrix_manual(y_true, y_pred):
    tp = np.sum((y_true == 1) & (y_pred == 1))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    return np.array([[tn, fp], [fn, tp]])


cm = confusion_matrix_manual(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Calculate accuracy manually
accuracy = np.sum(y_test == y_pred) / len(y_test)
print("Accuracy:", accuracy)

# Plot the cost function over iterations
plt.plot(range(num_iterations), cost_history)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Cost Function Over Iterations')
plt.show()
