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

        # =========== Déclaration des variables ======================== #
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
        labeltitle = Label(
            self.root,
            bd=20,
            relief=RIDGE,
            text="HOPITAL LES GÉNIES MANAGEMENT SYSTEM",
            fg="red",
            bg="white",
            font=("times new roman", 50, "bold"),
        )
        labeltitle.pack(side=TOP, fill=X)

        # =============================================== DataFrame ========================================================= #
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1440, height=400)

        DataframeLeft = LabelFrame(
            Dataframe,
            bd=10,
            relief=RIDGE,
            padx=10,
            font=("times new roman", 17, "bold"),
            text="Informations du Patient",
        )
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(
            Dataframe,
            bd=10,
            relief=RIDGE,
            padx=10,
            font=("times new roman", 17, "bold"),
            text="Prescription",
        )
        DataframeRight.place(x=990, y=5, width=400, height=350)

        # =======================================Buttons frame============================================================== #
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1440, height=80)

        # =======================================Details frame============================================================== #
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1440, height=190)

        # =======================================DataframeLeft============================================================== #
        labelService = Label(
            DataframeLeft,
            text="Service",
            font=("arial", 15, "bold"),
            padx=2,
            pady=6,
        )
        labelService.grid(row=0, column=0, sticky=W)

        comboBoxService = ttk.Combobox(
            DataframeLeft,
            textvariable=self.service,
            state="readonly",
            font=("arial", 15, "bold"),
            width=33,
        )
        comboBoxService["value"] = (
            "Service de Consultation",
            "Service d'urgence"
        )
        comboBoxService.current(0)
        comboBoxService.grid(row=0, column=1)


# ================== Déclaration de notre TKinter====================#
root = Tk()
ob = Hopital(root)
root.mainloop()
