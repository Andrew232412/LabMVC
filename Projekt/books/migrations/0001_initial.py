from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("tytul", models.CharField(max_length=200, verbose_name="tytuł")),
                ("autor", models.CharField(max_length=200)),
                ("rok_wydania", models.PositiveIntegerField(verbose_name="rok wydania")),
            ],
            options={
                "ordering": ["-rok_wydania", "tytul"],
            },
        ),
    ]
