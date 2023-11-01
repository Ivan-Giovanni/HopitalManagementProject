from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


# ============================================== Définition de la classe Hopital =============================================== #

class Hopital:
    def __init__(self, root):
        # ==================================== Définition de la fenêtre ======================================================= #
        self.root = root
        self.root.title("Hopital Les Génies Management System")
        self.root.geometry("1540x800+0+0")

        # =========== Déclaration des variables ========================#
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

        # =========== Table de la fin de la fenêtre ================= #
        self.hopitalTable = ttk.Treeview(
            columns=(
                "service",
                "numeroDImmatriculation",
                "nom",
                "prenom",
                "adresse",
                "age",
                "sexe",
                "descriptionDeLaMaladie",
                "numeroDeLaChambre",
                "specialiteDuMedecin",
                "coordoneeDuMedecin",
                "date",
                "heure",
                "nombreDeNuits",
            ),
        )

        # =========== On formatte le titre ========================= #
        lbltitle = Label(
            self.root,
            bd=20,
            relief=RIDGE,
            text="HOPITAL LES GÉNIES MANAGEMENT SYSTEM",
            fg="red",
            bg="white",
            font=("times new roman", 50, "bold"),
        )
        lbltitle.pack(side=TOP, fill=X)

        # =============================================== DataFrame ========================================================= #


# ================== Déclaration de notre TKinter====================#
root = Tk()
ob = Hopital(root)
root.mainloop()
