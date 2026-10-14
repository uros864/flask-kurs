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



@app.route("/bestilling", methods=["GET","POST"])
def bestilling():

    produkter = ["Margherita","Peproni","BBQ", "Hawaii"]
    storrelser = ["Liten", "Medium", "Stor"]
    if request.method == "POST":
        navn = request.form["navn"]
        produkt = request.form["produkt"]
        storrelse = request.form["storrelse"]
        antall = request.form["antall"]
        kommentar = request.form.get("kommentar","")
        return render_template(
            "bekreftelse.html",
            navn=navn,
            produkt=produkt,
            storrelse=storrelse,
            antall=antall,
            kommentar=kommentar
        )

    return render_template(
        "bestilling.html",
        produkter=produkter,
        storrelser=storrelser)


@app.route("/kalkulator", methods=["GET","POST"])
def kalkulator():

    regnearter = ["+","-","*", "/"]
    if request.method == "POST":
        tall_1=request.form["tall1"]
        tall_2=request.form["tall2"]
        regneart=request.form["regneart"]
        return render_template(
            "kalkulator.html",
            tall_1=tall_1,
            tall_2=tall_2,
            regneart=regneart

        )

    return render_template(
        "kalkulator_skjema.html",
        regnearter=regnearter)


if __name__ == "__main__":
    app.run(debug=True)