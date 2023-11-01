from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


#============================================== Définition de la classe Hopital ====================================================#

class Hopital:
    def __init__(self, root):
        #========== Définition de la fenêtre =========================#
        self.root = root
        self.root.title("Hopital Les Génies Management System")
        self.root.geometry("1540x800+0+0")

        #=========== Déclaration des variables ========================#
        self.service = StringVar()
        self.numeroDImmatriculation = StringVar()
        self.nom = StringVar()
        self.prenom = StringVar()
        self.adresse = StringVar()
        self.age = StringVar()
        self.sexe = StringVar()
        self.descriptionDeLaMaladie = StringVar()
        self.numeroDeLaChambre = StringVar()
        self.specialiteDuMedecin = StringVar()
        self.coordoneeDuMedecin = StringVar()
        self.date = StringVar()
        self.heure = StringVar()
        self.nombreDeNuits = StringVar()



#================== Déclaration de notre TKinter====================+++
root = Tk()
ob = Hopital(root)
root.mainloop()
