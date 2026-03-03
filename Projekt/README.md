# System zarządzania cyfrową biblioteką (Zadanie 1)

## Spis treści

1. [Opis](#opis)
2. [Funkcjonalności](#funkcjonalności)
3. [Uruchomienie](#uruchomienie)

## Opis

Aplikacja MVC: model Book, widoki Django, szablony. Katalog książek — tytuł, autor, rok wydania.

## Funkcjonalności

- Model: Książka (tytuł, autor, rok wydania)
- Lista książek
- Formularze: dodawanie, edycja, usuwanie (z potwierdzeniem)
- Panel admina (Django admin)

## Uruchomienie

Python 3.10+, pip.

```bash
cd Projekt
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/ — wcześniej `python manage.py createsuperuser`. Dane: formularz na stronie lub admin.
