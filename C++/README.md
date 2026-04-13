# 💻 C++ Lab Projects & Custom Data Structures

W tym repozytorium znajdują się zaawansowane projekty akademickie napisane w języku C++. Głównym celem tych implementacji jest głębokie zrozumienie niskopoziomowego zarządzania pamięcią, tworzenia własnych kontenerów od zera oraz poprawnego stosowania zaawansowanych paradygmatów C++.

## 🛠 Technologie i Kluczowe Koncepcje
* **Język:** C++11 / C++14
* **Kluczowe zagadnienia:** Manual Memory Management (wskaźniki, tablice dynamiczne), **Rule of Five** (konstruktory kopiujące/przenoszące, destruktory, operatory przypisania), **PIMPL Idiom**, Operator Overloading, operacje na surowych ciągach znaków (C-strings).

---

## 📂 Przegląd Projektów

### 1. Sorted Unique Vectored List (Hybrydowy Kontener)
Złożona struktura danych łącząca w sobie cechy `std::vector`, `std::list`, `std::set` oraz `std::deque`. Zamiast ciągłego bloku pamięci, kontener opiera się na połączonej liście tzw. "wiaderek" (Buckets), z których każde przechowuje stałą liczbę elementów (statyczna tablica). 

**Główne funkcjonalności i architektura:**
* **PIMPL Idiom (Pointer to Implementation):** Wykorzystanie wewnętrznej struktury `Bucket` z ukryciem implementacji, co zapewnia czystszy plik nagłówkowy i szybszą kompilację.
* **Głębokie zarządzanie pamięcią:** Ręczna alokacja i zwalnianie węzłów listy, z zachowaniem spójności pamięciowej (`head`, `tail`, wskaźniki `next` i `previous`).
* **Unikalność i Sortowanie:** Automatyczna eliminacja duplikatów i utrzymywanie porządku alfabetycznego przechowywanych tekstów przy każdym dodaniu elementu.
* **Przeciążanie operatorów:** * `operator-` (różnica zbiorów).
  * `operator*=` (zwielokrotnianie tekstów w kontenerze).
  * `operator std::string()` (rzutowanie całego kontenera na jeden zwarty tekst).
* **Semantyka przenoszenia (Move Semantics):** Optymalne konstruktory i operatory przenoszące (`&&`), zapobiegające niepotrzebnemu kopiowaniu danych.

### 2. C-String Pointer Vector (`PtrCStringVector`)
Autorska implementacja dynamicznej tablicy (wektora) przechowującej wskaźniki na surowe, niemodyfikowalne ciągi znaków z języka C (`char*`). Projekt symuluje działanie `std::vector<std::string>`, ale wymaga operowania bezpośrednio na pamięci.

**Główne funkcjonalności i architektura:**
* **Niskopoziomowe operacje na tekstach:** Intensywne wykorzystanie biblioteki `<cstring>` (`strcpy`, `strcat`, `strlen`) do alokowania i kopiowania danych znak po znaku.
* **Dynamiczna Reallokacja:** Mechanizm automatycznego rozszerzania pojemności tablicy (strategia podwajania rozmiaru) z bezwyciekowym przenoszeniem dotychczasowych wskaźników.
* **Zasada Pięciu (Rule of Five):** W pełni bezpieczne zarządzanie zasobami poprzez autorski destruktor zwalniający wielowymiarową pamięć, konstruktor kopiujący realizujący **głęboką kopię** (deep copy) oraz bezpieczne operatory przypisania (w tym samoprzypisanie).
* **Zaawansowane Przeciążanie Operatorów:**
  * `operator+` : Konkatenacja dwóch wektorów z alokacją nowej pamięci.
  * `operator&` : Złączenie odpowiadających sobie elementów obu wektorów (sklejanie tekstów z obsługą nierównych rozmiarów tablic).
  * `operator[]` : Bezpieczny dostęp z rzucaniem wyjątków (`std::out_of_range`).

---

## 🚀 Jak skompilować i uruchomić?

Projekty nie wykorzystują zewnętrznych bibliotek i można je skompilować dowolnym standardowym kompilatorem C++ (np. GCC, Clang, MSVC).

