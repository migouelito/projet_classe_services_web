from rest_framework import viewsets, status
from rest_framework.response import Response
from cours.models import Cours
from .serializers import CoursSerializer
from rest_framework.exceptions import ValidationError
from datetime import datetime
from django.http import Http404

def json_response(message, status_code=status.HTTP_200_OK, error=False):
    """
    Réponse JSON standardisée avec 'error' en premier si nécessaire
    """
    if error:
        payload = {
            "error": message,
            "timestamp": datetime.now().isoformat()
        }
    else:
        payload = {
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
    return Response(payload, status=status_code)

class CoursViewSet(viewsets.ModelViewSet):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

    # --- Méthode pour extraire le premier message d'erreur clair ---
    def _get_first_error_message(self, errors):
        """
        errors peut être dict ou list venant de ValidationError.detail
        """
        if isinstance(errors, dict):
            first_key = next(iter(errors))
            first_error = errors[first_key]
            if isinstance(first_error, (list, tuple)):
                return str(first_error[0])
            return str(first_error)
        elif isinstance(errors, list):
            return str(errors[0])
        else:
            return str(errors)

    # --- Récupération d'un cours ---
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Http404:
            return json_response("Ressource inexistante", status.HTTP_404_NOT_FOUND, error=True)

    # --- Création d'un cours ---
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return json_response("Création réussie", status.HTTP_201_CREATED)
        except ValidationError as e:
            message = self._get_first_error_message(e.detail)
            return json_response(message, status.HTTP_400_BAD_REQUEST, error=True)

    # --- Mise à jour d'un cours ---
    def update(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data, instance=self.get_object(), partial=False)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return json_response("Mise à jour réussie")
        except Http404:
            return json_response("Ressource inexistante", status.HTTP_404_NOT_FOUND, error=True)
        except ValidationError as e:
            message = self._get_first_error_message(e.detail)
            return json_response(message, status.HTTP_400_BAD_REQUEST, error=True)

    # --- Suppression d'un cours ---
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return json_response("Suppression réussie", status.HTTP_204_NO_CONTENT)
        except Http404:
            return json_response("Ressource inexistante", status.HTTP_404_NOT_FOUND, error=True)


