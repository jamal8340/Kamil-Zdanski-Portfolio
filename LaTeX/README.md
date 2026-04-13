# ☢️ Analiza Danych i Skład Tekstu (LaTeX): Dozymetria Promieniowania

W tym repozytorium znajduje się projekt akademicki łączący zaawansowaną analizę danych eksperymentalnych z profesjonalnym składem tekstu naukowego przy użyciu systemu **LaTeX**. 

Projekt ten demonstruje umiejętność matematycznego opracowywania wyników, weryfikacji praw fizycznych oraz wizualizacji danych za pomocą narzędzi wektorowych bezpośrednio w kodzie źródłowym.

## 🛠️ Technologie i Narzędzia
* **Skład dokumentu:** LaTeX
* **Wizualizacja danych:** `pgfplots`, `TikZ`
* **Pakiety matematyczne:** `amsmath`, `amssymb`, `siunitx`
* **Kluczowe kompetencje:** Analiza danych, regresja liniowa, rachunek niepewności pomiarowych, profesjonalne raportowanie.

---

## 📂 Przegląd Projektu

### 1. Analiza Danych i Modelowanie
Projekt polega na przetworzeniu surowych danych z detektora promieniowania jonizującego w celu weryfikacji teoretycznych modeli fizycznych:
* **Weryfikacja Prawa Odwrotnych Kwadratów:** Analiza zależności mocy dawki od odległości z wykorzystaniem dopasowania krzywej nieliniowej ($f(r) = a/r^2$).
* **Wyznaczanie współczynników materiałowych:** Zastosowanie prawa osłabienia promieniowania. Przeprowadzenie linearyzacji danych za pomocą logarytmu naturalnego w celu wyznaczenia masowego współczynnika osłabienia dla aluminium metodą regresji liniowej.
* **Propagacja błędów:** Zaawansowany rachunek niepewności pomiarowych (niepewność typu A, odchylenie standardowe średniej, prawo przenoszenia niepewności).

### 2. Zaawansowany Typesetting w LaTeX
Kod źródłowy (`.tex`) demonstruje biegłość w tworzeniu profesjonalnej dokumentacji technicznej:
* **Generowanie Wykresów z Kodu:** Użycie pakietu `pgfplots` do automatycznego rysowania wykresów na podstawie wprowadzonych współrzędnych, włączając w to słupki błędów (error bars) oraz krzywe dopasowania.
* **Złożone Struktury Tabelaryczne:** Tworzenie czytelnych tabel z danymi przy użyciu wielokrotnego łączenia komórek (`multicolumn`, `multirow`) oraz customowych definicji kolumn.
* **Środowiska Matematyczne:** Płynne formatowanie złożonych wzorów matematycznych, równań i symboli fizycznych z zachowaniem rygorystycznych standardów typograficznych.