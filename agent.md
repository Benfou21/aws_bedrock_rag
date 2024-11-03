

Création de l'agent avec des actions :

- api-kpi-actions
--> première fois : Création rapide d’une fonction Lambda - recommandé
--> enregistrer 
--> fonction : Tableau, nom : get_kpi_1
--> Paramètres : ticker ;id to get the info from api; string;True

--> cliquer sur afficher dans selection de la fonction Lambda
--> ajouter la logique du code (puis deploy)

-Ajouter Couche :
--> créer une couche dans  Lambda > couches (ARN pandas : https://api.klayers.cloud/api/v2/p3.11/layers/latest/us-west-2/json) , (personalisé : pip install yfinance -t python/ puis zip )

-> pour voir les logs : CloudWatch > groupes de journaux > api-kpi-actions


-> Next :
--> Faire en sorte que le modèle fasse le lien entre le ticker et le nom d'une entreprise
--> Créer les actions pour avoir toutes les données des APIs
--> Créer fonction pour analyse sentimentale

--> Créer interface