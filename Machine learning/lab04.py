# %%
from sklearn import datasets
data_breast_cancer = datasets.load_breast_cancer(as_frame=True)
data_iris = datasets.load_iris(as_frame=True)
print (data_breast_cancer)


# %%
print (data_breast_cancer['DESCR'])


# %%
print (data_iris['DESCR'])

# %%
from sklearn.model_selection import train_test_split

X_cancer=data_breast_cancer.data
y_cancer=data_breast_cancer.target
X_train_cancer,X_test_cancer,y_train_cancer,y_test_cancer = train_test_split(X_cancer,y_cancer,test_size=0.2,random_state=42)

X_iris=data_iris.data
y_iris=data_iris.target
X_train_iris,X_test_iris,y_train_iris,y_test_iris = train_test_split(X_iris,y_iris,test_size=0.2,random_state=42)

# %%
from sklearn.svm import LinearSVC
X_mean_cancer= data_breast_cancer.data[['mean area', 'mean smoothness']]

X_train_mean,X_test_mean,y_train_mean,y_test_mean = train_test_split(X_mean_cancer,y_cancer,test_size=0.2,random_state=42)

model_1=LinearSVC(loss='hinge',random_state=42)
model_1.fit(X_train_mean, y_train_mean)





# %%
from sklearn.preprocessing import StandardScaler


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_mean)
X_test_scaled = scaler.transform(X_test_mean)
model_2 = LinearSVC(loss="hinge", random_state=42)
model_2.fit(X_train_scaled, y_train_mean)


# %%
lista = []
acc_train_no_scale = model_1.score(X_train_mean, y_train_mean)
acc_test_no_scale = model_1.score(X_test_mean, y_test_mean)
acc_train_scale = model_2.score(X_train_scaled, y_train_mean)
acc_test_scale = model_2.score(X_test_scaled, y_test_mean)
lista.append(acc_train_no_scale)
lista.append(acc_test_no_scale)
lista.append(acc_train_scale)
lista.append(acc_test_scale)

print(lista)

import pickle
with open('bc_acc.pkl', 'wb') as f:
    pickle.dump(lista, f)

# %%
X_iris_SVC= data_iris.data[['petal length (cm)', 'petal width (cm)']]
y_iris_virginica = (data_iris.target == 2).astype(int)
X_train_virginica,X_test_virginica,y_train_virginica,y_test_virginica = train_test_split(X_iris_SVC,y_iris_virginica,test_size=0.2,random_state=42)

model_3=LinearSVC(loss='hinge',random_state=42)
model_3.fit(X_train_virginica, y_train_virginica)

acc_train_no_scale = model_3.score(X_train_virginica, y_train_virginica)
acc_test_no_scale = model_3.score(X_test_virginica, y_test_virginica)


# %%
scaler2=StandardScaler()
X_train_scaled_iris = scaler2.fit_transform(X_train_virginica)
X_test_scaled_iris = scaler2.transform(X_test_virginica)
model_4 = LinearSVC(loss="hinge", random_state=42)
model_4.fit(X_train_scaled_iris, y_train_virginica)

# %%

acc_train_scale = model_4.score(X_train_scaled_iris, y_train_virginica)
acc_test_scale = model_4.score(X_test_scaled_iris, y_test_virginica)

iris_acc = [
    acc_train_no_scale, 
    acc_test_no_scale, 
    acc_train_scale, 
    acc_test_scale
]

import pickle
with open('iris_acc.pkl', 'wb') as f:
    pickle.dump(iris_acc, f)


# %%
import numpy as np
import pandas as pd
size = 900
X = np.random.rand(size)*5-2.5
w4, w3, w2, w1, w0 = 1, 2, 1, -4, 2
y = w4*(X**4) + w3*(X**3) + w2*(X**2) + w1*X + w0 + np.random.randn(size)*8-4
df = pd.DataFrame({'x': X, 'y': y})
df.plot.scatter(x='x',y='y')


# %%
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import LinearSVR
from sklearn.metrics import mean_squared_error
X_reshaped=X.reshape(-1,1)
X_train,X_test,y_train,y_test = train_test_split(X_reshaped,y,test_size=0.2,random_state=42)


poly_svr_pipe = Pipeline([
    ("poly_features", PolynomialFeatures(degree=4)),
    ("linear_svr", LinearSVR(random_state=42))]
)

poly_svr_pipe.fit(X_train,y_train)
mse_train_poly=mean_squared_error(y_train,poly_svr_pipe.predict(X_train))
mse_test_poly=mean_squared_error(y_test,poly_svr_pipe.predict(X_test))
print(f"LinearSVR_Poly: Train MSE = {mse_train_poly}, Test MSE = {mse_test_poly}")

# %%
from sklearn.svm import SVR
svr_poly = SVR(kernel="poly", degree=4)
svr_poly.fit(X_train, y_train)
print(f"SVR poly (default): Train MSE = {mean_squared_error(y_train, svr_poly.predict(X_train))}")

# %%
from sklearn.model_selection import GridSearchCV
param_grid = {
    "C": [0.1, 1, 10],
    "coef0": [0.1, 1, 10]
}
grid_search = GridSearchCV(SVR(kernel="poly", degree=4), param_grid, scoring='neg_mean_squared_error', cv=5)
grid_search.fit(X_reshaped, y)
print("Najlepsze parametry:", grid_search.best_params_)

best_svr = grid_search.best_estimator_
best_svr.fit(X_train,y_train)
mse_train_svr_best = mean_squared_error(y_train, best_svr.predict(X_train))
mse_test_svr_best = mean_squared_error(y_test, best_svr.predict(X_test))



reg_mse = [
    mse_train_poly, 
    mse_test_poly, 
    mse_train_svr_best, 
    mse_test_svr_best
]

with open('reg_mse.pkl', 'wb') as f:
    pickle.dump(reg_mse, f)

print(reg_mse)


import matplotlib.pyplot as plt
import numpy as np
from sklearn.inspection import DecisionBoundaryDisplay

plt.figure(figsize=(15, 18))

ax1 = plt.subplot(3, 2, 1)
ax1.set_title("Rak piersi: LinearSVC (Bez skalowania)")

DecisionBoundaryDisplay.from_estimator(
    model_1, X_train_mean, response_method="predict",
    cmap=plt.cm.coolwarm, alpha=0.3, ax=ax1, xlabel='mean area', ylabel='mean smoothness'
)
ax1.scatter(X_train_mean.iloc[:, 0], X_train_mean.iloc[:, 1], c=y_train_mean, cmap=plt.cm.coolwarm, edgecolors='k', s=20)


ax2 = plt.subplot(3, 2, 2)
ax2.set_title("Rak piersi: LinearSVC (Ze skalowaniem)")
DecisionBoundaryDisplay.from_estimator(
    model_2, X_train_scaled, response_method="predict",
    cmap=plt.cm.coolwarm, alpha=0.3, ax=ax2, xlabel='mean area (scaled)', ylabel='mean smoothness (scaled)'
)

ax2.scatter(X_train_scaled[:, 0], X_train_scaled[:, 1], c=y_train_mean, cmap=plt.cm.coolwarm, edgecolors='k', s=20)


ax3 = plt.subplot(3, 2, 3)
ax3.set_title("Irysy (Virginica): LinearSVC (Bez skalowania)")
DecisionBoundaryDisplay.from_estimator(
    model_3, X_train_virginica, response_method="predict",
    cmap=plt.cm.viridis, alpha=0.3, ax=ax3, xlabel='petal length (cm)', ylabel='petal width (cm)'
)
ax3.scatter(X_train_virginica.iloc[:, 0], X_train_virginica.iloc[:, 1], c=y_train_virginica, cmap=plt.cm.viridis, edgecolors='k', s=20)


ax4 = plt.subplot(3, 2, 4)
ax4.set_title("Irysy (Virginica): LinearSVC (Ze skalowaniem)")
DecisionBoundaryDisplay.from_estimator(
    model_4, X_train_scaled_iris, response_method="predict",
    cmap=plt.cm.viridis, alpha=0.3, ax=ax4, xlabel='petal length (scaled)', ylabel='petal width (scaled)'
)
ax4.scatter(X_train_scaled_iris[:, 0], X_train_scaled_iris[:, 1], c=y_train_virginica, cmap=plt.cm.viridis, edgecolors='k', s=20)


ax5 = plt.subplot(3, 1, 3) 
ax5.set_title("Regresja: Porównanie Pipeline vs SVR (optymalny)")


ax5.scatter(X, y, color='gray', s=10, label="Dane")


X_plot = np.linspace(-2.5, 2.5, 100).reshape(-1, 1)


y_plot_poly = poly_svr_pipe.predict(X_plot)
y_plot_svr_best = best_svr.predict(X_plot)


ax5.plot(X_plot, y_plot_poly, color='blue', linewidth=3, label="LinearSVR + PolyFeatures (Pipeline)")
ax5.plot(X_plot, y_plot_svr_best, color='red', linestyle='--', linewidth=3, label="SVR Kernel Poly (GridSearch)")

ax5.set_xlabel('X')
ax5.set_ylabel('y')
ax5.legend()


plt.tight_layout()
plt.show()