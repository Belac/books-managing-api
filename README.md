# books-managing-api
API for managing books of a library, created with Flask, and could be tested from [here](https://books-managing-api.herokuapp.com/)

## Getting started

### Installing dependencies

#### Python
First of all, you must have at least **Python 3.10.0** on your computer.       
If not, click [download python](https://www.python.org/downloads/) to install the latest version of python for your platform.

#### Pip or another package manager
Secondly, be sure you have a **package manager** installed on your computer.    
For instance pip 22.0.3 from C:\Users\Username\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

#### Virtual environment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separated and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

#### Pip dependencies
Once you have your virtual environment setup and running, install dependencies by running :
````
pip install -r requirements.txt
````
or 
````
pip3 install -r requirements.txt
````

### Database Setup
With Postgres running, restore a database using the books_managing.sql file provided.     
From the backend folder in terminal run:
````
psql books_managing < books_managing.sql
````

### Running the server
Ensure you are working using your created virtual environment.
To run the server on Linux or Mac, execute:
````
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
````
To run the server on Windows, execute:
````
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
````
Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.
Setting the FLASK_APP variable to flaskr directs flask to use the flaskr directory and the __init__.py file to find the application.

## Api reference
This app can be run locally or hosted as a base URL. 
The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Error Handling
Errors are retourned as JSON objects in the following format: { "success": False, "error": 404, "message": "Not found" }       
The API will return different error types when requests fail: 
- 400: Bad request 
- 500: Internal server error 
- 422: Unprocessable 
- 404: Not found

## Some endpoints of our API
. ## GET/livres

  GENERAL:  This endpoints returns a list of Livre object, success value, total number of Livre.              
  SAMPLE: curl http://localhost:5000/livres
    
        {
                     
            "book": [
            {
            "auteur": "Michelle Marly",
            "date_publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "editeur": "Fleuves éditions",
            "id": 1,
            "id_categorie": 1,
            "isbn": "978-2-2651-5546-6",
            "titre": "Romy et les lumières de Paris"
            },
            {
            "auteur": "Jens Muller",
            "date_publication": "Mon, 01 Oct 2018 00:00:00 GMT",
            "editeur": "Taschen",
            "id": 2,
            "id_categorie": 1,
            "isbn": "978-3-8365-7037-4",
            "titre": "The history of graphic design : Volume 2, 1960-today"
            },
            {
            "auteur": "Walter Isaacson",
            "date_publication": "Tue, 19 Mar 2019 00:00:00 GMT",
            "editeur": "Quanto",
            "id": 3,
            "id_categorie": 1,
            "isbn": "978-2-8891-5263-6",
            "titre": "Léonard de Vinci"
            },
            {
            "auteur": "Mélanie Renaud",
            "date_publication": "Tue, 10 Sep 2019 00:00:00 GMT",
            "editeur": "First",
            "id": 4,
            "id_categorie": 1,
            "isbn": "978-2-4120-5977-7",
            "titre": "Le piano en 15 minutes par jour pour les Nuls mégapoche"
            },
            {
            "auteur": "Christophe Blain, Jean-Marc Jancovici",
            "date_publication": "Tue, 12 Oct 2021 00:00:00 GMT",
            "editeur": "Dargaud",
            "id": 5,
            "id_categorie": 2,
            "isbn": "978-2-2050-8816-8",
            "titre": "Le monde sans fin"
            },
            {
            "auteur": "Kohei Horikoshi",
            "date_publication": "Wed, 27 Jan 2021 00:00:00 GMT",
            "editeur": "Ki-oon",
            "id": 6,
            "id_categorie": 2,
            "isbn": "979-1-0327-1081-4",
            "titre": "My Hero Academia T31"
            },
            {
            "auteur": "Xavier Dorison",
            "date_publication": "Sat, 23 Oct 2021 00:00:00 GMT",
            "editeur": "Kana",
            "id": 7,
            "id_categorie": 2,
            "isbn": "978-2-5050-7846-3",
            "titre": "BD Goldorak"
            },
            {
            "auteur": "Masashi Kishimoto",
            "date_publication": "Thu, 13 Mar 2003 00:00:00 GMT",
            "editeur": "Kana",
            "id": 8,
            "id_categorie": 2,
            "isbn": "978-2-8712-9511-2",
            "titre": "Naruto, tome 6"
            },
            {
            "auteur": "Philippe Etchebest",
            "date_publication": "Tue, 12 Oct 2021 00:00:00 GMT",
            "editeur": "Albin Michel",
            "id": 9,
            "id_categorie": 3,
            "isbn": "978-2-2264-6454-5",
            "titre": "Cuisinez bien accompagné avec ma méthode Mentor: Méthode & recettes"
            },
            {
            "auteur": "Marie-Elodie Pape",
            "date_publication": "Wed, 04 Mar 2020 00:00:00 GMT",
            "editeur": "Dessain et Tolra",
            "id": 10,
            "id_categorie": 3,
            "isbn": "978-2-0359-7025-1",
            "titre": "Yaourts, desserts & cie à la yaourtière: Spécial multi délices"
            },
            {
            "auteur": "Bérengère Philippon",
            "date_publication": "Tue, 02 Feb 2021 00:00:00 GMT",
            "editeur": "Larousse",
            "id": 11,
            "id_categorie": 3,
            "isbn": "978-2-0359-9718-0",
            "titre": "Je réussis ma détox sucre: Comprenez et cuisinez IG bas au quotidien"
            },
            {
            "auteur": "Thibault Geoffray",
            "date_publication": "Wed, 12 Sep 2018 00:00:00 GMT",
            "editeur": "Marabout",
            "id": 12,
            "id_categorie": 3,
            "isbn": "978-2-5011-3634-1",
            "titre": "Mes recettes healthy: BIM ! Prends toi en main avec mes recettes fitfightforever"
            },
            {
            "auteur": "Clémence Maumené",
            "date_publication": "Sun, 12 Sep 2021 00:00:00 GMT",
            "editeur": "Albin Michel",
            "id": 13,
            "id_categorie": 3,
            "isbn": "978-2-2264-5998-5",
            "titre": "Cuisinez pour bébé"
            },
            {
            "auteur": "Maud Ankaoua",
            "date_publication": "Mon, 14 Oct 2019 00:00:00 GMT",
            "editeur": "J'ai lu",
            "id": 14,
            "id_categorie": 4,
            "isbn": "ISBN : 978-2-2902-1051-2",
            "titre": "Kilomètre zéro : Le chemin du bonheur"
            },
            {
            "auteur": "Charles Brasart",
            "date_publication": "Fri, 12 Mar 2021 00:00:00 GMT",
            "editeur": " Armand Colin",
            "id": 15,
            "id_categorie": 5,
            "isbn": "978-2-2006-2660-0",
            "titre": "L'essentiel de la grammaire anglaise"
            },
            {
            "auteur": "Yann-Gaël Menais",
            "date_publication": "Tue, 12 Oct 2021 00:00:00 GMT",
            "editeur": "Gereso",
            "id": 16,
            "id_categorie": 6,
            "isbn": "979-1-0397-0005-4",
            "titre": "Perfectionner ses méthodes de vente"
            },
            {
            "auteur": "Frédéric Laloux",
            "date_publication": "Wed, 07 Oct 2015 00:00:00 GMT",
            "editeur": "Diateino",
            "id": 17,
            "id_categorie": 6,
            "isbn": "978-2-3545-6105-5",
            "titre": "Reinventing Organizations: Vers des communautés de travail inspirées"
            },
            {
            "auteur": "Christophe Bourseiller",
            "date_publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "editeur": "Cerf",
            "id": 18,
            "id_categorie": 7,
            "isbn": "978-2-2041-4513-8",
            "titre": "Le complotisme, anatomie d'une religion"
            },
            {
            "auteur": "Edith Tavignot",
            "date_publication": "Tue, 29 Dec 2020 00:00:00 GMT",
            "editeur": "Particulier",
            "id": 19,
            "id_categorie": 8,
            "isbn": "978-2-3573-1296-8",
            "titre": "Tutelle, curatelle : Protéger un proche"
            },
            {
            "auteur": "Dominique Lormier",
            "date_publication": "Sun, 27 Sep 2020 00:00:00 GMT",
            "editeur": "Editions du Rocher",
            "id": 20,
            "id_categorie": 9,
            "isbn": "978-2-2681-0416-4",
            "titre": "Les vérités cachées de la Seconde Guerre mondiale"
            },
            {
            "auteur": "Jean-François Solnon",
            "date_publication": "Sun, 30 Jan 2022 00:00:00 GMT",
            "editeur": "Perrin",
            "id": 21,
            "id_categorie": 9,
            "isbn": "978-2-2620-8455-4",
            "titre": "Anne d'Autriche"
            },
            {
            "auteur": "Alain-Julien Rudefoucauld",
            "date_publication": "Sat, 11 Dec 2021 00:00:00 GMT",
            "editeur": "Esprit du Temps",
            "id": 22,
            "id_categorie": 9,
            "isbn": "978-2-8479-5542-2",
            "titre": "Les portes de l'enfer, la répression légale du citoyen sous Vichy"
            },
            {
            "auteur": "Eric David",
            "date_publication": "Sun, 26 Dec 2021 00:00:00 GMT",
            "editeur": "Racine Be",
            "id": 23,
            "id_categorie": 9,
            "isbn": "978-2-3902-5138-5",
            "titre": "Le procès de Nuremberg"
            },
            {
            "auteur": "Laurent Ruquier",
            "date_publication": "Fri, 07 May 2021 00:00:00 GMT",
            "editeur": "Flammarion",
            "id": 24,
            "id_categorie": 10,
            "isbn": "978-2-0802-5605-8",
            "titre": "Finement Con"
            },
            {
            "auteur": "Robert C. Martin",
            "date_publication": "Fri, 20 Nov 2020 00:00:00 GMT",
            "editeur": "Pearson",
            "id": 25,
            "id_categorie": 11,
            "isbn": "978-2-3260-0267-8",
            "titre": "Architecture logicielle propre"
            },
            {
            "auteur": "Lycia Diaz",
            "date_publication": "Wed, 18 Nov 2020 00:00:00 GMT",
            "editeur": "Eyrolles",
            "id": 26,
            "id_categorie": 11,
            "isbn": "978-2-4160-0067-6",
            "titre": "Je crée mon site avec WordPress. De l'hébergement à la promotion"
            },
            {
            "auteur": "Daniel Ichbiah",
            "date_publication": "Mon, 17 Feb 2020 00:00:00 GMT",
            "editeur": "First Interactive",
            "id": 27,
            "id_categorie": 11,
            "isbn": "978-2-4120-5415-4",
            "titre": "Guide d'autodéfense sur Internet"
            },
            {
            "auteur": "Bertrand Jouvenot",
            "date_publication": "Sat, 14 Sep 2019 00:00:00 GMT",
            "editeur": "Eyrolles",
            "id": 28,
            "id_categorie": 11,
            "isbn": "978-2-2126-7785-0",
            "titre": "Dopez votre stratégie digitale: 72 fiches pratiques"
            },
            {
            "auteur": " Marion Giroudon",
            "date_publication": "Sun, 27 Oct 2019 00:00:00 GMT",
            "editeur": "Gualino",
            "id": 29,
            "id_categorie": 11,
            "isbn": "978-2-2970-7357-8",
            "titre": "Créer une présence efficace et rentable sur Internet"
            },
            {
            "auteur": "Patrick Engebretson",
            "date_publication": "Thu, 22 Nov 2018 00:00:00 GMT",
            "editeur": "Pearson",
            "id": 30,
            "id_categorie": 11,
            "isbn": "978-2-7440-6723-5",
            "titre": "Hacker's box : Se protéger... et contre-attaquer !"
            },
            {
            "auteur": "Michelle Jean-Baptiste",
            "date_publication": "Tue, 21 Aug 2018 00:00:00 GMT",
            "editeur": "Nathan",
            "id": 31,
            "id_categorie": 11,
            "isbn": "978-2-0916-5179-8",
            "titre": "Créer son e-commerce"
            },
            {
            "auteur": "Henri Laude",
            "date_publication": "Wed, 20 Jun 2018 00:00:00 GMT",
            "editeur": "Editions ENI",
            "id": 32,
            "id_categorie": 11,
            "isbn": "978-2-4090-1397-3",
            "titre": "Data Scientist et langage R"
            },
            {
            "auteur": "Hervé Le Morvan",
            "date_publication": "Wed, 23 May 2018 00:00:00 GMT",
            "editeur": "Epsilon",
            "id": 33,
            "id_categorie": 11,
            "isbn": "978-2-4090-1384-3",
            "titre": "Java Spring - Le socle technique des applications Java EE"
            },
            {
            "auteur": "Eric Lalitte",
            "date_publication": "Mon, 01 Jan 2018 00:00:00 GMT",
            "editeur": "Eyrolles",
            "id": 34,
            "id_categorie": 11,
            "isbn": "978-2-2126-7477-4",
            "titre": "Apprenez le fonctionnement des réseaux TCP/IP"
            },
            {
            "auteur": "Fanny Abadie",
            "date_publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "editeur": "Syros Jeunesse",
            "id": 35,
            "id_categorie": 12,
            "isbn": "978-2-7485-3046-9",
            "titre": "Vous retiendrez mon nom"
            },
            {
            "auteur": "Ariana Godoy",
            "date_publication": "Fri, 02 Sep 2022 00:00:00 GMT",
            "editeur": "Hachette Romans",
            "id": 36,
            "id_categorie": 13,
            "isbn": "978-2-0171-4772-5",
            "titre": "À travers ma fenêtre"
            },
            {
            "auteur": "Rebecca Zanetti",
            "date_publication": "Thu, 01 Jul 2021 00:00:00 GMT",
            "editeur": "Milady",
            "id": 37,
            "id_categorie": 14,
            "isbn": "978-2-8112-2168-3",
            "titre": "Dark Protectors, T5 : Kane"
            },
            {
            "auteur": "Lisa Gardner",
            "date_publication": "Fri, 12 Nov 2021 00:00:00 GMT",
            "editeur": "Le livre de Poche",
            "id": 38,
            "id_categorie": 15,
            "isbn": "978-2-2531-8164-4",
            "titre": "La Fille cachée"
            },
            {
            "auteur": "Mike Nicol",
            "date_publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "editeur": "Gallimard",
            "id": 39,
            "id_categorie": 15,
            "isbn": "978-2-0729-0598-8",
            "titre": "Infiltrée"
            },
            {
            "auteur": "Lotte Hammer",
            "date_publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "editeur": "Actes Sud",
            "id": 40,
            "id_categorie": 15,
            "isbn": "978-2-3301-5992-4",
            "titre": "Le Polonais fou"
            },
            {
            "auteur": "François-Xavier Durrwell",
            "date_publication": "Mon, 08 Nov 2021 00:00:00 GMT",
            "editeur": "Cerf",
            "id": 41,
            "id_categorie": 16,
            "isbn": "978-2-2041-4056-0",
            "titre": "La Trinité"
            },
            {
            "auteur": "Anne Ancelin Schützenberger",
            "date_publication": "Sat, 02 Feb 2002 00:00:00 GMT",
            "editeur": "Editions Payot & Rivages",
            "id": 42,
            "id_categorie": 17,
            "isbn": "978-2-2289-3018-5",
            "titre": "Le psychodrame"
            },
            {
            "auteur": "Kip Thorne",
            "date_publication": "Wed, 14 Sep 2022 00:00:00 GMT",
            "editeur": "Flammarion",
            "id": 43,
            "id_categorie": 18,
            "isbn": "978-2-0802-6877-8",
            "titre": "Trous noirs et distorsions du temps"
            },
            {
            "auteur": "Thierry Courtin",
            "date_publication": "Tue, 10 Aug 2021 00:00:00 GMT",
            "editeur": "Nathan",
            "id": 44,
            "id_categorie": 19,
            "isbn": "978-2-0919-3555-3",
            "titre": "T'choupi Mon cahier ardoise - Ma moyenne section - dès 4 ans"
            },
            {
            "auteur": "David Bry",
            "date_publication": "Thu, 12 Jun 2014 00:00:00 GMT",
            "editeur": "Pocket",
            "id": 45,
            "id_categorie": 20,
            "isbn": "978-2-2663-2212-6",
            "titre": "La Princesse au visage de nuit"
            },
            {
            "auteur": "Jacob Aagaard",
            "date_publication": "Sat, 10 Apr 2021 00:00:00 GMT",
            "editeur": "Olibris",
            "id": 46,
            "id_categorie": 21,
            "isbn": "979-1-0971-4032-8",
            "titre": "Attaque et défense aux échecs"
            },
            {
            "auteur": "Molière",
            "date_publication": "Sat, 19 Nov 2022 00:00:00 GMT",
            "editeur": "Flammation",
            "id": 47,
            "id_categorie": 22,
            "isbn": "978-2-0802-6880-8",
            "titre": "Le misanthrope"
            },
            {
            "auteur": "Tom Masters",
            "date_publication": "Tue, 18 Jan 2022 00:00:00 GMT",
            "editeur": "Lonely Planet",
            "id": 48,
            "id_categorie": 23,
            "isbn": "978-1-7886-8824-6",
            "titre": "Lonely Planet Georgia, Armenia & Azerbaijan"
            }
            ],
            "success": true,
            "total_books": 48
        }
  
      
  
 

. ## DELETE/livres        

    GENERAL: Delete the Livre of the given ID if it exists. Return the Livre object deleted, success value and the total of Livre that remains.             
    SAMPLE: curl -X DELETE http://localhost:5000/livres/13
        {
            "book": {
                "auteur": "Clémence Maumené",
                "date_publication": "Sun, 12 Sep 2021 00:00:00 GMT",
                "editeur": "Albin Michel",
                "id": 13,
                "id_categorie": 3,
                "isbn": "978-2-2264-5998-5",
                "titre": "Cuisinez pour bébé"
            },
            "deleted_id": 13,
            "success": true,
            "total_books": 47
        }

. ##PATCH/livres/id

  GENERAL: This endpoint is used to update a certain property of Livre. Then, We return a Livre which we update and show the property modified.                  
  SAMPLE: curl -X PATCH http://localhost:5000/livres/12-H "Content-Type:application/json" -d "{"editeur": "Marabout"}"            
      {
          "book": {
              "auteur": "Thibault Geoffray",
              "date_publication": "Wed, 12 Sep 2018 00:00:00 GMT",
              "editeur": "Marabout",
              "id": 12,
              "id_categorie": 3,
              "isbn": "978-2-5011-3634-1",
              "titre": "Mes recettes healthy: BIM ! Prends toi en main avec mes recettes fitfightforever"
          },
          "info_edited": [
              "editeur"
          ],
          "success": true
      }
   
