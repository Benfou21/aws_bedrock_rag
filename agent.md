

Création de l'agent avec des actions :

- api-kpi-actions
--> première fois : Création rapide d’une fonction Lambda - recommandé
--> enregistrer 
--> fonction : Tableau, nom : get_kpi_1
--> Paramètres : ticker ;id to get the info from api; string;True   (dans les tests de la lambda fct le paramètre doit être un ticker "AAPL" et non "Apple", hors lorsqu'on essaye de prompte l'agent avec "Accenture" ou "Apple", il renvoi bien "ACN" et "AAPL" aux fonctions-> le LLM (claude 3) comprend alors qu'il faut passer de "Accenture" a ACN, mais pour des entreprise moins connu il ne le fera pas ex "EMP".

--> cliquer sur afficher dans selection de la fonction Lambda
--> ajouter la logique du code (puis deploy)

-Ajouter Couche :
--> créer une couche dans  Lambda > couches (ARN pandas : https://github.com/keithrozario/Klayers/tree/master/deployments/python3.12 -> arn:aws:lambda:us-west-2:770693421928:layer:Klayers-p312-pandas:10) , (personalisé : pip install yfinance -t python/ puis zip )
---> Attention : ordre des couches nécessaires : (1) pandas_yf_layer , (2) arn pandas : supposions que la version de pandas dans la couche perso n'est pas compatible avec yf, donc la couche arn de pandas overwright celle de pandas perso
-> pour voir les logs : CloudWatch > groupes de journaux > api-kpi-actions


-> Next :
--> Faire en sorte que le modèle fasse le lien entre le ticker et le nom d'une entreprise
--> Créer les actions pour avoir toutes les données des APIs
--> Créer fonction pour analyse sentimentale

--> Créer interface




Multi - Prompt 

-> Avis macro économique
-> analyse f
-> Elément clés
-> Analyse S
-> graphique