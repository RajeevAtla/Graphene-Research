from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dataset = loadtxt('dataset_nolabel.csv', delimiter = ",", skiprows = 1) #loads the dataset, skips the labels

X = dataset[:, 0:8] #input features
Y = dataset[:, 10] #output label - type of superconductivity

#Sanity check
#print(X)
#print(Y)

seed = 12 #used to provide a degree of reproducibility

test_size = 0.25 #train:test ratio
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = test_size, random_state = seed)

model = XGBClassifier()
model.fit(X_train, y_train)

#print(model)

y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]

#print(predictions) #sanitycheck

accuracy = accuracy_score(y_test, predictions)
print(accuracy * 100)
