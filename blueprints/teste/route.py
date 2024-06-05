from flask import Blueprint, render_template

teste = Blueprint('teste', __name__, template_folder='templates')

@teste.route('/teste')
def teste_page():
    return render_template('teste.html')