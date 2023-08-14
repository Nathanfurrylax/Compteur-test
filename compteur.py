class Compteur:
    def __init__(self, valeur_initiale=0):
        self.valeur = valeur_initiale
    
    def incrementer(self):
        self.valeur += 1
    
    def decrementer(self):
        self.valeur -= 1
    
    def reinitialiser(self):
        self.valeur = 0
    
    def obtenir_valeur(self):
        return self.valeur

# Exemple d'utilisation
compteur = Compteur()

print("Valeur initiale:", compteur.obtenir_valeur())

compteur.incrementer()
compteur.incrementer()
print("Après incrémentation:", compteur.obtenir_valeur())

compteur.decrementer()
print("Après décrémentation:", compteur.obtenir_valeur())

compteur.reinitialiser()
print("Après réinitialisation:", compteur.obtenir_valeur())
