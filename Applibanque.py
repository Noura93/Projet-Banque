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
            print("l'employé a été ajouter à la liste des employés",emp.nom,emp.prenom)
        
        else:
            print("l'employé est deja dans la liste ")


    def print_emps(self):
        for emp in self.employes:
            print("la liste des employés est",emp.nom,emp.prenom)

            
           
    def supprimer_employe(self,matricule):
        for i in self.employes:
            if matricule == i.matricule:
                self.employes.remove(i)
                print("le numéro de matricule a été supprimé de la liste des employés",matricule)
                break 


    def ajouter_clients(self,clts):
        if clts not in self.clients:
            self.clients.append(clts)
            print ("le client a été ajouté à la liste des clients",clts.nom,clts.prenom)

    
    def print_clients(self):
        for clts in self.clts:
            print ("la liste des employés est",clts.nom,clts.prenom)


    def supprimer_clients(self,numero_de_compte):
        for j in self.clients:
            if numero_de_compte == j.numero_de_compte:
                self.clients.remove(j)
                print("le numéro de compte clients a été supprimer de la liste des clients",numero_de_compte)      
               
    
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


class clients:
    def __init__(self):
        Personne.__init__(self)
        self.adresse = ''
        self.numero_de_compte = ''



    def saisie1 (self,nom,prenom,date_de_naissance,adresse,numero_de_compte):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.adresse = adresse
        self.numero_de_compte = numero_de_compte










       

       





