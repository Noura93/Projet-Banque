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
        for i in self.employes:
            if matricule == i.matricule:
                self.employes.remove(i)
                print("le numéro de matricule a été supprimé de la liste des employés",matricule)
                break   
            
    
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

             
    def saisie(self,nom,prenom,date_de_naissance,adresse,matricule):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.adresse = adresse
        self.matricule = matricule

