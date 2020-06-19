class Banque:
    def __init__(self,Nom_Banque,Adresse_Banque,Téléphone,Employés,Clients):
        self.nom = Nom
        self.adresse = Adresse
        self.téléphone = Téléphone
        self.employés = Employés
        self.clients = Clients

class Employés(Banque):
    def __init__(self,Nom_Employés,Prénom_Employés,Date_de_naissance,Adresse_Employés,Matricule):
        Banque.__init__(self,Nom_Employés,Adresse_Employés)
        self.prénom = Prénom
        self.date_de_naissance = Date_de_naissance
        self.matricule = Matricule



class Clients(Banque):
    def __init__(self,Nom_clients,Prénom_clients,Adresse_clients,Numero_compte):
        Banque.__init__(self,Nom_clients,Prénom_clients,Adresse_clients)
        self.numéro_compte = Numero_compte



class compte:
    def __init__(self,Numéro_client,Solde):
        self.Numéro = Numéro_client
        self.solde = Solde




