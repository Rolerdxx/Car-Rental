
# Application de location de voitures


Nous visons à développer une application de gestion de location de voiture.

✔ Nous avons utilisé une approche orientée objet pour faciliter la maintenance et l'évolutivité du code.

✔ Nous stockons les informations sur la voiture et l'utilisateur dans une base de données relationnelle.

✔ Nous avons créé une interface utilisateur conviviale pour faciliter l'utilisation de l'application.


## Fonctionnalités

➖ L'application permet aux utilisateurs de créer un compte avec un e-mail et un mot de passe. Elle vérifie l'e-mail en lui envoyant un code.

➖ Permet aux utilisateurs de se connecter avec leur email et leur mot de passe.

➖ Permet aux utilisateurs de réinitialiser leur mot de passe à l'aide de leur adresse e-mail.

➖ Affiche les voitures avec tous les détails dans la page principale.

➖ L'utilisateur peut filtrer les voitures par marque, modèle, carburant, lieux, transmission ou prix par jour.

➖ l'utilisateur peut sélectionner une voiture, aller sur sa page et la réserver.
## Auteurs

- [@Bilal Motassim](https://www.github.com/Rolerdxx)
- [@Hamza Elbouzidi](https://www.github.com/Hamza-Elbouzidi)
- [@Yahya Fekrane](https://www.github.com/YaHyA-FK)


## Installation

Installer l'environnement virtuel python:

```bash
  python3 -m venv venv
```

Exécutez l'environnement virtuel:

```bash
  ./venv/Scripts/activate
```

si vous rencontrez une erreur d'autorisation, exécutez cette commande et réessayez:

```bash
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Lorsque vous êtes dans l'environnement virtuel, exécutez la commande suivante pour installer tous les packages:

```bash
  pip install -r requirements.txt
```

Importez ceci dans la base de données sur votre serveur mysql:

- [CarRental](https://drive.google.com/file/d/1eN3Br_AKC32_MxGc4jAwT8MxK_w7zsWx/view?usp=sharing)

Pour exécuter ce projet, vous devrez ajouter les variables d'environnement suivantes à votre fichier .env :

- [.env](https://drive.google.com/file/d/1608vGivclNjdVUZhPBUzuGLRsOoqVt_r/view?usp=share_link)

Exécutez l'application:

```bash
  py main.py
```


    



## Diagramme de cas d'utilisation

![](https://i.imgur.com/Nm6Hx2Y.png)

## Diagramme de classe

![](https://i.imgur.com/JjoBUPf.png)

## Consultaion des voitures
Diagramme de sequence:
![](https://i.imgur.com/HBH13wT.png)

lorsque l'utilisateur ouvre l'application, il demande toutes les voitures de `mysql` et les affiche dans un `TableWidget`

![](https://i.imgur.com/JFBIW9p.png)

La fonction qui récupère toutes les voitures de la base de données:

```bash
def getallcars(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT id,image,marque,modele,carburant,places,transmission,state,prixParJour FROM voiture")
    return mycursor.fetchall()
```

La fonction qui affiche les données dans le `TableWidget`, la fonction `getImageLabel` Transforme les octets de l'image en une `QLabel` qui peut être affichée dans le tableau:

```bash
def showdata(self, cars):
        for row_number, row_data in enumerate(cars):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                if column_number == 1:
                    item = getImageLabel(self, column_data)
                    self.tableWidget.setCellWidget(row_number, column_number, item)
                elif column_number == 7:
                    if item == "1":
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem("Available"))
                    else:
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem("Reserved"))
                else:
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
        self.tableWidget.verticalHeader().setDefaultSectionSize(80)
```

## Filtrage
![](https://i.imgur.com/pkr6vzp.png)
### le Remplissage des QComboBox :
Pour remplir les QComboBox, nous avons décidé d'utiliser les données de ces champs à travers la base de données afin d'afficher uniquement les options disponibles dans notre base de données. Pour cela, nous avons utilisé une requête SQL SELECT DISTINCT pour obtenir toutes les marques présentes dans la base de données en éliminant les doublons.

```bash
def getallmarques(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT distinct marque FROM voiture where marque IS NOT NULL")
    return mycursor.fetchall()
```
```bash
def loadparametrs(self):
    marque = self.marque
    carburant = self.carburant
    transmission = self.transmission
    marques = self.db.getmarques()
    transmissions = self.db.gettransmissions()
    carburants = self.db.getcarburants()
    for choice in marques:
        marque.addItem(choice[0])
    for choice in transmissions:
        transmission.addItem(choice[0])
    for choice in carburants:
        carburant.addItem(choice[0])
```
Ce code remplit les options de trois QComboBox à partir des données de la base de données. Les marques, transmissions et carburants disponibles dans la base de données sont récupérés en appelant les méthodes correspondantes sur l'objet "self.db", puis chaque option est ajoutée

### Le Filtrage :

Pour le filtrage ona penser a utiliser une condition pour que le filtrage ne travaille que lorsque l’utilisateur choisir une option dans QComboBox ou taper des specifaction 

```bash
if marque == "none" and transmission == "none" and carburant == "none" and prix == "" and place == "" and modele == "":
```

si non le programme va prendre les donnees saisir par utilisateur est faire le traitement suivant :

```bash
def getsomecars(db, marque, modele, carburant, place, transmission, prix):
    mycursor = db.cursor()
    sql = "SELECT id,image,marque,modele,carburant,places,transmission,state,prixParJour FROM voiture WHERE"
    if marque != "none":
        sql += f" lower(marque) like '{marque.lower()}' AND"
    if modele != "":
        sql += f" lower(modele) like '{modele.lower()}' AND"
    if carburant != "none":
        sql += f" lower(carburant) like '{carburant.lower()}' AND"
    if place != "":
        sql += f" lower(places) like '{place.lower()}' AND"
    if transmission != "none":
        sql += f" lower(transmission) like '{transmission.lower()}' AND"
    if prix != "":
        sql += f" prixParJour <= {prix} AND"
    if sql.endswith("AND"):
        sql = sql[:-4]
        print(sql)
    mycursor.execute(sql)
    return mycursor.fetchall()

```
La fonction se connecte à la base de données en utilisant la connexion fournie (`db.cursor()`), puis construit une requête SQL qui sélectionne des voitures à partir de la table `voiture` en fonction des critères de recherche fournis. La requête commence par la chaîne de caractères `"SELECT id,image,marque,modele,carburant,places,transmission,state,prixParJour FROM voiture WHERE"`, qui sélectionne les colonnes `id`, `image`, `marque`, `modele`, `carburant`, `places`, `transmission`, `state` et `prixParJour` de la table `voiture`.
Ensuite, la fonction vérifie chaque critère de recherche pour voir s'il est renseigné ou non. Si un critère est renseigné, la fonction ajoute une condition à la requête SQL en utilisant la méthode `lower()` pour mettre en minuscule les valeurs de recherche et la clause `LIKE` pour chercher des correspondances partielles dans les colonnes de la table `voiture`. Si un critère n'est pas renseigné, la fonction ne l'ajoute pas à la requête SQL.
Enfin, si un prix maximum est fourni, la fonction ajoute une condition supplémentaire pour s'assurer que seules les voitures dont le `prixParJour` est inférieur ou égal à ce prix maximum sont sélectionnées.
Si la requête SQL se termine par la chaîne de caractères `"AND"`, la fonction la raccourcit en supprimant ces trois derniers caractères avec `sql = sql[:-4]`.
Enfin, la fonction exécute la requête SQL en utilisant la méthode `execute()` sur le curseur, puis retourne tous les résultats de la requête avec `fetchall()`. 

##  Reservation
### diagramme de sequence
![](https://i.imgur.com/NXvD684.png)
### Image:
![](https://i.imgur.com/lErxsOO.png)

Pour réserver une voiture, sélectionnez-la et cliquez sur le bouton Reserve.
```bash
def switchpage(self):
    if self.currentuser != "Guest":
        if self.selected is not None:
            carpage = CarPage(self)
            self.carpagecounter += 1
            self.widget.addWidget(carpage)
            self.widget.setCurrentIndex(self.carpagecounter)
        else:
            msgbox("Error", "Select a car")
    else:
        msgbox("Error", "You have to sign in")
```

Cette méthode vérifie si un utilisateur est connecté ou non, et si une voiture a été sélectionnée avant de basculer vers une page de voiture `CarPage` dans une application avec une structure à onglets `QTabWidget`.
Le cas où un utilisateur n'est pas connecté `self.currentuser == "Guest"` est géré avec un message d'erreur indiquant qu'il doit se connecter pour continuer. Le cas où une voiture n'est pas sélectionnée `self.selected is None` est également géré avec un message d'erreur indiquant qu'une voiture doit être sélectionnée pour continuer.
Après la vérification, le programme affiche les informations de la voiture sélectionnée.


![](https://i.imgur.com/LaTwqFh.png)

🏠 BACK BUTTON :

Ce bouton sert à retourner à la page principale

📝 RESERVE IT :

Ce buton sert a réserver la voiture sélectionnée 

Apres le système affiche ce QDialog :

![](https://i.imgur.com/E4W8tMf.png)

```bash
def reserveit(self):
    state = str(self.car[7])
    if state == "1":
        revdialog = ReservationDialog()
        res = revdialog.exec()
        if res:
            days = revdialog.getDays()
            user = self.main.currentuser[0]
            carid = self.car[0]
            priceperday = self.car[8]
            rescon = ResCon(float(priceperday)*float(days))
            res2 = rescon.exec()
            if res2:
                self.main.db.reservation(carid, user, priceperday, days)

```

```bash
def savereservation(db,carid,userid,priceperday,nbrDays):
    cursor = db.cursor()
    prix=calculTotalPrice(int(nbrDays),float(priceperday))
    sql = f"insert into reservations(date,nbrDays,iduser,idvoiture,prix) values(now(),{nbrDays},{userid},{carid},{prix}) "
    cursor.execute(sql)
    db.commit()

```

![](https://i.imgur.com/2z9MWSc.png)

La première ligne de code extrait la statut du voiture et le stocke dans la variable `state`.
La condition suivante vérifie si la variable `state` est égale à la chaîne de caractères `1`. signifie que la voiture est disponible. Si la voiture est disponible, une boîte de dialogue de réservation `ReservationDialog` est créée et affichée à l'utilisateur.
Si l'utilisateur clique sur `OK` dans la boîte de dialogue de réservation, la méthode récupère le nombre de jours sélectionnés dans la boîte de dialogue à l'aide de la méthode `getDays()` de l'objet `revdialog`. Ensuite, la méthode utilise les informations stockées dans `currentuser`, ` carID`, et la variable `days` pour ajouter une réservation à la base de données.
Avant d'ajouter la réservation, une autre boîte de dialogue est affichée pour confirmer le coût total de la réservation `ResCon`. Si l'utilisateur confirme le coût total en cliquant sur `OK`, la méthode ajoute la réservation en appelant la méthode `reservation` de l'objet `self.main.db` avec les informations nécessaires.

la fonction `savereservation` permet d'ajouter une nouvelle réservation à la base de données en calculant le coût total de la réservation `calculTotalPrice`, en créant une requête SQL et en exécutant cette requête en utilisant un curseur sur la connexion à la base de données.

```bash
def reservation(self,carid,userid,priceperday,nbrDays):
    changestate(self.db,carid,True)
    return savereservation(self.db,carid,userid,priceperday,nbrDays)
```

N'oublions pas le changement de l'état de cette voiture à travers la fonction 'changestate', qui prend en paramètre la variable de la base de données et l'identifiant de la voiture ainsi que l'état à affecter.


```bash
def changestate(db,carid,number):
    mycursor = db.cursor()
    if number:
        sql=f"UPDATE voiture SET state = '0' WHERE id ={carid}"
        mycursor.execute(sql)
        db.commit()
    else:
        sql=f"UPDATE voiture SET state = '1' WHERE id ={carid}"
        mycursor.execute(sql)
        db.commit()
```

La fonction commence par créer un curseur pour exécuter des requêtes `SQL` sur la base de données. Ensuite, elle utilise une instruction SQL pour mettre à jour l'état de la voiture dans la table `voiture` de la base de données en fonction de la valeur de `number` : si `number` est ` True ` , la voiture est marquée comme disponible `state = '1'`, sinon elle est marquée comme indisponible `state = '0'`. La fonction exécute ensuite la requête SQL à travers le curseur et committe les modifications apportées à la base de données.


## Verifier les Reservation :
### diagramme de sequence:
![](https://i.imgur.com/dsknqv5.png)

Avant chaque consultation des voitures, le système vérifie si toutes les réservations sont valides  a l’aide de :

```bash
def loaddata(self):
    self.cars = self.db.getallcars()
    carids = [self.cars[0] for self.cars in self.cars]
    for car in carids:
        self.db.checkCarState(int(car))
    self.cars = self.db.getallcars()
    self.showdata(self.cars)
```

Ce fragment de code permet de mettre à jour l'état de toutes les voitures dans une base de données a l’aide d’une boucle qui va parcourir tous les identifiants des voitures stockées dans `carids`. `checkCarState` est appelée avec l'identifiant de la voiture `car` en tant qu'argument, ce qui permet de mettre à jour l'état de la voiture dans la base de données. pour chaque voiture stockée dans la base de données, puis de récupérer la liste complète des voitures après la mise à jour. 


```bash
def checkCarState(self,carid):
    dateFN=getDayOfResevationEnd(self.db,carid)
    if dateFN :
        currentDate = datetime.now().date()
        if currentDate >= dateFN:
            changestate(self.db,carid,False)
ReservationDelete(self.db,carid)

        else:
            print("car reserved !!!")
```


La méthode `checkCarState` vérifie si une voiture est réservée ou non en fonction de sa date de fin de réservation `dateFN`. Elle prend en paramètre l'identifiant de la voiture `carid` dont l'état sera vérifié.
La première étape de la méthode est d'appeler la fonction `getDayOfReservationEnd` pour récupérer la date de fin de réservation de la voiture. 

```bash
def getDayOfResevationEnd(db,carid):
    cursor = db.cursor()
    sql=f"select nbrDays,DATE_FORMAT(date, '%d-%m-%Y') from reservations where idvoiture={carid}"
    cursor.execute(sql)
    table=cursor.fetchall()
    if len(table)!= 0 :
        date=table[0][1]
        nbrDays=table[0][0]
        dateFN = datetime.strptime(date, '%d-%m-%Y').date()
        newDateFN = dateFN + timedelta(days=nbrDays)
        return newDateFN
```


La fonction exécute une requête SQL pour récupérer les informations de réservation associées à la voiture. Si une réservation existe pour cette voiture, la fonction extrait le nombre de jours de location `nbrDays` et la date de début de la réservation `date` à partir du résultat de la requête. Elle calcule ensuite la date de fin de la réservation `newDateFN` en ajoutant le nombre de jours de location à la date de début de la réservation a l’aide de la function ` timedelta `.La fonction retourne la date de fin de la réservation `newDateFN` 
Si une date de fin de réservation existe, la méthode continue son traitement en vérifiant si cette date est passée ou non.
Si la date de fin de réservation est passée `c'est-à-dire que la date actuelle est supérieure ou égale à la date de fin de réservation`, la méthode appelle la fonction "changestate"qu’il était déjà mentionner dans la partie Reservation pour mettre à jour l'état de la voiture à indisponible `False` ainsi que la méthode appelle la fonction `ReservationDelete`.


```bash
def ReservationDelete(db,carid) :
    cursor = db.cursor()
    sql = f"DELETE FROM reservations WHERE idvoiture={carid}"
    cursor.execute(sql)
    db.commit()
```

La fonction ReservationDelete  supprime la ligne de la  `reservation` qui est l'identifiant de voiture donné en utilisant une instruction `SQL DELETE`.
Si la date de fin de réservation n'est pas encore passée, la méthode affiche simplement un message indiquant que la voiture est réservée.



## Screenshots

![](https://i.imgur.com/JFBIW9p.png)
![](https://i.imgur.com/LcRC9MH.png)
![](https://i.imgur.com/XIzKLz1.png)
![](https://i.imgur.com/sYJT80R.png)





