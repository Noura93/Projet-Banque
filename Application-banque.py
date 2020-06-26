# coding: utf-8
class Banque:
    def __init__(self,nom_banque,adresse_banque,telephone_banque,employes,clients):
        self.nom = nom_banque
        self.adresse = adresse_banque
        self.telephone = telephone_banque
        self.employes = list
        self.clients = []

    
class Personne:
    def __init__(self,nom_personne,prenom_personne,date_de_naissance_personne):
        self.nom = nom_personne
        self.prenom = prenom_personne
        self.date_de_naissance = date_de_naissance_personne


class Employés(Personne):
    def __init__(self,nom_employes,prenom_employes,date_de_naissance_employes,adresse_employes,matricule):
        super(self,nom_employes,prenom_employes,date_de_naissance_employes)
        self.adresse = adresse_employes
        self.matricule = list

    def saisie(self):
        self.nom = input("veuillez saisir le nom de l'employé")
        self.prenom = input("veuillez saisir le prénom de l'employé")
        self.date_de_naissance = input("veuillez saisir la date de naissance de l'employé")
        self.adresse = input("veuillez saisir l'adresse de l'employé")
        self.matricule = int(input("veuillez saisir le numéro de matricule de l'employé"))

    def affichage(self):
        print("l'employé",self.nom,self.prenom,"né(e) le ",self.date_de_naissance,"domicilié(e) à l'adresse suivante :",self.adresse,"à été ajouté à la liste",list,"des employés")

    def licencier(self):
        print("l'employé, ayant le numéro de matricule:",self.matricule,"a été supprimé de la",list, "des employés")

    def ajouter(self):
        for i in employes:
            a.saisie
            list.append(a)
        print(self.employes)
        
        
class Clients(Personne):
    def __init__(self,nom_clients,prenom_clients,date_de_naissance_clients,adresse_clients,numero_compte_clients):
        super(self,nom_clients,prenom_clients,date_de_naissance_clients)
        self.numero_compte = numero_compte_clients



class compte:
    def __init__(self,numero_client,solde):
        self.numero = numero_client
        self.solde = solde



