import bottle, model

SKRIVNOST = "Analiza je najboljši predmet"

vislice = model.Vislice()
vislice.nalozi_igre_iz_datoteke()

@bottle.get("/")

def indeks():
    return bottle.template("views/index.tpl")

@bottle.post("/nova_igra/")
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('id_igre', id_igre, path='/', secret=SKRIVNOST)
    return bottle.redirect(f"/igra/")

@bottle.get("/igra/")
def pokazi_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNOST)
    igra, stanje = vislice.igre[id_igre]
    geslo = igra.pravilni_del_gesla()
    nepravilni = igra.nepravilni_ugibi()
    obesenost = igra.stevilo_napak()
    return bottle.template("views/igra.tpl", {'stanje': stanje, 'model': model, 'geslo': geslo, 'nepravilni': nepravilni, 'obesenost': obesenost})

@bottle.post("/igra/")
def ugibaj():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNOST)
    crka = bottle.request.forms.crka
    vislice.ugibaj(id_igre, crka)
    return bottle.redirect(f"/igra/")

@bottle.get("/img/<picture>")
def slika(picture):
    return bottle.static_file(picture, root="img")

bottle.run(reloader=True, debug=True)