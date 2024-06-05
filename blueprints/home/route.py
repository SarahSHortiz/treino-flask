from flask import Blueprint, render_template, request

home = Blueprint('home', __name__)

@home.route('/')
def home_page():
    resultado = None
    media = None

    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')

    if primeira and segunda:
        primeira = float(primeira)
        segunda = float(segunda)

        media = (primeira + segunda) / 2

        if media >= 7:
            resultado = 'aprovadis'
        elif media >= 4:
            resultado = 'recuperação mano'
        else:
             resultado = 'ficou reprovado'
    
    return render_template('home.html', media = media, resultado=resultado)

