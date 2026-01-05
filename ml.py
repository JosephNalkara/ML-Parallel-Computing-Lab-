from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.model_selection import LeaveOneOut, LeavePOut
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
import numpy as np
# Load dataset
data = load_iris()
X = data.data
y = data.target
model = LogisticRegression(max_iter=200)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)

print("Hold-Out Accuracy:", accuracy)
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(model, X, y, cv=kfold)

print("K-Fold Scores:", scores)
print("Average Accuracy:", scores.mean())
skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(model, X, y, cv=skfold)

print("Stratified K-Fold Scores:", scores)
print("Average Accuracy:", scores.mean())
loo = LeaveOneOut()

scores = cross_val_score(model, X, y, cv=loo)

print("Leave-One-Out Accuracy:", scores.mean())
lpo = LeavePOut(p=2)

scores = cross_val_score(model, X, y, cv=lpo)

print("Leave-P-Out Accuracy:", scores.mean())
