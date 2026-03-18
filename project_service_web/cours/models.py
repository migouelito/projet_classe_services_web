import uuid
from django.db import models

class Cours(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    titre = models.CharField(max_length=200)
    enseignant = models.CharField(max_length=200)
    volumeHoraire = models.IntegerField()
    actif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} - {self.titre} - {self.enseignant}"
        