# LabMVC — projekt zaliczeniowy MVC

Projekt główny (Zadanie 1), 7 kroków tutoriala Django, aplikacja ASP.NET Core MVC (MvcMovie).

## Spis treści

1. [Projekt — biblioteka](#projekt--biblioteka)
2. [Django — polls](#django--polls)
3. [.NET — MvcMovie](#net--mvcmovie)

---

## Projekt — biblioteka

`Projekt/` — Zadanie 1 z PDF. Django: model Książka (tytuł, autor, rok wydania), lista, dodawanie/edycja/usuwanie, admin.

Wymagania: Python 3.10+, pip

```bash
cd Projekt
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

http://127.0.0.1:8000/

---

## Django — polls

`Django/djangotutorial/` — tutorial [parts 1–7](https://docs.djangoproject.com/en/6.0/intro/tutorial01/): mysite, polls (Question, Choice), widoki, formularze, testy, static, admin.

Wymagania: Python 3.10+, pip

```bash
cd Django/djangotutorial
python3 -m venv .venv && source .venv/bin/activate
pip install Django
python manage.py migrate
python manage.py runserver
```

http://127.0.0.1:8000/polls/ — jeśli pusto: admin (createsuperuser) → Polls → Questions, dodaj pytanie i Choices.

Testy: `python manage.py test polls`

---

## .NET — MvcMovie

`Dotnet/` — [tutorial Microsoft](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc): Movie, EF Core SQLite, MoviesController, CRUD.

Wymagania: [.NET 9 SDK](https://dotnet.microsoft.com/download)

```bash
cd Dotnet
dotnet run
```

Adres w konsoli (np. http://localhost:5112). W menu: **Movies** — lista, Create New, Edit, Details, Delete.
