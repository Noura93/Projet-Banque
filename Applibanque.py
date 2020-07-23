class Banque:
    def __init__(self,nom_banque,adresse_banque,telephone_banque):
        self.nom = nom_banque
        self.adresse = adresse_banque
        self.telephone = telephone_banque
        self.employes = []
        self.clients = []


    def ajouter_employe(self,emp):
        if emp not in self.employes:
            self.employes.append(emp)
            print("l'employé a été ajouter à la liste des employés",emp.nom)
        
        else:
            print("l'employé est deja dans la liste ")


    def print_emps(self,emp):
        for emp in self.employes:
            print("la liste des employés est",emp.nom)
            
           

    def supprimer_employe(self,matricule):
        mat = input("veuillez entrez le numéro de matricule que vous souhaitez supprimer")
        employes = []
        for i in matricule:
            if matricule in self.employes:
                self.employes.remove(matricule)
                print("le numéro de matricule a été supprimé de la liste des employés",emp.matricule)
                print(i)
            else:
                print("le numéro de matricule ne se trouve plus dans la liste des employés")  
    
    
class Personne:
    def __init__(self):
        self.nom = ''
        self.prenom = ''
        self.date_de_naissance = '' 


class Employes(Personne):

    def __init__(self):
        Personne.__init__(self)
        self.adresse = ''
        self.matricule = ''

             
    def saisie(self):
        self.nom = input("veuillez saisir le nom de l'employé")
        self.prenom = input("veuillez saisir le prénom de l'employé")
        self.date_de_naissance = input("veuillez saisir la date de naissance de l'employé")
        self.adresse = input("veuillez saisir l'adresse de l'employé")
        self.matricule = int(input("veuillez saisir le numéro de matricule de l'employé"))

