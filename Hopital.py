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
        self.age = IntVar()
        self.sexe = StringVar()
        self.descriptionDeLaMaladie = StringVar()
        self.numeroDeLaChambre = StringVar()
        self.specialiteDuMedecin = StringVar()
        self.coordoneeDuMedecin = StringVar()
        self.jour = IntVar()
        self.mois = IntVar()
        self.annee = IntVar()
        self.heure = IntVar()
        self.nombreDeNuits = IntVar()

        self.recherche = StringVar()

        self.accouchement = IntVar()
        self.bilanSante = IntVar()
        self.operationDuCanalCarpien = IntVar()
        self.orl = IntVar()
        self.echographie = IntVar()
        self.coloscopie = IntVar()
        self.irm = IntVar()
        self.chambreIndividuelle = IntVar()

        self.devis = StringVar()

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
                "jour",
                "mois",
                "annee",
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

        DataframeRightUp = LabelFrame(
            Dataframe,
            bd=10,
            relief=RIDGE,
            padx=10,
            font=("times new roman", 17, "bold"),
            text="Examens et Tarifs",
        )
        DataframeRightUp.place(x=990, y=5, width=400, height=231)

        DataframeRightDown = LabelFrame(
            Dataframe,
            bd=10,
            relief=RIDGE,
            padx=10,
            font=("times new roman", 17, "bold"),
            text="Devis",
        )
        DataframeRightDown.place(x=990, y=240, width=400, height=64)

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
        labelDescriptionDeLaMaladie.grid(row=7, column=0, sticky=W)
        textlDescriptionDeLaMaladie = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.descriptionDeLaMaladie, width=35
        )
        textlDescriptionDeLaMaladie.grid(row=7, column=1)

        # ===================================== #
        labelNumeroDeLaChambre = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="N° Chambre", padx=2
        )
        labelNumeroDeLaChambre.grid(row=0, column=2, sticky=W)
        texteNumeroDeLaChambre = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.numeroDeLaChambre, width=35
        )
        texteNumeroDeLaChambre.grid(row=0, column=3)

        # ===================================== #
        labelSpecialiteDuMedecin = Label(
            DataframeLeft,
            text="Specialite du Med.",
            font=("arial", 15, "bold"),
            padx=2,
            pady=6,
        )
        labelSpecialiteDuMedecin.grid(row=1, column=2, sticky=W)

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
        comboBoxSpecialiteDuMedecin.grid(row=1, column=3)

        # ===================================== #
        labelCoordonneDuMedecin = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Coordonnees du Med.", padx=2
        )
        labelCoordonneDuMedecin.grid(row=2, column=2, sticky=W)
        texteCoordonneDuMedecin = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.coordoneeDuMedecin, width=35
        )
        texteCoordonneDuMedecin.grid(row=2, column=3)

        # ===================================== #
        labelJour = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Jour", padx=2
        )
        labelJour.grid(row=5, column=2, sticky=W)
        texteJour = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.jour, width=35
        )
        texteJour.grid(row=5, column=3)

        # ===================================== #
        labelMois = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Mois", padx=2
        )
        labelMois.grid(row=6, column=2, sticky=W)
        texteMois = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.mois, width=35
        )
        texteMois.grid(row=6, column=3)

        # ===================================== #
        labelAnnee = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Annee", padx=2
        )
        labelAnnee.grid(row=7, column=2, sticky=W)
        texteAnnee = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.annee, width=35
        )
        texteAnnee.grid(row=7, column=3)

        # ===================================== #
        labelHeure = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Heure", padx=2
        )
        labelHeure.grid(row=4, column=2, sticky=W)
        texteHeure = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.heure, width=35
        )
        texteHeure.grid(row=4, column=3)

        # ===================================== #
        labelNombreDeNuits = Label(
            DataframeLeft, font=("arial", 15, "bold"), text="Nombre de nuits", padx=2
        )
        labelNombreDeNuits.grid(row=3, column=2, sticky=W)
        texteNombreDeNuits = Entry(
            DataframeLeft, font=("arial", 14, "bold"), textvariable=self.nombreDeNuits, width=35
        )
        texteNombreDeNuits.grid(row=3, column=3)

        # ======================================= DataframeRight ================================================= #
        # ======================================= DataframeRightUp =============================================== #
        # ======================================= #
        Checkbutton(DataframeRightUp, text="Accouchement", font=("arial", 15, "bold"),
                    variable=self.accouchement).grid(
            row=0, column=0, sticky=W)
        labelAccouchement = Label(
            DataframeRightUp, font=("arial", 15, "bold"), text="2600€", padx=40
        )
        labelAccouchement.grid(row=0, column=1, sticky=W)

        # ======================================= #
        Checkbutton(DataframeRightUp, text="Bilan de Sante", font=("arial", 15, "bold"),
                    variable=self.bilanSante).grid(
            row=1, column=0, sticky=W)
        labelBilanSante = Label(
            DataframeRightUp, font=("arial", 15, "bold"), text="50€", padx=40
        )
        labelBilanSante.grid(row=1, column=1, sticky=W)

        # ======================================= #
        Checkbutton(DataframeRightUp, text="Operation du canal carpien", font=("arial", 15, "bold"),
                    variable=self.operationDuCanalCarpien).grid(
            row=2, column=0, sticky=W)
        labelOperationDuCanalCarpien = Label(
            DataframeRightUp, font=("arial", 15, "bold"), text="1250€", padx=40
        )
        labelOperationDuCanalCarpien.grid(row=2, column=1, sticky=W)

        # ======================================= #
        Checkbutton(DataframeRightUp, text="ORL", font=("arial", 15, "bold"), variable=self.orl).grid(
            row=3, column=0, sticky=W)
        labelOrl = Label(
            DataframeRightUp, font=("arial", 15, "bold"), text="35€", padx=40
        )
        labelOrl.grid(row=3, column=1, sticky=W)

        # ======================================= #
        Checkbutton(DataframeRightUp, text="Echographie ", font=("arial", 15, "bold"),
                    variable=self.echographie).grid(
            row=4, column=0, sticky=W)
        labelEchographie = Label(
            DataframeRightUp, font=("arial", 15, "bold"), text="85€", padx=40
        )
        labelEchographie.grid(row=4, column=1, sticky=W)

        # ======================================= #
        Checkbutton(DataframeRightUp, text="Coloscopie", font=("arial", 15, "bold"),
                    variable=self.coloscopie).grid(
            row=5, column=0, sticky=W)
        labelColoscopie = Label(
            DataframeRightUp, font=("arial", 15, "bold"), text="190€", padx=40
        )
        labelColoscopie.grid(row=5, column=1, sticky=W)

        # ======================================= #
        Checkbutton(DataframeRightUp, text="IRM ", font=("arial", 15, "bold"), variable=self.irm).grid(
            row=6, column=0, sticky=W)
        labelIrm = Label(
            DataframeRightUp, font=("arial", 15, "bold"), text="400€", padx=40
        )
        labelIrm.grid(row=6, column=1, sticky=W)

        # ======================================= #
        Checkbutton(DataframeRightUp, text="Chambre individuelle", font=("arial", 15, "bold"),
                    variable=self.chambreIndividuelle).grid(
            row=7, column=0, sticky=W)
        labelChambreIndividuelle = Label(
            DataframeRightUp, font=("arial", 15, "bold"), text="68€/jour", padx=40
        )
        labelChambreIndividuelle.grid(row=7, column=1, sticky=W)

        # ======================================= DataframeRightDown =============================================== #
        # ======================================= #
        labelTotal = Label(
            DataframeRightDown, font=("arial", 18, "bold"), text="TOTAL(€): ", padx=1
        )
        labelTotal.grid(row=0, column=0)
        texteTotal = Entry(
            DataframeRightDown, font=("arial", 18, "bold"), textvariable=self.devis, width=23, state="readonly")
        texteTotal.grid(row=0, column=1)

        # ======================================= Search Bar ========================================================== #
        labelSearchBar = Label(SearchBarframe, font=("arial", 16, "bold"), text="SearchBar", padx=2)
        labelSearchBar.grid(row=0, column=0, sticky=W)
        searchBarEntry = Entry(SearchBarframe, font=("arial", 17, "bold"), textvariable=self.recherche, width=130)
        searchBarEntry.grid(row=0, column=1)

        # ======================================= Boutons =========================================================== #
        # ===================================== #
        boutonToutAfficher = Button(
            Buttonframe,
            command=self.ifetch_data,
            text="ToutAfficher",
            bg="#00FF00",
            fg="blue",
            font=("arial", 12, "bold"),
            width=18,
            height=2,
        )
        boutonToutAfficher.grid(row=0, column=0)

        # ===================================== #
        boutonEnregistrer = Button(
            Buttonframe,
            command=self.iEnregistrer,
            text="Enregistrer",
            bg="#00FF00",
            fg="blue",
            font=("arial", 12, "bold"),
            width=16,
            height=2,
        )
        boutonEnregistrer.grid(row=0, column=1)

        # ===================================== #
        optionsRechercher = [
            "Rechercher par",
            "Nom",
            "Penom",
            "N° Imma.",
            "Annee"
        ]

        clickedRecherche = StringVar()
        clickedRecherche.set(optionsRechercher[0])

        boutonRechercher = Frame(Buttonframe, bd=5)
        boutonRechercher.grid(row=0, column=2)

        dropRechercher = OptionMenu(boutonRechercher, clickedRecherche, *optionsRechercher, command=self.iRechercher)
        dropRechercher.config(height=1, width=16, fg="blue", font=("arial", 12, "bold"))
        dropRechercher.pack()

        # ===================================== #
        boutonModifier = Button(
            Buttonframe,
            command=self.iModifier,
            text="Modifier",
            bg="#00FF00",
            fg="blue",
            font=("arial", 12, "bold"),
            width=16,
            height=2,
        )
        boutonModifier.grid(row=0, column=3)

        # ===================================== #
        optionsTrier = [
            "Trier par",
            "Alphabetique",
            "Urgence",
            "Mois",
            "Annee"
        ]

        clickedTrier = StringVar()
        clickedTrier.set(optionsTrier[0])

        boutonTrier = Frame(Buttonframe, bd=5)
        boutonTrier.grid(row=0, column=4)

        dropTrier = OptionMenu(boutonTrier, clickedTrier, *optionsTrier, command=self.iTrier)
        dropTrier.config(height=1, width=16, fg="blue", font=("arial", 12, "bold"))
        dropTrier.pack()

        # ===================================== #
        boutonSupprimer = Button(
            Buttonframe,
            command=self.iSupprimer,
            text="Supprimer",
            bg="#00FF00",
            fg="blue",
            font=("arial", 12, "bold"),
            width=16,
            height=2,
        )
        boutonSupprimer.grid(row=0, column=5)

        # ===================================== #
        optionsStatistiques = [
            "Afficher Stats",
            "Stat 1",
            "Stat 2",
            "Stat 3",
            "Stat 4"
        ]

        clickedStatistiques = StringVar()
        clickedStatistiques.set(optionsStatistiques[0])

        boutonStatistiques = Frame(Buttonframe, bd=5)
        boutonStatistiques.grid(row=0, column=6)

        dropStatistiques = OptionMenu(boutonStatistiques, clickedStatistiques, *optionsStatistiques)
        dropStatistiques.config(height=1, width=16, fg="blue", font=("arial", 12, "bold"))
        dropStatistiques.pack()

        # ===================================== #
        boutonCalculerDevis = Button(
            Buttonframe,
            text="Devis",
            command=self.iDevis,
            bg="#00FF00",
            fg="blue",
            font=("arial", 12, "bold"),
            width=16,
            height=2,
        )
        boutonCalculerDevis.grid(row=0, column=7)

        # ===================================== #
        boutonQuitter = Button(
            Buttonframe,
            command=self.iQuitter,
            text="Quitter",
            bg="#00FF00",
            fg="blue",
            font=("arial", 12, "bold"),
            width=17,
            height=2,
        )
        boutonQuitter.grid(row=0, column=8)

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
                "jour",
                "mois",
                "annee",
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
        self.hospitalTable.heading("jour", text="Jour")
        self.hospitalTable.heading("mois", text="Mois")
        self.hospitalTable.heading("annee", text="Annee")
        self.hospitalTable.heading("heure", text="Heure")
        self.hospitalTable.heading("nombreDeNuits", text="Nbre nuits")
        self.hospitalTable.heading("description", text="Description")

        self.hospitalTable["show"] = "headings"

        self.hospitalTable.pack(fill=BOTH, expand=1)

        self.hospitalTable.column("numeroDImmatriculation", width=90)
        self.hospitalTable.column("nom", width=90)
        self.hospitalTable.column("prenom", width=90)
        self.hospitalTable.column("age", width=90)
        self.hospitalTable.column("sexe", width=90)
        self.hospitalTable.column("adresse", width=90)
        self.hospitalTable.column("service", width=90)
        self.hospitalTable.column("numeroDeChambre", width=90)
        self.hospitalTable.column("specialiteDuMedecin", width=90)
        self.hospitalTable.column("coordonnesDuMedecin", width=90)
        self.hospitalTable.column("jour", width=80)
        self.hospitalTable.column("mois", width=80)
        self.hospitalTable.column("annee", width=80)
        self.hospitalTable.column("heure", width=80)
        self.hospitalTable.column("nombreDeNuits", width=70)
        self.hospitalTable.column("description", width=90)

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
                "insert into nf06HopitalV3 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
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
                    self.jour.get(),
                    self.mois.get(),
                    self.annee.get(),
                    self.heure.get(),
                    self.nombreDeNuits.get(),
                    self.descriptionDeLaMaladie.get(),
                    self.accouchement.get(),
                    self.bilanSante.get(),
                    self.operationDuCanalCarpien.get(),
                    self.orl.get(),
                    self.echographie.get(),
                    self.coloscopie.get(),
                    self.irm.get(),
                    self.chambreIndividuelle.get(),
                    self.devis.get(),
                ),
            )

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Patient enregistré avec succès ✅")
            print("\nSUCCESSFUL COMMITMENT")

    # =========================================================== #
    def ifetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="GiovannI2004@",
            database="nf06Hopital",
        )
        myCursor = conn.cursor()
        myCursor.execute("select * from nf06HopitalV3")

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
        query = "delete from nf06HopitalV3 where numeroDImmatriculation=%s"
        value = (self.numeroDImmatriculation.get(),)
        myCursor.execute(query, value)

        conn.commit()
        self.ifetch_data()
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
        self.age.set(int(row[3]))
        self.sexe.set(row[4])
        self.adresse.set(row[5])
        self.service.set(row[6])
        self.numeroDeLaChambre.set(row[7])
        self.specialiteDuMedecin.set(row[8])
        self.coordoneeDuMedecin.set(row[9])
        self.jour.set(int(row[10]))
        self.mois.set(int(row[11]))
        self.annee.set(int(row[12]))
        self.heure.set(int(row[13]))
        self.nombreDeNuits.set(int(row[14]))
        self.descriptionDeLaMaladie.set(row[15])
        self.accouchement.set(int(row[16]))
        self.bilanSante.set(int(row[17]))
        self.operationDuCanalCarpien.set(int(row[18]))
        self.orl.set(int(row[19]))
        self.echographie.set(int(row[20]))
        self.coloscopie.set(int(row[21]))
        self.irm.set(int(row[22]))
        self.chambreIndividuelle.set(int(row[23]))
        self.devis.set(row[24])

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
            "update nf06HopitalV3 set nom=%s,prenom=%s,age=%s,sexe=%s,adresse=%s,service=%s,numeroDeLaChambre=%s,"
            "specialiteDuMedecin=%s,coordoneeDuMedecin=%s,jour=%s,mois=%s,annee=%s,heure=%s,"
            "nombreDeNuits=%s,description=%s,accouchement=%s,bilanSante=%s,operationDuCanalCarpien=%s,"
            "orl=%s,echographie=%s,coloscopie=%s,irm=%s,chambreIndividuelle=%s,devis=%s where numeroDImmatriculation=%s",
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
                self.jour.get(),
                self.mois.get(),
                self.annee.get(),
                self.heure.get(),
                self.nombreDeNuits.get(),
                self.descriptionDeLaMaladie.get(),
                self.accouchement.get(),
                self.bilanSante.get(),
                self.operationDuCanalCarpien.get(),
                self.orl.get(),
                self.echographie.get(),
                self.coloscopie.get(),
                self.irm.get(),
                self.chambreIndividuelle.get(),
                self.devis.get(),
                self.numeroDImmatriculation.get(),
            ),
        )

        conn.commit()
        self.ifetch_data()
        conn.close()
        messagebox.showinfo("Success", "Patient modifié avec success ✅")

    # ==================================================================== #
    def iQuitter(self):
        iExit = messagebox.askyesno(
            "Hopital Les Genies Management System", "Voulez-vous quitter l'application?"
        )
        if iExit > 0:
            root.destroy()
            return

    # ==================================================================== #
    def iRechercher(self, option):
        self.delete_all_rows()

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="GiovannI2004@",
            database="nf06Hopital",
        )
        myCursor = conn.cursor()

        if option == "Nom":
            myCursor.execute("select * from nf06HopitalV3 where nom = %s", (self.recherche.get(),))
        elif option == "Penom":
            myCursor.execute("select * from nf06HopitalV3 where prenom = %s", (self.recherche.get(),))
        elif option == "N° Imma.":
            myCursor.execute("select * from nf06HopitalV3 where numeroDImmatriculation = %s", (self.recherche.get(),))
        elif option == "Annee":
            myCursor.execute("select * from nf06HopitalV3 where annee = %s", (self.recherche.get(),))

        rows = myCursor.fetchall()
        if len(rows) != 0:
            for i in rows:
                self.hospitalTable.insert("", END, values=i)
            conn.commit()
        else:
            messagebox.showerror("Error", "Aucun patient correspondant")
        conn.close()

    # ==================================================================== #
    def iTrier(self, option):
        self.delete_all_rows()

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="GiovannI2004@",
            database="nf06Hopital",
        )
        myCursor = conn.cursor()
        myCursor.execute("select * from nf06HopitalV3")

        rows = myCursor.fetchall()

        if option == "Alphabetique":
            sortedRows = sorted(rows, key=lambda item: item[1])
            if len(sortedRows) != 0:
                for i in sortedRows:
                    self.hospitalTable.insert("", END, values=i)
                conn.commit()
            conn.close()
            print(sortedRows)
            print("\n")

        if option == "Urgence":
            sortedRows = sorted(rows, key=lambda item: item[8], reverse=True)
            if len(sortedRows) != 0:
                for i in sortedRows:
                    self.hospitalTable.insert("", END, values=i)
                conn.commit()
            conn.close()
            print(sortedRows)
            print("\n")

        if option == "Annee":
            sortedRows = sorted(rows, key=lambda item: item[12], reverse=True)
            if len(sortedRows) != 0:
                for i in sortedRows:
                    self.hospitalTable.insert("", END, values=i)
                conn.commit()
            conn.close()
            print(sortedRows)
            print("\n")

        if option == "Mois":
            sortedRows = sorted(rows, key=lambda item: item[11], reverse=True)
            if len(sortedRows) != 0:
                for i in sortedRows:
                    self.hospitalTable.insert("", END, values=i)
                conn.commit()
            conn.close()
            print(sortedRows)
            print("\n")

    # ==================================================================== #
    def iDevis(self):
        self.devis.set(
            str((2600 * self.accouchement.get()) + (50 * self.bilanSante.get()) + \
                (1250 * self.operationDuCanalCarpien.get()) + (35 * self.orl.get()) + \
                (85 * self.echographie.get()) + (190 * self.coloscopie.get()) + \
                (400 * self.irm.get()) + (68 * self.chambreIndividuelle.get() * self.nombreDeNuits.get()))
        )

        self.iModifier()

        print("Devis = ", self.devis.get(), "\n")

    # ==================================================================== #


# ================== Déclaration de notre TKinter====================#
root = Tk()
ob = Hopital(root)
root.mainloop()
