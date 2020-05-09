from flask import Flask, request, render_template

from apps.grupos.api import bp as bp_grupos

app = Flask('app')

@app.route('/')
def index():
  return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
  ra = request.form['ra']
  return render_template('login.html')
  
app.register_blueprint(bp_grupos, url_prefix='/grupos')

app.run(host='0.0.0.0', port='8081', debug=True)