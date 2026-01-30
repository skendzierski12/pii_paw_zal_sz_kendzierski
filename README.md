# 🌍 Wiki Fantasy - System Zarządzania Światem z Plagą

Aplikacja webowa Django do katalogowania i zarządzania światem fantasy dotkniętym epidemią. System umożliwia dokumentowanie kontynentów, lokacji, ras, gildii, królestw, przedmiotów oraz szczegółowych informacji o pladze.

## 📋 Spis treści

- [Funkcjonalności](#-funkcjonalności)
- [Technologie](#-technologie)
- [Wymagania](#-wymagania)
- [Instalacja](#-instalacja)
- [Konfiguracja](#-konfiguracja)
- [Uruchomienie](#-uruchomienie)
- [Struktura projektu](#-struktura-projektu)
- [Modele danych](#-modele-danych)
- [API Endpoints](#-api-endpoints)
- [Autoryzacja](#-autoryzacja)
- [Przykłady użycia API](#-przykłady-użycia-api)
- [Panel administracyjny](#-panel-administracyjny)
- [Licencja](#-licencja)

## ✨ Funkcjonalności

- 📚 **Katalog świata** - zarządzanie kontynentami, lokacjami, rasami, gildiami i królestwami
- 🦠 **System plagi** - śledzenie epicentrów, statystyk zarażeń i zgonów
- 🔐 **Uwierzytelnianie** - system logowania i rejestracji użytkowników
- 🌐 **REST API** - pełne API z tokenami uwierzytelniającymi
- 📱 **Interfejs HTML** - responsywne widoki do przeglądania danych
- 🎨 **Herby lokacji** - możliwość dodawania grafik/emblematów
- 🔍 **Filtrowanie i sortowanie** - uporządkowane dane według populacji i nazw

## 🛠 Technologie

- **Backend:** Django 6.0.1
- **API:** Django REST Framework
- **Baza danych:** SQLite3
- **Uwierzytelnianie:** Token Authentication + Basic Authentication
- **Python:** 3.13+

## 📦 Wymagania

- Python 3.13 lub nowszy
- pip (menedżer pakietów Python)
- virtualenv (opcjonalnie, ale zalecane)

## 🚀 Instalacja

### 1. Sklonuj repozytorium

```bash
git clone <url-repozytorium>
cd projekt_zaliczeniowy
```

### 2. Utwórz środowisko wirtualne

```bash
# Linux/MacOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Zainstaluj zależności

```bash
pip install django==6.0.1
pip install djangorestframework
pip install pillow  # Do obsługi obrazków (emblem)
```

### 4. Wykonaj migracje

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Utwórz superusera (administratora)

```bash
python manage.py createsuperuser
```

Podaj nazwę użytkownika, email i hasło.

## ⚙️ Konfiguracja

### Ustawienia bezpieczeństwa (WAŻNE dla produkcji!)

W pliku `projekt_zaliczeniowy/settings.py`:

```python
# Zmień SECRET_KEY na unikalny!
SECRET_KEY = 'twoj-unikalny-sekretny-klucz'

# W produkcji ustaw DEBUG na False
DEBUG = False

# Dodaj domenę produkcyjną
ALLOWED_HOSTS = ['twoja-domena.com', 'localhost', '127.0.0.1']
```

### Dozwolone hosty

Domyślnie projekt akceptuje połączenia z:
- `localhost`
- `127.0.0.1`
- `192.168.0.136` (sieć lokalna)

## 🎯 Uruchomienie

### Serwer deweloperski

```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem: `http://localhost:8000/`

### Uruchomienie na konkretnym porcie

```bash
python manage.py runserver 8080
```

### Uruchomienie na wszystkich interfejsach (dostęp z sieci)

```bash
python manage.py runserver 0.0.0.0:8000
```

## 📁 Struktura projektu

```
projekt_zaliczeniowy/
├── manage.py                      # Skrypt zarządzający Django
├── db.sqlite3                     # Baza danych SQLite
├── projekt_zaliczeniowy/          # Konfiguracja projektu
│   ├── __init__.py
│   ├── settings.py               # Główne ustawienia
│   ├── urls.py                   # Główne URLe
│   ├── wsgi.py                   # WSGI config
│   └── asgi.py                   # ASGI config
└── wiki/                          # Aplikacja Wiki
    ├── __init__.py
    ├── admin.py                  # Konfiguracja panelu admin
    ├── apps.py                   # Konfiguracja aplikacji
    ├── models.py                 # Modele danych
    ├── serializers.py            # Serializery REST API
    ├── views.py                  # Widoki (logika)
    ├── urls.py                   # URLe aplikacji
    ├── permissions.py            # Uprawnienia
    ├── templates/                # Szablony HTML
    └── migrations/               # Migracje bazy danych
```

## 🗄️ Modele danych

### Continent (Kontynent)
- Kontynenty w świecie fantasy
- Pola: nazwa, opis, klimat, typ terenu, populacja
- Sortowanie: według populacji

### Location (Lokacja)
- Miasta, wioski i inne miejsca
- Pola: nazwa, opis, typ, populacja, bezpieczeństwo od plagi, herb
- Relacja: należy do kontynentu

### Race (Rasa)
- Rasy zamieszkujące świat
- Pola: nazwa, opis, odporność, ojczyzna, cechy, etos
- Relacja: ojczyzna to kontynent

### Guild (Gildia)
- Organizacje i gildie
- Pola: nazwa, opis, specjalne cechy

### Kingdom (Królestwo)
- Państwa i królestwa
- Pola: nazwa, opis, stolica, populacja
- Relacja: stolica to lokacja

### Plague (Plaga)
- Informacje o epidemii (tylko jeden rekord!)
- Pola: opis, historia, objawy, liczba zgonów, epicentrum
- Relacja: epicentrum to lokacja

### Epicentre (Epicentrum plagi)
- Rozszerzenie Location z danymi o pladze
- Pola dodatkowe: procent zarażonych, zgony, poziom zagrożenia
- Poziomy zagrożenia: niski, umiarkowany, wysoki, śmiertelny

### Item (Przedmiot)
- Przedmioty w świecie
- Pola: nazwa, opis, efekt

## 🌐 API Endpoints

### Uwierzytelnianie

| Metoda | Endpoint | Opis |
|--------|----------|------|
| POST | `/api/login/` | Pobranie tokenu uwierzytelniającego |

### Listy zasobów

| Metoda | Endpoint | Opis |
|--------|----------|------|
| GET, POST | `/api/` | Główny endpoint API |
| GET, POST | `/api/continents/` | Lista kontynentów |
| GET, POST | `/api/locations/` | Lista lokacji |
| GET, POST | `/api/races/` | Lista ras |
| GET, POST | `/api/guilds/` | Lista gildii |
| GET, POST | `/api/kingdoms/` | Lista królestw |
| GET, POST | `/api/epicentres/` | Lista epicentrów plagi |
| GET, POST | `/api/items/` | Lista przedmiotów |

### Szczegóły zasobów

| Metoda | Endpoint | Opis |
|--------|----------|------|
| GET, PUT, PATCH, DELETE | `/api/continents/<id>/` | Operacje na kontynencie |
| GET, PUT, PATCH, DELETE | `/api/locations/<id>/` | Operacje na lokacji |
| GET, PUT, PATCH, DELETE | `/api/races/<id>/` | Operacje na rasie |
| GET, PUT, PATCH, DELETE | `/api/guilds/<id>/` | Operacje na gildii |
| GET, PUT, PATCH, DELETE | `/api/kingdoms/<id>/` | Operacje na królestwie |
| GET, PUT, PATCH, DELETE | `/api/items/<id>/` | Operacje na przedmiocie |
| GET, PUT, PATCH, DELETE | `/api/plague/<id>` | Operacje na informacjach o pladze |

### Widoki HTML

| Endpoint | Opis |
|----------|------|
| `/` | Strona główna |
| `/continents/` | Lista kontynentów (HTML) |
| `/continents/<id>/` | Szczegóły kontynentu |
| `/locations/` | Lista lokacji |
| `/locations/<id>/` | Szczegóły lokacji |
| `/races/` | Lista ras |
| `/races/<id>/` | Szczegóły rasy |
| `/guilds/` | Lista gildii |
| `/guilds/<id>/` | Szczegóły gildii |
| `/kingdoms/` | Lista królestw |
| `/kingdoms/<id>/` | Szczegóły królestwa |
| `/items/` | Lista przedmiotów |
| `/items/<id>/` | Szczegóły przedmiotu |
| `/plague/` | Informacje o pladze |

### Autoryzacja użytkowników

| Endpoint | Opis |
|----------|------|
| `/login/` | Logowanie |
| `/logout/` | Wylogowanie |
| `/register/` | Rejestracja nowego użytkownika |

## 🔐 Autoryzacja

API obsługuje dwa typy uwierzytelniania:

### 1. Token Authentication (zalecane dla API)

```bash
# Uzyskanie tokenu
curl -X POST http://localhost:8000/api/login/ \
  -d "username=admin&password=haslo123"

# Odpowiedź:
{
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### 2. Basic Authentication

Przekazywanie username:password w każdym żądaniu.

## 📝 Przykłady użycia API

### Pobranie listy kontynentów

```bash
curl http://localhost:8000/api/continents/ \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
```

### Utworzenie nowego kontynentu

```bash
curl -X POST http://localhost:8000/api/continents/ \
  -H "Authorization: Token TWOJ_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Azeroth",
    "description": "Mityczny kontynent pełen magii",
    "climate": "Umiarkowany",
    "terrain_type": "Różnorodny",
    "population": 5000000
  }'
```

### Edycja kontynentu

```bash
curl -X PATCH http://localhost:8000/api/continents/1/ \
  -H "Authorization: Token TWOJ_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "population": 5500000
  }'
```

### Usunięcie kontynentu

```bash
curl -X DELETE http://localhost:8000/api/continents/1/ \
  -H "Authorization: Token TWOJ_TOKEN"
```

### Utworzenie lokacji z powiązaniem

```bash
curl -X POST http://localhost:8000/api/locations/ \
  -H "Authorization: Token TWOJ_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Stormwind",
    "description": "Wielka stolica ludzi",
    "continent": 1,
    "location_type": "Miasto",
    "population": 200000,
    "is_safe_from_plague": true
  }'
```

### Utworzenie epicentrum plagi

```bash
curl -X POST http://localhost:8000/api/epicentres/ \
  -H "Authorization: Token TWOJ_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Darkshire",
    "description": "Ciemna wioska",
    "continent": 1,
    "location_type": "Wioska",
    "population": 5000,
    "is_safe_from_plague": false,
    "infection_rate": 75,
    "deaths_here": 1200,
    "danger_level": "high"
  }'
```

### Użycie w Pythonie

```python
import requests

# Logowanie i pobranie tokenu
response = requests.post('http://localhost:8000/api/login/', 
    data={'username': 'admin', 'password': 'haslo123'})
token = response.json()['token']

# Nagłówki z tokenem
headers = {
    'Authorization': f'Token {token}',
    'Content-Type': 'application/json'
}

# Pobranie listy kontynentów
continents = requests.get('http://localhost:8000/api/continents/', 
    headers=headers).json()

# Utworzenie nowego kontynentu
new_continent = {
    'name': 'Northrend',
    'description': 'Lodowy kontynent na północy',
    'climate': 'Arktyczny',
    'terrain_type': 'Lodowce i tundra',
    'population': 500000
}
response = requests.post('http://localhost:8000/api/continents/', 
    headers=headers, json=new_continent)
```

## 👨‍💼 Panel administracyjny

Dostęp do panelu administracyjnego:

```
http://localhost:8000/admin/
```

Zaloguj się używając konta superusera utworzonego wcześniej.

W panelu możesz:
- ✅ Zarządzać wszystkimi modelami
- ✅ Dodawać, edytować i usuwać rekordy
- ✅ Przeglądać powiązania między obiektami
- ✅ Zarządzać użytkownikami i uprawnieniami

## 🧪 Testowanie

### Uruchomienie testów

```bash
python manage.py test
```

### Shell Django (interaktywne testowanie)

```bash
python manage.py shell
```

Przykład użycia w shell:

```python
from wiki.models import Continent, Location

# Utworzenie kontynentu
kontynent = Continent.objects.create(
    name="Testowy Kontynent",
    description="Opis testowy",
    climate="Tropikalny",
    terrain_type="Dżungla",
    population=1000000
)

# Pobranie wszystkich kontynentów
wszystkie = Continent.objects.all()

# Filtrowanie
duze = Continent.objects.filter(population__gt=1000000)
```

## 🔧 Przydatne komendy

```bash
# Sprawdzenie projektu pod kątem błędów
python manage.py check

# Utworzenie nowych migracji
python manage.py makemigrations

# Zastosowanie migracji
python manage.py migrate

# Wyświetlenie SQL dla migracji
python manage.py sqlmigrate wiki 0001

# Zbieranie plików statycznych (produkcja)
python manage.py collectstatic

# Czyszczenie bazy danych
python manage.py flush
```

## ⚠️ Uwagi bezpieczeństwa

Przed wdrożeniem w środowisku produkcyjnym:

1. **Zmień SECRET_KEY** na unikalny i nie udostępniaj go publicznie
2. **Ustaw DEBUG = False** w settings.py
3. **Skonfiguruj ALLOWED_HOSTS** tylko dla zaufanych domen
4. **Użyj produkcyjnej bazy danych** (PostgreSQL, MySQL) zamiast SQLite
5. **Skonfiguruj HTTPS** dla bezpiecznej komunikacji
6. **Dodaj CORS headers** jeśli API będzie dostępne z innych domen
7. **Regularnie aktualizuj** Django i zależności

## 🤝 Współpraca

Jeśli chcesz wnieść swój wkład w projekt:

1. Fork repozytorium
2. Utwórz branch dla swojej funkcjonalności (`git checkout -b feature/NowaFunkcja`)
3. Commit zmian (`git commit -m 'Dodanie nowej funkcji'`)
4. Push do brancha (`git push origin feature/NowaFunkcja`)
5. Utwórz Pull Request


**Projekt stworzony jako zaliczenie z przedmiotu Projektowanie Aplikacji Webowych**

*Wersja: 1.0 | Django 6.0.1 | Python 3.13+*
