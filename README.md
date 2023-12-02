
# Amazon Product Data Scraper

## Description
Ce script Python permet de récupérer des données détaillées sur les produits à partir de leur ASIN (Amazon Standard Identification Number) sur le site Amazon. Il est capable d'extraire des informations telles que le titre, le sous-titre, la description, le prix et d'autres détails de produits.

## Installation
Assurez-vous d'avoir Python installé sur votre système. Vous aurez également besoin des bibliothèques `requests` et `beautifulsoup4`.

Pour installer les dépendances, exécutez :
```
pip install requests beautifulsoup4
```

## Utilisation
Le script peut être exécuté avec Python. Vous devez fournir l'ASIN du produit et le code de langue du site Amazon (par exemple, "fr" pour Amazon France).

Exemple d'utilisation :
```python
asin = "B00IKI352E"
language = "fr"
result = asinResolver(asin, language)
print(result)
```

Le script va extraire les informations du produit et les imprimer sous forme de JSON.

## Fonctionnalités
- Extraction des détails du produit à partir d'Amazon via ASIN.
- Prise en charge de différents domaines Amazon en fonction de la langue.
- Récupération de diverses informations telles que le titre, la description, le prix, etc.

## Avertissements
- Ce script est uniquement destiné à des fins éducatives et de recherche.
- Le scraping de sites web peut être contraire aux conditions d'utilisation du site, utilisez ce script de manière responsable.

## Licence
Ce projet est sous licence libre. Vous êtes libre de l'utiliser et de le modifier pour vos besoins personnels.
