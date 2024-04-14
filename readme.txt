Wrapper Météo avec Docker et Trivy par Elyes SALAH
 
Ce projet développe un wrapper en Python pour interroger les prévisions météorologiques d'un emplacement spécifique via les coordonnées géographiques, utilisant l'API OpenWeatherMap. Le script est containerisé dans une image Docker, disponible sur DockerHub, et analysé pour les vulnérabilités avec Trivy.
 
Détails du Repository :
 
weather_wrapper.py : Script Python servant de wrapper à l'API OpenWeatherMap. 
Il nécessite la latitude et la longitude en entrée pour retourner les informations météorologiques de l'emplacement.
 
Dockerfile : Fichier pour la construction de l'image Docker incluant le script Python et ses dépendances.
 
Installation :
 
docker pull esalah/20221477:latest
 
docker run --env LAT="5.902785" --env LONG="102.754175" --env API_KEY="VOTRE_CLE_API" weatherapp:latest
Pour obtenir les données météo.
 
Étapes :
 
Script Python : Créez un fichier weather_wrapper.py utilisant l'API OpenWeatherMap pour obtenir les conditions météo avec les coordonnées de latitude et longitude. 
Les clés API et coordonnées doivent être passées comme variables d'environnement.
 
Dockerfile :
 
FROM python:3.9-alpine
WORKDIR /app
COPY weather_wrapper.py
RUN pip install requests --no-cache-dir
CMD ["python", "weather_wrapper.py"]
 
Construction de l'Image Docker :
 
docker build -t weatherapp
 
Taguez l'image avec une version spécifique au besoin.
 
Publication sur DockerHub :
 
docker login
docker tag weatherapp esalah/20221477
 
Puis, publiez l'image sur DockerHub en utilisant :
 
docker push esalah/20221477
 
Analyse avec Trivy :
 
Installez Trivy et scannez l'image pour des vulnérabilités :
 
docker run aquasec/trivy image esalah/20221477
 
Modification effectuée pour réduire les vulnérabilités en changeant la base de l'image Docker de python:3.9-slim à python:3.9-alpine.
 
Correction des erreurs Hadolint :
 
Utilisez Hadolint pour détecter les erreurs de style dans le Dockerfile :
 
docker run --rm -i hadolint/hadolint < Dockerfile
 
Correction apportée par l'ajout de la version spécifique des paquets et l'utilisation de --no-cache-dir pour installer requests.