#!/bin/bash
clear
#!/bin/bash
echo "Choisissez une option :"
echo "1 - Serveur local (accessible seulement sur ce PC)"
echo "2 - Serveur réseau (accessible depuis une autre machine)"

read choix

if [ "$choix" = "2" ]; then
    echo "Serveur accessible sur le réseau..."
    python3 manage.py runserver 0.0.0.0:8000
else
    echo "Serveur accessible uniquement en local..."
    python3 manage.py runserver 127.0.0.1:8000
fi

