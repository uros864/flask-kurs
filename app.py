from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/om")
def om():
    return render_template(
        "om.html",
        navn="Uros",
        alder=17,
        sprak="Serbisk",
        skole="Kuben VGS",
        poeng=30
        )
@app.route("/spill")
def spill():
    spillliste = ["Minecraft", "Rocket League", "Witcher 3", "Cyberpunk", "Apex Legends"  ]
    return render_template("spill.html", spill=spillliste)

@app.route("/registrering", methods=["GET","POST"])
def registrering():

    if request.method == "POST":
        navn = request.form["navn"]
        email = request.form["email"]
        alder = request.form["alder"]
        komentar = request.form["komentar"]
        return render_template(
            "resultat.html",
            navn=navn,
            email=email,
            alder=alder,
            komentar=komentar
        )

    return render_template("registrering.html")


if __name__ == "__main__":
    app.run(debug=True)