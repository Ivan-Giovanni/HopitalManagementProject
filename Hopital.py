from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


# ============================================= Définition de la classe Hopital ====================================================#

class Hopital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hopital Les Génies Management System")
        self.root.geometry("1540x800+0+0")

        self.nameOfTablets = StringVar()
        self.ref = StringVar()
        self.dose = StringVar()
        self.numberOfTablets = StringVar()
        self.lot = StringVar()
        self.issueDate = StringVar()
        self.expDate = StringVar()
        self.dailyDose = StringVar()
        self.storageAdvice = StringVar()
        self.nhsNumber = StringVar()
        self.patientName = StringVar()
        self.dateOfBirth = StringVar()
        self.patientAddress = StringVar()


root = Tk()
ob = Hopital(root)
root.mainloop()

print(2)
