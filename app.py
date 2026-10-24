from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)
app.secret_key = 'une cle(token) : grain de sel(any random string)'
app.config["TEMPLATES_AUTO_RELOAD"] = True

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


@app.route('/', methods=['GET'])

@app.route('/accueil', methods=['GET'])
def accueil():
    return render_template('index.html')

# =====================
# La partie Type-Salle
# =====================
@app.route('/type-salle/show', methods=['GET'])
def show_type_salle():
    return render_template('type_salle/show_type_salle.html', typeSalle = typeSalle)

@app.route('/type-salle/add', methods=['GET'])
def add_type_salle():
    return render_template('type_salle/add_type_salle.html')

@app.route('/type-salle/add', methods=['POST'])
def valid_add_type_salle():
    return redirect('type_salle/valid_add_type_salle.html')

@app.route('/type-salle/delete', methods=['GET'])
def delete_type_salle():
    print(''' Suppression d'une Salle ''')
    id = request.args.get("id")
    message = f"Suppression du type de salle dont l\'Identifiant est : {str(id)}"
    print(message)
    flash(message, 'alert-danger')
    return redirect("/type-salle/show")

@app.route('/type-salle/edit', methods=['GET'])
def edit_type_salle():
    return render_template('type_salle/edit_type_salle.html')

@app.route('/type-salle/edit', methods=['POST'])
def valid_edit_type_salle():
    return redirect('type_salle/valid_edit_type_salle.html')

# =====================
# La partie Salle-Cours
# =====================
@app.route('/salle-cours/show', methods=['GET'])
def show_salle_cours():
    return render_template('salle_cours/show_salle_cours.html', salleCours = salleCours)

@app.route('/salle-cours/add', methods=['GET'])
def add_salle_cours():
    return render_template('salle_cours/add_salle_cours.html')

@app.route('/salle-cours/add', methods=['POST'])
def valid_add_salle_cours():
    return redirect('salle_cours/valid_add_salle_cours.html')

@app.route('/salle-cours/delete', methods=['GET'])
def delete_salle_cours():
    print(''' Suppression d'une Salle ''')
    id = request.args.get("id")
    message = f"Suppression de la salle dont l\'Identifiant est : {str(id)}"
    print(message)
    flash(message, 'alert-danger')
    return redirect("/salle-cours/show")

@app.route('/salle-cours/edit', methods=['GET'])
def edit_salle_cours():
    return render_template('salle_cours/edit_salle_cours.html')

@app.route('/salle-cours/edit', methods=['POST'])
def valid_edit_salle_cours():
    return redirect('salle_cours/valid_edit_salle_cours.html')

@app.route('/salle-cours/filtre', methods=['GET'])
def filtre_salle_cours():
    return render_template('salle_cours/front_salle_cours_filtre_show.html')


if __name__ == '__main__': # Permet de lancer l'application à travers l'instance de app que si celle-ci existe ('if' est nécessaire)
    app.run()
