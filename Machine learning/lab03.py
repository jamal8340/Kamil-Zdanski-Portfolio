# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import pickle
size = 300
X = np.random.rand(size)*5-2.5
w4, w3, w2, w1, w0 = 1, 2, 1, -4, 2
y = w4*(X**4) + w3*(X**3) + w2*(X**2) + w1*X + w0 + np.random.randn(size)*8-4
df = pd.DataFrame({'x': X, 'y': y})
df.to_csv('dane_do_regresji.csv',index=None)
df.plot.scatter(x='x',y='y')

X_reshaped = X.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X_reshaped,y,test_size=0.2,random_state=42)

# %%
MSE_wyniki={}
Regresory_lista=[]

lin_reg = LinearRegression()
lin_reg.fit(X_train,y_train)
MSE_wyniki['lin_reg']=[
    mean_squared_error(y_train, lin_reg.predict(X_train)),
    mean_squared_error(y_test, lin_reg.predict(X_test))
]
Regresory_lista.append((lin_reg, None))



# %%
knn_3_reg=KNeighborsRegressor(n_neighbors=3)
knn_3_reg.fit(X_train, y_train)
MSE_wyniki['knn_3_reg']=[
    mean_squared_error(y_train, knn_3_reg.predict(X_train)),
    mean_squared_error(y_test, knn_3_reg.predict(X_test))
]
Regresory_lista.append((knn_3_reg, None))

# %%
knn_5_reg = KNeighborsRegressor(n_neighbors=5)
knn_5_reg.fit(X_train, y_train)
MSE_wyniki['knn_5_reg'] = [
    mean_squared_error(y_train, knn_5_reg.predict(X_train)),
    mean_squared_error(y_test, knn_5_reg.predict(X_test))
]
Regresory_lista.append((knn_5_reg, None))

# %%
modele_wielomianowe={}
for stopien in [2,3,4,5]:
    poly_feature=PolynomialFeatures(degree=stopien, include_bias=False)
    X_train_poly=poly_feature.fit_transform(X_train)
    X_test_poly = poly_feature.transform(X_test)
    poly_reg = LinearRegression()
    poly_reg.fit(X_train_poly, y_train)
    
    MSE_wyniki[f'poly_{stopien}_reg'] = [
        mean_squared_error(y_train, poly_reg.predict(X_train_poly)),
        mean_squared_error(y_test, poly_reg.predict(X_test_poly))
    ]
    modele_wielomianowe[stopien]=(poly_reg, poly_feature)
    Regresory_lista.append((poly_reg, poly_feature))

poly_2_reg, poly_feature_2 = modele_wielomianowe[2]
poly_3_reg, poly_feature_3 = modele_wielomianowe[3]
poly_4_reg, poly_feature_4 = modele_wielomianowe[4]
poly_5_reg, poly_feature_5 = modele_wielomianowe[5]   


# %%
df_MSE = pd.DataFrame.from_dict(
    MSE_wyniki,
    orient='index',
    columns=['train_mse','test_mse']
)
df_MSE.to_pickle('mse.pkl')
print(df_MSE)

with open('reg.pkl', 'wb') as f:
    pickle.dump(Regresory_lista, f)

# %%
import matplotlib.pyplot as plt
import numpy as np


X_plot = np.linspace(-2.5, 2.5, 500).reshape(-1, 1)
models_to_plot = [
    ('Regresja Liniowa', lin_reg, None),
    ('KNN (k=3)', knn_3_reg, None),
    ('KNN (k=5)', knn_5_reg, None),
    ('Regresja Wielomianowa (rząd 2)', poly_2_reg, poly_feature_2),
    ('Regresja Wielomianowa (rząd 3)', poly_3_reg, poly_feature_3),
    ('Regresja Wielomianowa (rząd 4)', poly_4_reg, poly_feature_4),
    ('Regresja Wielomianowa (rząd 5)', poly_5_reg, poly_feature_5)
]
for name, model, poly_feat in models_to_plot:
    plt.figure(figsize=(8, 5)) 
    plt.scatter(X, y, color='gray', alpha=0.5, label='Dane oryginalne')
    if poly_feat is not None:
        X_plot_transformed = poly_feat.transform(X_plot)
        y_plot = model.predict(X_plot_transformed)
    else:
        y_plot = model.predict(X_plot)
        
    plt.plot(X_plot, y_plot, color='red', linewidth=2, label=f'Predykcja modelu')
    plt.title(f'Wykres dla: {name}')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()

    plt.show()

# %%
# --- Pamięć ---
mem_lin_reg = len(pickle.dumps(lin_reg))
mem_knn = len(pickle.dumps(knn_5_reg))

print(f"Rozmiar modelu liniowego w pamięci: {mem_lin_reg} bajtów")
print(f"Rozmiar modelu KNN(5) w pamięci: {mem_knn} bajtów")


