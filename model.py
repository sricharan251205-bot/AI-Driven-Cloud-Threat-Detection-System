import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("dataset.csv")

X = data[['cpu','login_attempts','traffic']]
y = data['attack']

model = DecisionTreeClassifier()
model.fit(X,y)

def predict_threat(cpu,login,traffic):
    
    result = model.predict([[cpu,login,traffic]])
    
    return result[0]