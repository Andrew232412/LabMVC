from django.db import models


class Book(models.Model):
    tytul = models.CharField("tytuł", max_length=200)
    autor = models.CharField(max_length=200)
    rok_wydania = models.PositiveIntegerField("rok wydania")

    class Meta:
        ordering = ["-rok_wydania", "tytul"]

    def __str__(self):
        return f"{self.tytul} ({self.autor}, {self.rok_wydania})"
