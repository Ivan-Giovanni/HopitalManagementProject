from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


# ============================================== Définition de la classe Hopital ============================================= #

class Hopital:
    def __init__(self, root):
        # ==================================== Définition de la fenêtre ====================================================== #
        self.root = root
        self.root.title("Hopital Les Genies Management System")
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
        self.hospitalTable = ttk.Treeview(
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
                "description"
            ),
        )

        # =========== On formatte le titre ========================= #
        labeltitle = Label(
            self.root,
            bd=20,
            relief=RIDGE,
            text="HOPITAL LES GENIES MANAGEMENT SYSTEM",
            fg="red",
            bg="white",
            font=("times new roman", 50, "bold"),
        )
        labeltitle.pack(side=TOP, fill=X)

        # =============================================== DataFrame ========================================================= #
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=100, width=1440, height=350)

        DataframeLeft = LabelFrame(
            Dataframe,
            bd=10,
            relief=RIDGE,
            padx=10,
            font=("times new roman", 17, "bold"),
            text="Informations du Patient",
        )
        DataframeLeft.place(x=0, y=5, width=980, height=300)

        DataframeRight = LabelFrame(
            Dataframe,
            bd=10,
            relief=RIDGE,
            padx=10,
            font=("times new roman", 17, "bold"),
            text="Prescription",
        )
        DataframeRight.place(x=990, y=5, width=400, height=300)

        # =======================================SearchBar frame============================================================== #
        SearchBarframe = Frame(self.root, bd=20, relief=RIDGE)
        SearchBarframe.place(x=0, y=430, width=1440, height=70)

        # =======================================Buttons frame============================================================== #
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=500, width=1440, height=80)

        # =======================================Details frame============================================================== #
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=570, width=1440, height=220)

        # =======================================DataframeLeft============================================================== #
        # ===================================== #
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
            width=30,
        )
        comboBoxService["value"] = (
            "Service de Consultation",
            "Service d'urgence"
        )
        comboBoxService.current(0)
        comboBoxService.grid(row=0, column=1)

        # ===================================== #
        labelNumeroDImmatriculation = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="N° d'Immatriculation", padx=2
        )
        labelNumeroDImmatriculation.grid(row=1, column=0, sticky=W)
        texteNumeroDImmatriculation = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.numeroDImmatriculation, width=35
        )
        texteNumeroDImmatriculation.grid(row=1, column=1)

        # ===================================== #
        labelNom = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Nom", padx=2
        )
        labelNom.grid(row=2, column=0, sticky=W)
        texteNom = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.nom, width=35
        )
        texteNom.grid(row=2, column=1)

        # ===================================== #
        labelPrenom = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Prenom", padx=2
        )
        labelPrenom.grid(row=3, column=0, sticky=W)
        textePrenom = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.prenom, width=35
        )
        textePrenom.grid(row=3, column=1)

        # ===================================== #
        labelAdresse = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Adresse", padx=2
        )
        labelAdresse.grid(row=4, column=0, sticky=W)
        texteAdresse = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.adresse, width=35
        )
        texteAdresse.grid(row=4, column=1)

        # ===================================== #
        labelAge = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Age", padx=2
        )
        labelAge.grid(row=5, column=0, sticky=W)
        texteAge = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.age, width=35
        )
        texteAge.grid(row=5, column=1)

        # ===================================== #
        labelSexe = Label(
            DataframeLeft,
            text="Sexe",
            font=("arial", 15, "bold"),
            padx=2,
            pady=6,
        )
        labelSexe.grid(row=6, column=0, sticky=W)

        comboBoxSexe = ttk.Combobox(
            DataframeLeft,
            textvariable=self.sexe,
            state="readonly",
            font=("arial", 15, "bold"),
            width=30,
        )
        comboBoxSexe["value"] = (
            "Feminin",
            "Masculin"
        )
        comboBoxSexe.current(0)
        comboBoxSexe.grid(row=6, column=1)

        # ===================================== #
        labelDescriptionDeLaMaladie = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Description", padx=2
        )
        labelDescriptionDeLaMaladie.grid(row=0, column=2, sticky=W)
        textlDescriptionDeLaMaladie = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.descriptionDeLaMaladie, width=35
        )
        textlDescriptionDeLaMaladie.grid(row=0, column=3)

        # ===================================== #
        labelNumeroDeLaChambre = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="N° Chambre", padx=2
        )
        labelNumeroDeLaChambre.grid(row=1, column=2, sticky=W)
        texteNumeroDeLaChambre = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.numeroDeLaChambre, width=35
        )
        texteNumeroDeLaChambre.grid(row=1, column=3)

        # ===================================== #
        labelSpecialiteDuMedecin = Label(
            DataframeLeft,
            text="Specialite du Med.",
            font=("arial", 15, "bold"),
            padx=2,
            pady=6,
        )
        labelSpecialiteDuMedecin.grid(row=2, column=2, sticky=W)

        comboBoxSpecialiteDuMedecin = ttk.Combobox(
            DataframeLeft,
            textvariable=self.specialiteDuMedecin,
            state="readonly",
            font=("arial", 15, "bold"),
            width=30,
        )
        comboBoxSpecialiteDuMedecin["value"] = (
            "Gynecologie",
            "Chirurgie",
            "Gastrologie",
            "Radiologie",
            "Generale"
        )
        comboBoxSpecialiteDuMedecin.current(4)
        comboBoxSpecialiteDuMedecin.grid(row=2, column=3)

        # ===================================== #
        labelCoordonneDuMedecin = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Coordonnees du Med.", padx=2
        )
        labelCoordonneDuMedecin.grid(row=3, column=2, sticky=W)
        texteCoordonneDuMedecin = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.coordoneeDuMedecin, width=35
        )
        texteCoordonneDuMedecin.grid(row=3, column=3)

        # ===================================== #
        labelDate = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Date", padx=2
        )
        labelDate.grid(row=4, column=2, sticky=W)
        texteDate = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.date, width=35
        )
        texteDate.grid(row=4, column=3)

        # ===================================== #
        labelHeure = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Heure", padx=2
        )
        labelHeure.grid(row=5, column=2, sticky=W)
        texteHeure = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.heure, width=35
        )
        texteHeure.grid(row=5, column=3)

        # ===================================== #
        labelNombreDeNuits = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Nombre de nuits", padx=2
        )
        labelNombreDeNuits.grid(row=6, column=2, sticky=W)
        texteNombreDeNuits = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.nombreDeNuits, width=35
        )
        texteNombreDeNuits.grid(row=6, column=3)

        # ======================================= DataframeRight ================================================= #
        self.textePrescription = Text(
            DataframeRight,
            font=("arial", 14, "bold"),
            width=44,
            height=15,
            padx=2,
            pady=6,
        )
        self.textePrescription.grid(row=0, column=0)

        # ======================================= Boutons =========================================================== #
        # ===================================== #
        boutonEnregistrer = Button(
            Buttonframe,
            command=self.iEnregistrer,
            text="Enregistrer",
            bg="#00FF00",
            fg="blue",
            font=("arial", 12, "bold"),
            width=23,
            height=2,
        )
        boutonEnregistrer.grid(row=0, column=0)

        # ===================================== #
        boutonRechercher = Button(
            Buttonframe,
            text="Rechercher",
            bg="#00FF00",
            fg="blue",
            font=("arial", 12, "bold"),
            width=22,
            height=2,
        )
        boutonRechercher.grid(row=0, column=1)

        # ===================================== #
        boutonModifier = Button(
            Buttonframe,
            command=self.iModifier,
            text="Modifier",
            bg="#00FF00",
            fg="blue",
            font=("arial", 12, "bold"),
            width=23,
            height=2,
        )
        boutonModifier.grid(row=0, column=2)

        # ===================================== #
        optionsTrier = [
            "Tier par",
            "Alphabetique",
            "Urgence",
            "Externe",
            "Date"
        ]

        clicked = StringVar()
        clicked.set(optionsTrier[0])

        boutonTrier = Frame(Buttonframe, bd=5)
        boutonTrier.grid(row=0, column=3)

        dropTrier = OptionMenu(boutonTrier, clicked, *optionsTrier)
        dropTrier.config(height=1, width=23, fg="blue", font=("arial", 12, "bold"))
        dropTrier.pack()

        # ===================================== #
        boutonSupprimer = Button(
            Buttonframe,
            command=self.iSupprimer,
            text="Supprimer",
            bg="#00FF00",
            fg="blue",
            font=("arial", 12, "bold"),
            width=22,
            height=2,
        )
        boutonSupprimer.grid(row=0, column=4)

        # ===================================== #
        boutonCalculerDevis = Button(
            Buttonframe,
            text="Devis",
            bg="#00FF00",
            fg="blue",
            font=("arial", 12, "bold"),
            width=13,
            height=2,
        )
        boutonCalculerDevis.grid(row=0, column=5)

        # ===================================== #
        boutonQuitter = Button(
            Buttonframe,
            command=self.iQuitter,
            text="Quitter",
            bg="#00FF00",
            fg="blue",
            font=("arial", 12, "bold"),
            width=23,
            height=2,
        )
        boutonQuitter.grid(row=0, column=6)

        # ===================================== #
        optionsStatistiques = [
            "Afficher Stats",
            "Stat 1",
            "Stat 2",
            "Stat 3",
            "Stat 4"
        ]

        clicked = StringVar()
        clicked.set(optionsStatistiques[0])

        boutonAfficherStatistiques = Button(
            Buttonframe,
            text="Statistques",
            bg="#00FF00",
            fg="blue",
            font=("arial", 12, "bold"),
            width=22,
            height=2,
        )
        boutonAfficherStatistiques.grid(row=0, column=5)

        boutonTrier = Frame(Buttonframe, bd=5)
        boutonTrier.grid(row=0, column=5)

        dropStatistiques = OptionMenu(boutonTrier, clicked, *optionsStatistiques)
        dropStatistiques.config(height=1, width=23, fg="blue", font=("arial", 12, "bold"))
        dropStatistiques.pack()

        # =============================================== Hospital Table ==================================================== #
        # ================================================ ScrollBar ======================================================= #
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospitalTable = ttk.Treeview(
            Detailsframe,
            columns=(
                "numeroDImmatriculation",
                "nom",
                "prenom",
                "age",
                "sexe",
                "adresse",
                "service",
                "numeroDeChambre",
                "specialiteDuMedecin",
                "coordonnesDuMedecin",
                "date",
                "heure",
                "nombreDeNuits",
                "description"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospitalTable.xview)
        scroll_y = ttk.Scrollbar(command=self.hospitalTable.yview)

        self.hospitalTable.heading("numeroDImmatriculation", text="N° D'imma.")
        self.hospitalTable.heading("nom", text="Nom")
        self.hospitalTable.heading("prenom", text="Prenom")
        self.hospitalTable.heading("age", text="Age")
        self.hospitalTable.heading("sexe", text="Sexe")
        self.hospitalTable.heading("adresse", text="Adresse")
        self.hospitalTable.heading("service", text="Service")
        self.hospitalTable.heading("numeroDeChambre", text="N° Chambre")
        self.hospitalTable.heading("specialiteDuMedecin", text="Spe du Med.")
        self.hospitalTable.heading("coordonnesDuMedecin", text="Coor du Med.")
        self.hospitalTable.heading("date", text="Date")
        self.hospitalTable.heading("heure", text="Heure")
        self.hospitalTable.heading("nombreDeNuits", text="Nbre nuits")
        self.hospitalTable.heading("description", text="Description")

        self.hospitalTable["show"] = "headings"

        self.hospitalTable.pack(fill=BOTH, expand=1)

        self.hospitalTable.column("numeroDImmatriculation", width=100)
        self.hospitalTable.column("nom", width=100)
        self.hospitalTable.column("prenom", width=100)
        self.hospitalTable.column("age", width=100)
        self.hospitalTable.column("sexe", width=100)
        self.hospitalTable.column("adresse", width=100)
        self.hospitalTable.column("service", width=100)
        self.hospitalTable.column("numeroDeChambre", width=100)
        self.hospitalTable.column("specialiteDuMedecin", width=100)
        self.hospitalTable.column("coordonnesDuMedecin", width=100)
        self.hospitalTable.column("date", width=90)
        self.hospitalTable.column("heure", width=90)
        self.hospitalTable.column("nombreDeNuits", width=90)
        self.hospitalTable.column("description", width=100)

        self.hospitalTable.pack(fill=BOTH, expand=1)
        self.hospitalTable.bind("<ButtonRelease-1>", self.get_cursor)

    # ============================================ Declaration des fonctionnalites =========================================== #
    # =========================================================== #
    def iEnregistrer(self):  # les fontions qui commencent par i sont liées aux boutons
        if self.numeroDImmatriculation == "" or self.service == "":
            messagebox.showerror("Error", "Veuillez remplir tous les champs")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="GiovannI2004@",  # Utilise ton propre mot de passe
                database="nf06Hopital",  # Nomme exactement comme dans mySQL Workbench
            )
            myCursor = conn.cursor()

            myCursor.execute(
                "insert into nf06Hopital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.numeroDImmatriculation.get(),
                    self.nom.get(),
                    self.prenom.get(),
                    self.age.get(),
                    self.sexe.get(),
                    self.adresse.get(),
                    self.service.get(),
                    self.numeroDeLaChambre.get(),
                    self.specialiteDuMedecin.get(),
                    self.coordoneeDuMedecin.get(),
                    self.date.get(),
                    self.heure.get(),
                    self.nombreDeNuits.get(),
                    self.descriptionDeLaMaladie.get(),
                ),
            )

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Patient enregistré avec succès ✅")
            print("\nSUCCESSFUL COMMITMENT")

    # =========================================================== #
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="GiovannI2004@",
            database="nf06Hopital",
        )
        myCursor = conn.cursor()
        myCursor.execute("select * from nf06Hopital")

        self.delete_all_rows()

        rows = myCursor.fetchall()
        if len(rows) != 0:
            for i in rows:
                self.hospitalTable.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ============================================================ #
    def iSupprimer(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="GiovannI2004@",
            database="nf06Hopital",
        )
        myCursor = conn.cursor()
        query = "delete from nf06Hopital where numeroDImmatriculation=%s"
        value = (self.numeroDImmatriculation.get(),)
        myCursor.execute(query, value)

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete", "Patient Supprimé avec success ✅")

    # ============================================================= #
    def delete_all_rows(self):
        for item in self.hospitalTable.get_children():
            self.hospitalTable.delete(item)

    # ============================================================= #
    def get_cursor(self, event=""):
        cursor_row = self.hospitalTable.focus()
        content = self.hospitalTable.item(cursor_row)
        row = content["values"]

        print(row)

        self.numeroDImmatriculation.set(row[0])
        self.nom.set(row[1])
        self.prenom.set(row[2])
        self.age.set(row[3])
        self.sexe.set(row[4])
        self.adresse.set(row[5])
        self.service.set(row[6])
        self.numeroDeLaChambre.set(row[7])
        self.specialiteDuMedecin.set(row[8])
        self.coordoneeDuMedecin.set(row[9])
        self.date.set(row[10])
        self.heure.set(row[11])
        self.nombreDeNuits.set(row[12])
        self.descriptionDeLaMaladie.set(row[13])

        self.prescription()

    # ============================================================= #
    def iModifier(self):
        print("\nUPDATING PATIENT...\n")
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="GiovannI2004@",
            database="nf06Hopital",
        )
        myCursor = conn.cursor()
        myCursor.execute(
            "update nf06Hopital set nom=%s,prenom=%s,age=%s,sexe=%s,adresse=%s,service=%s,numeroDeLaChambre=%s,specialiteDuMedecin=%s,coordoneeDuMedecin=%s,date=%s,heure=%s,nombreDeNuits=%s,description=%s where numeroDImmatriculation=%s",
            (
                self.nom.get(),
                self.prenom.get(),
                self.age.get(),
                self.sexe.get(),
                self.adresse.get(),
                self.service.get(),
                self.numeroDeLaChambre.get(),
                self.specialiteDuMedecin.get(),
                self.coordoneeDuMedecin.get(),
                self.date.get(),
                self.heure.get(),
                self.nombreDeNuits.get(),
                self.descriptionDeLaMaladie.get(),
                self.numeroDImmatriculation.get(),
            ),
        )

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Patient modifié avec success ✅")

    # ==================================================================== #
    def prescription(self):
        self.textePrescription.delete("1.0", END)

        self.textePrescription.insert(
            END, "•N° Imma:\t\t" + self.numeroDImmatriculation.get() + "\n"
        )
        self.textePrescription.insert(
            END, "•Nom:\t\t" + self.nom.get() + "\n"
        )
        self.textePrescription.insert(
            END, "•Prenom:\t\t" + self.prenom.get() + "\n"
        )
        self.textePrescription.insert(
            END, "•Age:\t\t" + self.age.get() + "\n"
        )
        self.textePrescription.insert(
            END, "•Sexe:\t\t" + self.sexe.get() + "\n"
        )
        self.textePrescription.insert(
            END, "•Adresse:\t\t" + self.adresse.get() + "\n"
        )
        self.textePrescription.insert(
            END, "•Service:\t\t" + self.service.get() + "\n"
        )
        self.textePrescription.insert(
            END, "•N° Chambre:\t\t" + self.numeroDeLaChambre.get() + "\n"
        )
        self.textePrescription.insert(
            END, "•Spe Med:\t\t" + self.specialiteDuMedecin.get() + "\n"
        )
        self.textePrescription.insert(
            END, "•Coor Med:\t\t" + self.coordoneeDuMedecin.get() + "\n"
        )
        self.textePrescription.insert(
            END, "•Date:\t\t" + self.date.get() + "\n"
        )
        self.textePrescription.insert(
            END, "•Heure:\t\t" + self.heure.get() + "\n"
        )
        self.textePrescription.insert(
            END, "•Nbre nuits:\t\t" + self.nombreDeNuits.get() + "\n"
        )
        self.textePrescription.insert(
            END, "•Description:\t\t" + self.descriptionDeLaMaladie.get() + "\n"
        )

        self.textePrescription.insert(END, "\n")

    # ==================================================================== #
    def iQuitter(self):
        iExit = messagebox.askyesno(
            "Hopital Les Genies Management System", "Voulez-vous quitter l'application?"
        )
        if iExit > 0:
            root.destroy()
            return


# ================== Déclaration de notre TKinter====================#
root = Tk()
ob = Hopital(root)
root.mainloop()
