# 📅 System Rezerwacji Zasobów (Resource Reservation System)

Kompleksowy projekt inżynierski systemu informatycznego służącego do zarządzania i rezerwacji współdzielonych zasobów wewnątrz organizacji (m.in. sale konferencyjne, laptopy, rzutniki). 

Projekt został zrealizowany w ramach przedmiotu **Inżynieria Oprogramowania** i obejmuje pełną analizę systemową, modelowanie procesów biznesowych oraz projekt architektury aplikacji webowej w oparciu o wzorzec MVC.

## 👥 Autorzy Projektu
* **Wojciech Żmuda**
* **Kamil Zdański**
* Grupa: CWP 5

---

## 🚀 Główne Funkcjonalności (Use Cases)

System przewiduje dwa główne poziomy dostępu opierające się na rolach: **Użytkownik** oraz **Administrator**.

### 🧑‍💻 Moduł Użytkownika
* **Wyszukiwanie i dostępność:** Przeglądanie katalogu zasobów z podglądem ich dostępności w czasie rzeczywistym.
* **Rezerwacje jednorazowe i cykliczne:** Możliwość rezerwowania zasobów na konkretny termin, a także tworzenia serii rezerwacji (np. co tydzień) z automatyczną detekcją konfliktów.
* **Zarządzanie kontem:** Wgląd w historię własnych rezerwacji, możliwość ich anulowania oraz funkcja samodzielnej zmiany hasła.

### 🛡️ Moduł Administratora
* **Zarządzanie Katalogiem Zasobów:** Pełny dostęp do operacji CRUD (Create, Read, Update, Delete) na sprzęcie i salach, wliczając w to blokady usuwania zasobów będących w aktywnym użyciu.
* **Zarządzanie Użytkownikami:** Dodawanie nowych kont, edycja ról oraz usuwanie pracowników z systemu.
* **Monitorowanie Systemu:** Wgląd w globalny dziennik wszystkich rezerwacji w systemie z możliwością zaawansowanego filtrowania.

---

## 🏗️ Architektura i Technologie

Aplikacja została zaprojektowana w modelu klient-serwer jako nowoczesna aplikacja przeglądarkowa.

* **Wzorzec Projektowy:** System opiera się na architekturze **MVC (Model-View-Controller)** zaadaptowanej do środowiska webowego.
* **Moduł Serwerowy:** Podzielony na warstwy: *API Layer* (przyjmowanie żądań HTTP), *Service Layer* (logika biznesowa i weryfikacja kolizji terminów) oraz *Repository Layer* (komunikacja z bazą danych).
* **Komunikacja (REST API):** Wymiana danych w formacie **JSON** poprzez bezstanowe API. Autoryzacja i zarządzanie sesją realizowane jest za pomocą tokenów **JWT (JSON Web Token)**.

---

## 📂 Zawartość Dokumentacji Projektowej

W ramach projektu sporządzono kompletną dokumentację analityczno-projektową, w której skład wchodzą:

1. **Modele UML:** * Diagram Przypadków Użycia obrazujący interakcje aktorów z systemem.
   * Diagram Klas Dziedzinowych i Systemowych szczegółowo opisujący strukturę danych oraz relacje pomiędzy widokami, kontrolerami i modelami.
2. **Modelowanie Przepływu Danych (DFD):**
   * Hierarchiczna dekompozycja procesów: od Diagramu Kontekstowego, przez Poziom 0 (Systemowy) operujący na magazynach danych (Użytkownicy, Zasoby, Rezerwacje), aż po szczegółowe diagramy Poziomu 1.
3. **Projekty Interfejsu (UI Mockups):**
   * Wizualizacje kluczowych ekranów aplikacji: Panel Logowania, Interaktywny Kalendarz Rezerwacji, Historia Rezerwacji oraz Panel Zarządzania Systemem dla Administratora (zawierający obsługę wyjątków i błędów walidacji).