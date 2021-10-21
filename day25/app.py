from flask import Flask, render_template


app = Flask(__name__)


@app.route("/") 
def index():
    active = 'False'
    return render_template('index.html', a=active)

@app.route("/product")
def product():
    active = 'True'
    book_info = {
        'name': 'Incognito (beyinin gizli həyatı)',
        'price': '12.00',
        'ex_price': '15.00',
        'bio': 'loremas jnfasjunbfv ewcnerewrsc eanrif asrvnaer cvaervcn aer oiawnerrf cawni onawiee fj wei wefin erwrfniwne nionkwe f olkwnee onilermf qwo4lkn f3e4rf omeif ewqrrf ejwrf nqnwererf erwfno.',
        'language': 'Azərbaycanca',
        'genre': 'Psixologiya',
        'writer': 'David Eagleman',
        'publisher': 'Qanun Nəşriyyatı',
        'number': 1,
        'image': "../static/images/Inkognito.png"
    }
    return render_template('product.html', a=active, book_info=book_info)