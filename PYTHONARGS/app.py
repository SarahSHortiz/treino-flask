from flask import Flask, jsonify, render_template


app = Flask('flaskweb', template_folder="./static")

@app.route('/<ano>')
def root(ano):
    return render_template('./teste.html', ano=ano)

# @app.route('/<batata>')

# def comida(batata):
#     return f'alô {batata}'

# @app.route('/cafe/<cafe>')

# def cafe(cafe):
#     return f'kkkkkkkkkk{cafe}'

# #apirest
# @app.route('/user/<nome>')
# def usuarios(nome):
#     x = {
#         'nome': nome,
#         'idade':12
#     }
#     return jsonify(x)

app.run()