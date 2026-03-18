# Créer les migrations pour toutes les applications installées
echo "Création des migrations..."
python3 manage.py makemigrations

# Appliquer les migrations à la base de données
echo "Application des migrations..."
python3 manage.py migrate

# Afficher les migrations appliquées
echo "Migrations terminées !"
python3 manage.py showmigrations

echo "Toutes les migrations ont été effectuées."

