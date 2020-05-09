from flask import Flask, request, render_template

app = Flask('app')

@app.route('/')
def index():
  return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
  return render_template('login.html')

app.run(host='0.0.0.0', port='8081', debug=True)