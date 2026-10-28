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
def show_layout():
    return render_template('layout.html', salleCours = salleCours, typeSalle = typeSalle)

# =====================
# La partie Type-Salle
# =====================
@app.route('/type-salle/show', methods=['GET'])
def show_type_salle():
    return render_template('type_salle/show_type_salle.html', typeSalle = typeSalle)

@app.route('/type-salle/add', methods=['GET'])
def add_type_salle():
    return render_template('type_salle/add_type_salle.html', typeSalle = typeSalle)

@app.route('/type-salle/add', methods=['POST'])
def valid_add_type_salle():
    id = request.form.get('id')
    nomTypeSalle = request.form.get('nomTypeSalle')
    typeCours = request.form.get('typeCours')
    message = (f"Vous venez d'ajouter un nouveau type de salle ! | "
               f"L'identifiant de la salle ajouté est : {id} | "
               f"Le nom du type choisi est : {nomTypeSalle} | "
               f"Le cours choisi est : {typeCours} | ")
    flash(message, 'alert-success')
    return redirect('/type-salle/show')

@app.route('/type-salle/delete', methods=['GET'])
def delete_type_salle():
    id = request.args.get("id")
    message = f"Suppression du type de salle dont l\'Identifiant est : {str(id)}"
    print(message)
    flash(message, 'alert-danger')
    return redirect("/type-salle/show")

@app.route('/type-salle/edit', methods=['GET'])
def edit_type_salle():
    id = request.args.get("id")
    if id.isnumeric():
        indice = int(id)
        salle = typeSalle[indice - 1]
    else:
        salle = []
    return render_template('type_salle/edit_type_salle.html', typeSalle = salle)

@app.route('/type-salle/edit', methods=['POST'])
def valid_edit_type_salle():
    id = request.form.get("id")
    nomTypeSalle = request.form.get("nomTypeSalle")
    typeCours = request.form.get("typeCours")
    message = (f"Vous venez de modifier les informations d'une salle ! | "
               f"L'identifiant de la salle choisi était : {id} | "
               f"Le nouveau nom choisi est : {nomTypeSalle} | "
               f"Le nouvel identifiant du type choisi est : {typeCours} | ")
    flash(message, 'alert-warning')
    return redirect('/type-salle/show')

# =====================
# La partie Salle-Cours
# =====================
@app.route('/salle-cours/show', methods=['GET'])
def show_salle_cours():
    return render_template('salle_cours/show_salle_cours.html', salleCours = salleCours)

@app.route('/salle-cours/add', methods=['GET'])
def add_salle_cours():
    return render_template('salle_cours/add_salle_cours.html', salleCours = salleCours, typeSalle = typeSalle)

@app.route('/salle-cours/add', methods=['POST'])
def valid_add_salle_cours():
    id = request.form.get("id")
    nomSalle = request.form.get("nomSalle")
    typeSalle_id = request.form.get("typeSalle_id")
    etage = request.form.get("etage")
    batiment = request.form.get("batiment")
    nbMaxEtudiants = request.form.get("nbMaxEtudiants")
    surface = request.form.get("surface")
    nbPrisesCourant = request.form.get("nbPrisesCourant")
    nbMachines = request.form.get("nbMachines")
    photo = request.form.get("photo")
    message = (f"Vous venez de créer une nouvelle salle ! | "
               f"L'identifiant de la nouvelle salle est : {id} | "
               f"Le nouveau nom choisi est : {nomSalle} | "
               f"Le nouvel identifiant du type choisi est : {typeSalle_id} | "
               f"L'étage de la nouvelle salle est : {etage} | "
               f"La nouvelle salle se situe dans le bâtiment : {batiment} | "
               f"Le nombre d'étudiants maximum pouvant être dans la salle est : {nbMaxEtudiants} | "
               f"La surface de la nouvelle salle est : {surface} | "
               f"Le nombre de prises dans la nouvelle salle est : {nbPrisesCourant} | "
               f"Le nombre de machiines dans la nouvelle salle est : {nbMachines} | "
               f"Le nom du fichier photo choisi est : {photo}")
    flash(message, 'alert-success')
    return redirect('/salle-cours/show')

@app.route('/salle-cours/delete', methods=['GET'])
def delete_salle_cours():
    id = request.args.get("id")
    message = f"Suppression de la salle dont l\'Identifiant est : {str(id)}"
    print(message)
    flash(message, 'alert-danger')
    return redirect("/salle-cours/show")

@app.route('/salle-cours/edit', methods=['GET'])
def edit_salle_cours():
    id = request.args.get("id")
    if id.isnumeric():
        indice = int(id)
        salle = salleCours[indice - 1]
    else:
        salle = []
    return render_template('salle_cours/edit_salle_cours.html', salleCours = salle, typeSalle = typeSalle)

@app.route('/salle-cours/edit', methods=['POST'])
def valid_edit_salle_cours():
    id = request.form.get("id")
    nomSalle = request.form.get("nomSalle")
    typeSalle_id = request.form.get("typeSalle_id")
    etage = request.form.get("etage")
    batiment = request.form.get("batiment")
    nbMaxEtudiants = request.form.get("nbMaxEtudiants")
    surface = request.form.get("surface")
    nbPrisesCourant = request.form.get("nbPrisesCourant")
    nbMachines = request.form.get("nbMachines")
    photo = request.form.get("photo")
    message = (f"Vous venez de modifier les informations d'une salle ! | "
               f"L'identifiant de la salle choisi était : {id} | "
               f"Le nouveau nom choisi est : {nomSalle} | "
               f"Le nouvel identifiant du type choisi est : {typeSalle_id} | "
               f"Le nouvel étage de la salle est : {etage} | "
               f"Le batiment de la salle est maintenant le batiment : {batiment} | "
               f"Le nombre d'étudiants maximum pouvant être dans la salle est : {nbMaxEtudiants} | "
               f"La surface de la salle est : {surface} | "
               f"Le nombre de prises dans la salle est : {nbPrisesCourant} | "
               f"Le nombre de machiines dans la salle est : {nbMachines} | "
               f"Le nom du fichier photo choisi est : {photo}")
    flash(message, 'alert-warning')
    return redirect('/salle-cours/show')

@app.route('/salle-cours/filtre', methods=['GET'])
def filtre_salle_cours():
    return render_template('salle_cours/front_salle_cours_filtre_show.html', salleCours=salleCours, typeSalle=typeSalle)

@app.route('/salle-cours/filtre', methods=['POST'])
def valid_filtre_salle_cours():
    nomSalle = request.form.get('nomSalle', None)
    surfaceMin = request.form.get('surfaceMin', None)
    surfaceMax = request.form.get('surfaceMax', None)
    typeSalle_id = request.form.getlist('typeSalle_id')

    # Les 'if' sont nécessaires pour filtrer les différentes recherches et ne pas rentrer des mauvaise valeurs impossibles dans la vrai réalistiquement parlant.
    # Un mail a également été envoyé par rapport à cela.
    if nomSalle and nomSalle != '':
        flash('Filtre sur le nom de la salle : ' + nomSalle, 'alert-success')

    if surfaceMin or surfaceMax:
        mini = str(surfaceMin).replace(',', '.')
        maxi = str(surfaceMax).replace(',', '.')
        if mini.replace('.', '', 1).isdigit() and maxi.replace('.', '', 1).isdigit():
            if float(mini) < float(maxi):
                flash('Filtre sur la surface entre ' + mini + ' et ' + maxi, 'alert-success')
            else:
                flash('La surface min doit être inférieure à la surface max', 'alert-warning')
        else:
            flash('Surface min et max doivent être des numériques positifs', 'alert-warning')

    if typeSalle_id:
        flash('Types de salle cochés (id) : ' + ', '.join(typeSalle_id), 'alert-success')

    return redirect('/salle-cours/filtre')

if __name__ == '__main__': # Permet de lancer l'application à travers l'instance de app que si celle-ci existe ('if' est nécessaire)
    app.run()
