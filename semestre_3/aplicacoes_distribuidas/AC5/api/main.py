from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def index():
  return 'ok'

app.run(host='0.0.0.0', port='8081', debug=True)