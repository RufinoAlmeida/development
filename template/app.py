from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def formulario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']

        # Por enquanto só imprime no terminal
        print(f"Nome: {nome}, Email: {email}, Telefone: {telefone}")

        return f"<h3>Dados recebidos com sucesso!</h3>"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
