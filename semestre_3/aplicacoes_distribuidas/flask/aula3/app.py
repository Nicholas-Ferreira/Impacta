'''
 Nome: Nicholas Mota Ferreira
 RA: 1900953
'''

from flask import Flask, request, render_template

app = Flask('app')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
  login = request.form["login"]
  senha = request.form["senha"]
  if(login == '123' and senha == "123"):
    return render_template('dashboard.html', mensagem='Bem vindo, '+login)

  return render_template('dashboard.html', mensagem='Falha no login')

if __name__ == '__main__':
  app.run(host='localhost', port=5002, debug=True)