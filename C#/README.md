# 💻 C# Lab Projects & Mini-Tools

W tym folderze znajdują się akademickie projekty i skrypty napisane w języku C#. Skupiają się one głównie na przetwarzaniu danych z plików (JSON, CSV, XML), transformacji danych oraz wykorzystaniu zaawansowanych mechanizmów języka takich jak **LINQ**, **Generics** oraz delegaty.

## 🛠 Technologie i Narzędzia
* **Język:** C# / .NET
* **Kluczowe zagadnienia:** LINQ, OOP, Generic Types, Serialization/Deserialization (JSON, XML), Text Parsing, algorytmy (TF-IDF).

---

## 📂 Przegląd Projektów

### 1. Analizator Tweetów (JSON Parsing & Text Analysis)
Skrypt służący do wczytywania i analizy strumienia danych z Twittera zapisanych w formacie `.jsonl`. Projekt demonstruje nie tylko deserializację obiektów, ale również podstawy analizy tekstu.

**Główne funkcjonalności:**
* **Deserializacja JSON:** Wczytywanie i mapowanie logów do silnie typowanej listy obiektów `Tweet`.
* **Analiza czasowa:** Sortowanie tweetów po dacie oraz identyfikacja najstarszych i najnowszych wpisów z uwzględnieniem parsowania niestandardowych formatów czasu (`CultureInfo.InvariantCulture`).
* **Grupowanie danych:** Wykorzystanie słowników (`Dictionary<string, List<Tweet>>`) do grupowania aktywności konkretnych użytkowników.
* **Obliczanie IDF (Inverse Document Frequency):** Zaawansowana analiza częstotliwości występowania słów (o długości min. 5 znaków) i implementacja matematycznego wzoru na IDF w celu znalezienia najbardziej unikalnych i znaczących słów w zbiorze.
* **Eksport danych:** Możliwość serializacji i deserializacji przetworzonych danych do formatu XML.

### 2. Northwind Data Aggregator (CSV Parsing & Advanced LINQ)
Narzędzie analityczne symulujące pracę na relacyjnej bazie danych (model Northwind) przy użyciu surowych plików `.csv`. Projekt świetnie obrazuje wykorzystanie C# jako narzędzia do inżynierii danych w pamięci.

**Główne funkcjonalności:**
* **Generyczny parser CSV:** Autorska klasa `wczytywacz` wykorzystująca typy generyczne (`<T>`) oraz delegaty (`Func<string[], T>`) do dynamicznego mapowania wierszy CSV na odpowiednie struktury i klasy (np. `employee`, `order`, `territory`).
* **Złożone zapytania LINQ (Joins):** Realizacja zapytań przypominających SQL bezpośrednio w kodzie C# (łączenie wielu list na podstawie kluczy obcych, np. dopasowywanie pracowników do regionów i terytoriów).
* **Agregacja i grupowanie danych (GroupBy):** Obliczanie zaawansowanych statystyk biznesowych, w tym:
  * Łączna wartość zamówień z uwzględnieniem ilości, ceny jednostkowej i zniżki (parsowanie `double` z formatów invariant).
  * Wyliczanie średniej i maksymalnej wartości zamówienia per pracownik.
  * Grupowanie pracowników według obsługiwanych regionów.

---

## 🚀 Jak uruchomić?

Wymagane jest środowisko wspierające .NET.
1. Sklonuj repozytorium.
2. Upewnij się, że odpowiednie zbiory danych (`favorite-tweets.jsonl` lub pliki CSV bazy Northwind) znajdują się w katalogu roboczym (bin/Debug/net...).
3. Uruchom skrypty za pomocą polecenia `dotnet run` lub z poziomu IDE (np. Visual Studio / Rider).