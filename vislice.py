import bottle, model

vislice = model.Vislice()

@bottle.get("/")

def indeks():
    return bottle.template("views/index.tpl")

@bottle.post("/igra/")
def nova_igra():
    i = vislice.nova_igra()
    return bottle.redirect(f"/igra/{i}/")

@bottle.get("/igra/<id_igre:int>/")
def pokazi_igro(id_igre):
    igra, stanje = vislice.igre[id_igre]
    geslo = igra.pravilni_del_gesla()
    nepravilni = igra.nepravilni_ugibi()
    obesenost = igra.stevilo_napak()
    return bottle.template("views/igra.tpl", {'stanje': stanje, 'model': model, 'geslo': geslo, 'nepravilni': nepravilni, 'obesenost': obesenost})

@bottle.post("/igra/<id_igre:int>/")
def ugibaj(id_igre):
    crka = bottle.request.forms.crka
    vislice.ugibaj(id_igre, crka)
    return bottle.redirect(f"/igra/{id_igre}/")

bottle.run(reloader=True, debug=True)