# Opis Projektu 

Projekt przedstawia implementację prostej aplikacji typu e-commerce, wykonanej w języku **Python** z wykorzystaniem frameworka **FastAPI**. Celem projektu było zaprojektowanie podstawowych funkcjonaliści platformy sprzedażowej.

Aplikacja umożliwia zarządzanie:
- produktami,
- koszykiem użytkownika,
- zamówieniami.

Projekt został wykonany jako **szkielet aplikacji**, z naciskiem na logikę biznesową, testy jednostkowe oraz poprawną strukturę kodu.

---
Zastosowane technologie
- Python 3.12+
- FastAPI
- Pydantic
- Pytest
- Uvicorn

---

### Opis warstw

- **API** – obsługa zapytań HTTP (FastAPI), brak logiki biznesowej
    
- **Services** – logika aplikacji (zasady, walidacje, operacje)
    
- **Repositories** – przechowywanie danych w pamięci aplikacji
    
- **Models** – definicje struktur danych (Pydantic)
    

---

## Funkcjonalności

### Produkty

- dodawanie produktu
    
- pobieranie listy produktów
    
- pobieranie produktu po ID
    

### Koszyk

- tworzenie koszyka użytkownika
    
- dodawanie produktów do koszyka
    
- czyszczenie koszyka
    

### Zamówienia

- tworzenie zamówienia na podstawie koszyka
    
- pobieranie zamówienia
    
- generowanie szczegółów zamówienia w formacie **XML**
    

---

## XML – szczegóły zamówienia

Aplikacja umożliwia zwrócenie danych zamówienia w formacie XML, zgodnie z wymaganiami zadania projektowego.

Przykładowy endpoint:

`GET /orders/{order_id}/xml`

XML generowany jest przy użyciu standardowej biblioteki:  
`xml.etree.ElementTree`.

---

## Testy jednostkowe

Projekt zawiera testy jednostkowe dla warstwy serwisów:

- ProductService
    
- CartService
    
- OrderService
    

Testy zostały napisane z użyciem **pytest** i sprawdzają:

- poprawność logiki biznesowej,
    
- obsługę błędów,
    
- poprawne tworzenie zamówień.
    

Uruchamianie testów:

`pytest`

---

## Uruchomienie aplikacji

1. Utwórz i aktywuj środowisko wirtualne
    
2. Zainstaluj zależności
    
3. Uruchom serwer
    

`uvicorn app.main:app --reload`

Swagger UI dostępny pod adresem:

`http://127.0.0.1:8000/docs`

---

## Uwagi końcowe

- Dane przechowywane są w pamięci aplikacji (brak bazy danych).
    
- Projekt stanowi bazę pod dalszą rozbudowę (np. baza danych, autoryzacja).
    
- Kod jest zgodny ze standardami PEP-8.
    

---

## Autor

Projekt wykonany jako zadanie zaliczeniowe z programowania w języku Python.
