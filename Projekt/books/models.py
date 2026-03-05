from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Book(models.Model):
    tytul = models.CharField("tytuł", max_length=200)
    autor = models.CharField("autor", max_length=200)
    rok_wydania = models.PositiveIntegerField(
        "rok wydania", validators=[MinValueValidator(1), MaxValueValidator(2100)]
    )

    class Meta:
        ordering = ["-rok_wydania", "tytul"]

    def __str__(self):
        return f"{self.tytul} ({self.autor}, {self.rok_wydania})"
