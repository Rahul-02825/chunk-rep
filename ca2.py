import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score, roc_auc_score, roc_curve, auc
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
import missingno as mn
def preprocess_data(input_file, output_file):

  df = pd.read_csv(input_file)

  # Remove rows with '?'
  df = df.replace('?', pd.NA)

  mn.matrix(df)

  df=df.dropna()

  # Replace unique values with numbers for each column
  for column in df.columns:
    unique_values = df[column].unique()
    mapping = {value: i for i, value in enumerate(unique_values)}
    df[column] = df[column].map(mapping)

  # Label the first column with ranges
  first_column = df.columns[0]
  min_val = df[first_column].min()
  max_val = df[first_column].max()
  range_size = (max_val - min_val) // 10  # Adjust range size as needed

  if range_size > 0:
    bins = [min_val + i * range_size for i in range(6)]
    labels = list(range(1, 6))
    df[first_column] = pd.cut(df[first_column], bins=bins, labels=labels, include_lowest=True)


  df.to_csv(output_file, index=False)


# Example usage
input_file = "/content/adult.csv"  # Replace with your input file path
output_file = '/content/modified_adult.csv'  # Replace with your desired output file path
preprocess_data(input_file, output_file)

# Load the CSV file
data = pd.read_csv(r"/content/modified_adult.csv")  # Replace 'your_file.csv' with your file name

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Display the correlation matrix
print(correlation_matrix["target_variable"])
# Handle null values (replace with mean, median, or remove rows/columns)
# Example: Fill null values with the mean of the column
data.fillna(data.mean(), inplace=True)

# X = data[['age']]
# X = data[['age','gender']]
# X = data[['age','gender','course']]
# X = data[['age','gender','course','color']]
X = data[['age','gender','course','color','expertise']]
y = data['target_variable']

smote = SMOTE(random_state=42)
X, y = smote.fit_resample(X, y)

# Normalize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# SVM
svm_model = SVC(kernel='linear', C=1.0)  # You can change kernel and C parameter
svm_model.fit(X_train, y_train)
svm_y_pred = svm_model.predict(X_test)
print(len(y_test[y_test==0])," - ",len(y_test))
print(len(svm_y_pred[svm_y_pred==0])," - ",len(svm_y_pred))
cm = confusion_matrix(y_test, svm_y_pred)
print(cm)
svm_f1 = f1_score(y_test, svm_y_pred)
svm_auc = roc_auc_score(y_test, svm_y_pred)

# KNN
knn_model = KNeighborsClassifier(n_neighbors=5)  # You can change n_neighbors parameter
knn_model.fit(X_train, y_train)
knn_y_pred = knn_model.predict(X_test)
print(len(y_test[y_test==0])," - ",len(y_test))
print(len(knn_y_pred[knn_y_pred==0])," - ",len(knn_y_pred))
cm = confusion_matrix(y_test, knn_y_pred)
print(cm)
knn_f1 = f1_score(y_test, knn_y_pred)
knn_auc = roc_auc_score(y_test, knn_y_pred)

# Decision Tree
dt_model = DecisionTreeClassifier(max_depth=5)  # You can change max_depth parameter
dt_model.fit(X_train, y_train)
dt_y_pred = dt_model.predict(X_test)
print(len(y_test[y_test==0])," - ",len(y_test))
print(len(dt_y_pred[dt_y_pred==0])," - ",len(dt_y_pred))
cm = confusion_matrix(y_test, dt_y_pred)
print(cm)
dt_f1 = f1_score(y_test, dt_y_pred)
dt_auc = roc_auc_score(y_test, dt_y_pred)

# Naive Bayes
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
nb_y_pred = nb_model.predict(X_test)
print(len(y_test[y_test==0])," - ",len(y_test))
print(len(nb_y_pred[nb_y_pred==0])," - ",len(nb_y_pred))
cm = confusion_matrix(y_test, nb_y_pred)
print(cm)
nb_f1 = f1_score(y_test, nb_y_pred)
nb_auc = roc_auc_score(y_test, nb_y_pred)


# Plotting F1 Score
plt.figure(figsize=(8, 6))
plt.bar(['SVM', 'KNN', 'Decision Tree', 'Naive Bayes'], [svm_f1, knn_f1, dt_f1, nb_f1])
plt.title('F1 Score Comparison')
plt.xlabel('Algorithm')
plt.ylabel('F1 Score')
plt.show()

# Plotting AUC
plt.figure(figsize=(8, 6))
plt.bar(['SVM', 'KNN', 'Decision Tree', 'Naive Bayes'], [svm_auc, knn_auc, dt_auc, nb_auc])
plt.title('AUC Score Comparison')
plt.xlabel('Algorithm')
plt.ylabel('AUC Score')
plt.show()

# Plotting ROC Curve (Example for SVM)
fpr, tpr, thresholds = roc_curve(y_test, svm_y_pred)
roc_auc = auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (SVM)')
plt.legend(loc="lower right")
plt.show()

# Plotting ROC Curve (Example for KNN)
fpr, tpr, thresholds = roc_curve(y_test, knn_y_pred)
roc_auc = auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (RNN)')
plt.legend(loc="lower right")
plt.show()

# Plotting ROC Curve (Example for Decision tree)
fpr, tpr, thresholds = roc_curve(y_test, dt_y_pred)
roc_auc = auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (DT)')
plt.legend(loc="lower right")
plt.show()

# Plotting ROC Curve (Example for Naive Bayes)
fpr, tpr, thresholds = roc_curve(y_test, nb_y_pred)
roc_auc = auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (NB)')
plt.legend(loc="lower right")
plt.show()
