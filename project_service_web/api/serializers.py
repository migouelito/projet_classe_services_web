# api/serializers.py
from rest_framework import serializers
from cours.models import Cours

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = "__all__"
        extra_kwargs = {
            "titre": {"error_messages": {"required": "Le titre est requis."}},
            "enseignant": {"error_messages": {"required": "Le nom de l'enseignant est requis."}},
            "volumeHoraire": {
                "error_messages": {
                    "required": "Le volume horaire est requis.",
                    "invalid": "Le volume horaire doit être un nombre."
                }
            },
            "actif": {"error_messages": {"required": "Le statut actif est requis."}},
        }

    # Validation personnalisée pour volumeHoraire
    def validate_volumeHoraire(self, value):
        if value <= 0:
            raise serializers.ValidationError("Le volume horaire doit être supérieur à 0.")
        return value