from django.db import models

# Create your models here.
class Temoignage(models.Model):
    quote = models.TextField(
        max_length = 500,
        blank = False,  #Champ obligatoire
        null = False,



    )
    author = models.CharField(
        max_length = 50,
        blank = False,
        null = False,
    )

    def __str__(self) :  #pour changer la présentation de la calsse quand elle apparait
        return f"{self.quote} par {self.author}" #f for string format self pour renvoyer les vaeiables

