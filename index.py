from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/inici")
def inici():
    return render_template("inici.html")

@app.route("/llibres", methods=["POST", "GET"])
def llibres():
    if request.method == "POST":
        try:
            nom = request.form["nom"]
            cognom = request.form["cognom"]
            titol = request.form["titol"]
            editorial = request.form["editorial"]
            any_ = request.form["any"]
            lloc = request.form["lloc"]

            
            text = format_llibre(nom, cognom, titol, editorial, any_, lloc)
            return render_template("llibres.html", text=text)
        except:
            return render_template("llibres.html")
    else:
        return render_template("llibres.html")


@app.route("/revistes", methods=["POST", "GET"])
def revistes():
    if request.method == "POST":
        try:
            nom = request.form["nom"]
            cognom = request.form["cognom"]
            titol = request.form["titol"]
            data = request.form["data"]
            nom_revista = request.form["revista"]
            num = request.form["numero"]
            pags = request.form["pags"]

            
            text = format_revista(nom, cognom, titol, data, nom_revista, num, pags)
            return render_template("revistes.html", text=text)
        except:
            return render_template("revistes.html")
    else:
        return render_template("revistes.html")
    return render_template("revistes.html")

@app.route("/internet", methods=["POST", "GET"])
def internet():
    if request.method == "POST":
        try:
            nom = request.form["nom"]
            cognom = request.form["cognom"]
            titol = request.form["titol"]
            any_ = request.form["any"]
            email = request.form["email"]

            
            text = format_internet(nom, cognom, titol, any_, email)
            return render_template("enciclopedies.html", text=text)
        except:
            return render_template("enciclopedies.html")
    else:
        return render_template("internet.html")
    return render_template("internet.html")

@app.route("/enciclopedies", methods=["POST", "GET"])
def enciclopedies():
    if request.method == "POST":
        try:
            nom = request.form["nom"]
            cognom = request.form["cognom"]
            titol = request.form["titol"]
            editorial = request.form["editorial"]
            any_ = request.form["any"]
            lloc = request.form["lloc"]
            volum = request.form["volum"]

            
            text = format_enciclopedies(nom, cognom, titol, editorial, any_, lloc, volum)
            return render_template("enciclopedies.html", text=text)
        except:
            return render_template("enciclopedies.html")
    else:
        return render_template("enciclopedies.html")
    return render_template("enciclopedies.html")


def format_llibre(nom, cognom, titol, editorial, any_, lloc):
    return f"{cognom.upper()}, {nom[0].upper() + nom[1:].lower()} : {titol}, Ed. {editorial}, {lloc}, {any_}."


def format_enciclopedies(nom, cognom, titol, editorial, any_, lloc, volum):
    return f"{cognom.upper()}, {nom[0].upper() + nom[1:].lower()} : {titol}, Ed. {editorial}, {lloc}, {any_}, volum {volum}."

def format_internet(nom, cognom, titol, any_, email):
    return f"{cognom.upper()}, {nom[0].upper() + nom[1:].lower()}: {titol}. {email}. {any_}."

def format_revista(nom, cognom, titol, data, nom_revista, num, pags):
    return f'{cognom.upper()}, {nom[0].upper() + nom[1:].lower()} : "{titol}", {nom_revista}.  número {num}. {data}. {pags}.'


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")