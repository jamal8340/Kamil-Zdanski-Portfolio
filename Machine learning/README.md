# 🤖 Machine Learning & Predictive Modeling

W tym repozytorium znajdują się skrypty i mini-projekty z dziedziny uczenia maszynowego (Machine Learning). Projekty demonstrują praktyczne zastosowanie algorytmów klasyfikacji i regresji, optymalizację hiperparametrów oraz wizualizację granic decyzyjnych z wykorzystaniem ekosystemu Pythona.

## 🛠 Technologie i Narzędzia
* **Język:** Python 3.x
* **Biblioteki:** `scikit-learn`, `pandas`, `numpy`, `matplotlib`
* **Kluczowe zagadnienia:** Regresja Liniowa/Wielomianowa, K-Nearest Neighbors (KNN), Support Vector Machines (SVC/SVR), Feature Scaling, Hyperparameter Tuning (GridSearchCV), Scikit-Learn Pipelines, Model Serialization (`pickle`).

---

## 📂 Przegląd Modułów

### 1. Modelowanie Nieliniowe i Ocena Modeli (`lab03.py`)
Skrypt analizujący problem regresji na wygenerowanym, nieliniowym zbiorze danych z zaszumieniem.
* **Inżynieria Cech (Feature Engineering):** Wykorzystanie `PolynomialFeatures` do transformacji przestrzeni cech i trenowania modeli regresji wielomianowej (od 2 do 5 stopnia).
* **Porównanie Algorytmów:** Zestawienie skuteczności klasycznej Regresji Liniowej, modeli wielomianowych oraz algorytmu K-Najbliższych Sąsiadów (`KNeighborsRegressor` dla różnych wartości *k*).
* **Ewaluacja i Profilowanie:** Ocena modeli na podstawie błędu średniokwadratowego (MSE) dla zbiorów treningowych i testowych. Analiza rozmiaru modeli w pamięci RAM (np. ciężki model KNN przechowujący dane vs lekki model parametryczny).
* **Wizualizacja:** Generowanie czytelnych wykresów za pomocą `matplotlib` w celu wizualnej oceny dopasowania krzywych regresji do danych (underfitting vs overfitting).

### 2. Support Vector Machines i Optymalizacja (`lab04.py`)
Zaawansowany moduł skupiający się na maszynach wektorów nośnych (SVM) z wykorzystaniem popularnych zbiorów danych (Breast Cancer, Iris).
* **Klasyfikacja i Skalowanie:** Praktyczna demonstracja wpływu standaryzacji cech (`StandardScaler`) na zbieżność i dokładność modeli `LinearSVC`.
* **Wizualizacja Marginesów:** Rysowanie dwuwymiarowych granic decyzyjnych (Decision Boundaries) z wykorzystaniem przestrzeni barw w celu analizy separowalności klas.
* **Pipelines:** Konstruowanie bezpiecznych potoków analitycznych (`Pipeline`) łączących transformacje cech (wielomiany) z estymatorem (`LinearSVR`).
* **Hyperparameter Tuning:** Automatyczne poszukiwanie optymalnych parametrów (`C`, `coef0`) dla nieliniowego jądra (`kernel="poly"`) za pomocą `GridSearchCV` z 5-krotną walidacją krzyżową.

---

## 🚀 Uruchomienie

1. Zainstaluj wymagane pakiety:
   ```bash
   pip install scikit-learn pandas numpy matplotlib