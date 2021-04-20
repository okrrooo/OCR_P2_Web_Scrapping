Pour créer votre environnement virtuel suivez la doc officiel : 

https://docs.python.org/3/tutorial/venv.html

Les modules requis sont dans le requirements.txt

Exécutez main.py pour utiliser le programme.

----


Bonjour, Ceci est mon premier script dans le cadre de ma formation sur Openclassrooms.
Dans le cadre de mon 'projet n°2' je dois faire du webscraping en utilisant beautifulsoup
et requests.

Je suis donc charger de récupérer les informations du site 'https://books.toscrape.com/index.html'

Voici donc le mail qui me décrit exactement ma mission :

Objet : Programme d'extraction des prix
À : Vous
De : Sam

Bonjour ! 

J'espère que vous pourrez m'aider à créer un système de surveillance des prix. Pour élaborer une version bêta du système limitée à un seul revendeur, le mieux est probablement de suivre les étapes que j'ai définies ci-dessous.

Choisissez n'importe quelle page Produit sur le site de Books to Scrape. Écrivez un script Python qui visite cette page et en extrait les informations suivantes :

product_page_url
universal_ product_code (upc)
title
price_including_tax
price_excluding_tax
number_available
product_description
category
review_rating
image_url

Écrivez les données dans un fichier CSV qui utilise les champs ci-dessus comme en-têtes de colonnes.

Maintenant que vous avez obtenu les informations concernant un premier livre, vous pouvez essayer de récupérer toutes les données nécessaires pour toute une catégorie d'ouvrages. Choisissez n'importe quelle catégorie sur le site de Books to Scrape. Écrivez un script Python qui consulte la page de la catégorie choisie, et extrait l'URL de la page Produit de chaque livre appartenant à cette catégorie. Combinez cela avec le travail que vous avez déjà effectué afin d'extraire les données produit de tous les livres de la catégorie choisie, puis écrivez les données dans un seul fichier CSV.

Remarque : certaines pages de catégorie comptent plus de 20 livres, qui sont donc répartis sur différentes pages («  pagination  »). Votre application doit être capable de parcourir automatiquement les multiples pages si présentes. 

Ensuite, étendez votre travail à l'écriture d'un script qui consulte le site de Books to Scrape, extrait toutes les catégories de livres disponibles, puis extrait les informations produit de tous les livres appartenant à toutes les différentes catégories, ce serait fantastique  ! Vous devrez écrire les données dans un fichier CSV distinct pour chaque catégorie de livres.

Enfin, prolongez votre travail existant pour télécharger et enregistrer le fichier image de chaque page Produit que vous consultez  !

Au cours du projet, veillez à enregistrer votre code dans un repository GitHub et à effectuer des commits réguliers accompagnés de messages de commit clairs. N'oubliez pas que vous devez enregistrer un fichier requirements.txt sans enregistrer votre environnement virtuel dans le repository lui-même. Vous ne devez pas non plus y enregistrer vos fichiers CSV. Lorsque vous aurez terminé, envoyez-moi un lien vers votre repository GitHub et un fichier compressé des données qu'il génère. Veillez également à prendre le temps d'écrire un fichier README.md, que vous ajouterez dans le repository afin que je puisse exécuter le code correctement et produire quelques données !

Cordialement,

Sam
Responsable d'équipe
Books Online
