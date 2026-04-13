# ⚙️ Data Engineering & Analytics Pipelines

W tym repozytorium znajdują się skrypty i mini-projekty z obszaru Inżynierii Danych oraz Analizy Danych. Skupiają się one na przetwarzaniu dużych zbiorów danych (ETL), transformacji szeregów czasowych oraz analityce in-memory z wykorzystaniem nowoczesnych narzędzi i bibliotek w ekosystemie Pythona.

## 🛠 Technologie i Narzędzia
* **Język:** Python 3.x
* **Biblioteki:** `pandas`, `numpy`, `duckdb`, `scipy`, `json`
* **Kluczowe zagadnienia:** ETL (Extract, Transform, Load), Relational Joins, Time-Series Analysis (Upsampling/Downsampling), In-Memory OLAP Databases, SQL Window Functions.

---

## 📂 Przegląd Modułów

### 1. Data Processing & ETL z Pandas (`lab3.py`)
Skrypt realizujący pełny przepływ danych: od wczytania surowych plików JSON, przez transformacje, aż po agregację i eksport.
* **Integracja danych:** Łączenie wielu źródeł danych za pomocą operacji `concat` oraz relacyjnych złączeń (`left`, `right`, `inner`, `outer` joins).
* **Data Cleaning & Casting:** Dynamiczna konwersja typów (np. do `int`), standaryzacja formatów tekstowych, radzenie sobie z wartościami brakującymi (`NaN` / `None`).
* **Dynamiczne agregacje:** Wykonywanie grupowania (`groupby`) i obliczeń na podstawie zewnętrznych parametrów konfiguracyjnych wczytywanych z pliku JSON.
* **Kategoryzacja:** Optymalizacja pamięciowa poprzez rzutowanie typów tekstowych na typ `category` oraz rozszerzanie domen kategorycznych.

### 2. Time-Series Transformation (`lab5.py`)
Moduł dedykowany pracy z danymi o charakterze czasowym (np. odczyty z czujników/IoT).
* **Standaryzacja danych:** Czyszczenie nazw kolumn (Regex) i parsowanie różnych formatów daty z wyrównaniem do wspólnego indeksu czasowego (`DatetimeIndex`).
* **Resampling (Downsampling & Upsampling):** * Zmniejszanie częstotliwości próbkowania z bezpiecznym agregowaniem sum i kontrolą minimalnej liczby próbek w oknie (`min_count`).
  * Zwiększanie częstotliwości z zachowaniem proporcji wartości (skalowanie ratia) oraz zastosowaniem wielomianowej/liniowej interpolacji.
* **Grid Alignment:** Transformacja danych z formatu "long" na "wide" (`pivot`), generowanie nowej, wspólnej siatki czasu (`pd.date_range`) i rzutowanie danych wielu czujników na spójną oś czasu.

### 3. In-Memory OLAP Analytics z DuckDB (`lab6.py`)
Wykorzystanie superszybkiej, wbudowanej bazy danych **DuckDB** do analizy ruchu/detektorów za pomocą czystego języka SQL bezpośrednio w Pythonie.
* **Integracja Python-SQL:** Płynne ładowanie surowych danych do wirtualnych tabel DuckDB i eksport wyników bezpośrednio do ramek danych `pandas` (`.df()`).
* **Statystyki grupowe:** Generowanie metryk podstawowych (COUNT DISTINCT, MIN, MAX starttime) per detektor.
* **Zaawansowane Funkcje Okna (SQL Window Functions):**
  * Użycie funkcji `LAG()` do analizy wartości poprzedzających.
  * Agregacje ruchome oparte na liczbie wierszy (`ROWS BETWEEN CURRENT ROW AND 9 FOLLOWING`).
  * Agregacje ruchome oparte na przedziałach czasu (`RANGE BETWEEN CURRENT ROW AND INTERVAL 900 SECONDS FOLLOWING`), idealne dla nieregularnie próbowanych szeregów czasowych.

---

## 🚀 Uruchomienie

1. Upewnij się, że posiadasz zainstalowane wymagane pakiety:
   ```bash
   pip install pandas numpy duckdb scipy