from flask import Flask, request, render_template

app = Flask('app')

@app.route('/')
def index():
  return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
  req = request.form
  print(req['ra'])
  return render_template('login.html')

app.run(host='localhost', port='8081', debug=True)