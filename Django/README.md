# Django — 7 kroków tutoriala

[Writing your first Django app](https://docs.djangoproject.com/en/6.0/intro/tutorial01/), parts 1–7.

1. Projekt mysite, aplikacja polls, runserver  
2. Baza, modele Question/Choice, admin  
3. Widoki, URLconf, szablony (index, detail, results, vote)  
4. Formularze, generic views  
5. Testy (model, widoki)  
6. Static (CSS)  
7. Admin: fieldsets, inlines, list_display, list_filter, search_fields  

Python 3.10+, pip.

```bash
cd Django/djangotutorial
python3 -m venv .venv && source .venv/bin/activate
pip install Django
python manage.py migrate
python manage.py runserver
```

http://127.0.0.1:8000/polls/ — przy pustej bazie: "No polls are available."; admin → Polls → Questions, dodaj pytanie i Choices.

Testy: `python manage.py test polls` → 10 testów, OK.
