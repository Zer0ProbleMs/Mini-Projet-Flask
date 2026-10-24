from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)

typeSalle = [
    {'id': 1, 'nomTypeSalle': 'td', 'typeCours': 'TD'},
    {'id': 2, 'nomTypeSalle': 'amphi', 'typeCours': 'CM'},
    {'id': 3, 'nomTypeSalle': 'tp_machine', 'typeCours': 'TP'},
    {'id': 4, 'nomTypeSalle': 'tp_reseau', 'typeCours': 'TP'},
    {'id': 5, 'nomTypeSalle': 'salle_des_profs', 'typeCours': None}
]


salleCours = [
    {'id': 1, 'nomSalle': 'Salle 101', 'etage': 0, 'nbMaxEtudiants': 30, 'surface': 100, 'nbPrisesCourant': 25,
     'nbMachines': 35, 'batiment': 'E', 'typeSalle_id': 3, 'photo':'101.jpg'},
    {'id': 2, 'nomSalle': 'Salle 102', 'etage': 0, 'nbMaxEtudiants': 25, 'surface': 102, 'nbPrisesCourant': 25,
     'nbMachines': 35, 'batiment': 'E', 'typeSalle_id': 3, 'photo':'102.jpg'},
    {'id': 3, 'nomSalle': 'Salle 103', 'etage': 1, 'nbMaxEtudiants': 28, 'surface': 104, 'nbPrisesCourant': 25,
     'nbMachines': 35, 'batiment': 'E', 'typeSalle_id': 4, 'photo':'103.jpg'},
    {'id': 4, 'nomSalle': 'Salle 104', 'etage': 1, 'nbMaxEtudiants': 24, 'surface': 105, 'nbPrisesCourant': 25,
     'nbMachines': 35, 'batiment': 'E', 'typeSalle_id': 3, 'photo':'104.jpg'},
    {'id': 5, 'nomSalle': 'Salle 105', 'etage': 1, 'nbMaxEtudiants': 28, 'surface': 98, 'nbPrisesCourant': 25,
     'nbMachines': 35, 'batiment': 'E', 'typeSalle_id': 3, 'photo':'105.jpg'},
    {'id': 6, 'nomSalle': 'Salle 106', 'etage': 1, 'nbMaxEtudiants': 23, 'surface': 97, 'nbPrisesCourant': 25,
     'nbMachines': 35, 'batiment': 'E', 'typeSalle_id': 3, 'photo':'106.jpg'},
    {'id': 7, 'nomSalle': 'Salle 107', 'etage': 1, 'nbMaxEtudiants': 24, 'surface': 96, 'nbPrisesCourant': 25,
     'nbMachines': 35, 'batiment': 'E', 'typeSalle_id': 3, 'photo':'107.jpg'},
    {'id': 8, 'nomSalle': 'Salle 108', 'etage': 1, 'nbMaxEtudiants': 31, 'surface': 85, 'nbPrisesCourant': 25,
     'nbMachines': 35, 'batiment': 'E', 'typeSalle_id': 5, 'photo':'108.jpg'},
    {'id': 9, 'nomSalle': 'Salle 109', 'etage': 1, 'nbMaxEtudiants': 34, 'surface': 88, 'nbPrisesCourant': 25,
     'nbMachines': 35, 'batiment': 'E', 'typeSalle_id': 5, 'photo':'109.jpg'},
    {'id': 10, 'nomSalle': 'Salle 200', 'etage': 1, 'nbMaxEtudiants': 10, 'surface': 91, 'nbPrisesCourant': 15,
     'nbMachines': 25, 'batiment': 'E', 'typeSalle_id': 3, 'photo':'200.jpg'},
    {'id': 11, 'nomSalle': 'Salle 201', 'etage': 1, 'nbMaxEtudiants': 10, 'surface': 94, 'nbPrisesCourant': 15,
     'nbMachines': 25, 'batiment': 'E', 'typeSalle_id': 3, 'photo':'201.jpg'},
    {'id': 12, 'nomSalle': 'Salle 202', 'etage': 2, 'nbMaxEtudiants': 14, 'surface': 95, 'nbPrisesCourant': 15,
     'nbMachines': 25, 'batiment': 'E', 'typeSalle_id': 3, 'photo':'202.jpg'},
    {'id': 13, 'nomSalle': 'Salle 203', 'etage': 2, 'nbMaxEtudiants': 30, 'surface': 96, 'nbPrisesCourant': 25,
     'nbMachines': 35, 'batiment': 'E', 'typeSalle_id': 1, 'photo':'203.jpg'},
    {'id': 14, 'nomSalle': 'Salle 204', 'etage': 2, 'nbMaxEtudiants': 28, 'surface': 103, 'nbPrisesCourant': 10,
     'nbMachines': 15, 'batiment': 'E', 'typeSalle_id': 1, 'photo':'204.jpg'},
    {'id': 15, 'nomSalle': 'Salle 205', 'etage': 2, 'nbMaxEtudiants': 27, 'surface': 108, 'nbPrisesCourant': 10,
     'nbMachines': 15, 'batiment': 'E', 'typeSalle_id': 1, 'photo':'205.jpg'},
    {'id': 16, 'nomSalle': 'Salle 206', 'etage': 2, 'nbMaxEtudiants': 36, 'surface': 107, 'nbPrisesCourant': 10,
     'nbMachines': 15, 'batiment': 'E', 'typeSalle_id': 1, 'photo':'206.jpg'},
    {'id': 17, 'nomSalle': 'Salle 207', 'etage': 2, 'nbMaxEtudiants': 36, 'surface': 100, 'nbPrisesCourant': 10,
     'nbMachines': 15, 'batiment': 'E', 'typeSalle_id': 1, 'photo':'207.jpg'},
    {'id': 18, 'nomSalle': 'Salle 208', 'etage': 2, 'nbMaxEtudiants': 28, 'surface': 100, 'nbPrisesCourant': 10,
     'nbMachines': 15, 'batiment': 'E', 'typeSalle_id': 1, 'photo':'208.jpg'},
    {'id': 19, 'nomSalle': 'Salle 209', 'etage': 2, 'nbMaxEtudiants': 27, 'surface': 100, 'nbPrisesCourant': 10,
     'nbMachines': 15, 'batiment': 'E', 'typeSalle_id': 1, 'photo':'209.jpg'},
    {'id': 20, 'nomSalle': 'Amphi 1', 'etage': 0, 'nbMaxEtudiants': 100, 'surface': 500, 'nbPrisesCourant': 10,
     'nbMachines': 15, 'batiment': 'F', 'typeSalle_id': 2, 'photo':'amphi1.jpg'},
    {'id': 21, 'nomSalle': 'Amphi 3', 'etage': 0, 'nbMaxEtudiants': 100, 'surface': 500, 'nbPrisesCourant': 10,
     'nbMachines': 15, 'batiment': 'D', 'typeSalle_id': 2, 'photo':'amphi3.jpg'}
]


@app.route('/')

@app.route('/type-salle/show')
def show_type_salle():
    return render_template('type_salle/show_type_salle.html', etudiants=typeSalle)

if __name__ == '__main__':
    app.run()
