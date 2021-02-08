from flask import Flask

app = Flask(__name__)

@app.route('/<n1>/<op>/<n2>', methods=["GET"])
def calc(n1, op, n2):
  try:
    n1 = float(n1)
    n2 = float(n2)
  except:
    return "", 404
  
  if(op == "mais"): return str(n1+n2)
  if(op == "manos"): return str(n1-n2)
  if(op == "mult"): return str(n1*n2)
  if(n2 == 0): return "", 422
  if(op == "div"): return str(n1/n2)
  if(op == "mod"): return str(n1%n2)
  else: return "", 404

if __name__ == "__main__":
  app.run(port=5000, debug=True)