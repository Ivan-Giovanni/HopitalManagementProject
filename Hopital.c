#include <stdio.h>
#include <stdlib.h>


typedef struct Patient Patient;

struct Patient {
    char service[20];
    char NumeroImmatriculation[20];
    char nom[20];
    char prenom[20];
    char adresse[20];
    int age;
    char sexe;
    char descriptionDeLaMaladie[256];
    char numeroDeChambre[10];
    char coordonnesDuMedecin[20];
    char specialiteDuMedecin[20];
    char date[10];
    char heure[10];
    int nombreDeNuits;
};

int main() {
    printf("\n");



    printf("\n");
    return 0;
}