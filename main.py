from flask import Flask
from flask import request, jsonify, json, render_template, redirect, url_for, flash
import html
from csembarang import Csembarang

app = Flask(__name__)

sc = []
wsc = []
cs = Csembarang()

def checkrando(r, s):
    if r in s:
        return r+1
    return r

@app.route('/', defaults={"seed":None})
@app.route('/<seed>')
def home(seed):
    rando = cs.randin(cs.lendata, int(seed) if seed != None else 0)
    rando = checkrando(rando, sc)
    sc.append(rando)
    return render_template("form.html", btnran=rando, seed=int(seed) if seed != None else 0)

@app.route('/whitelist', defaults={"seed":None})
@app.route('/whitelist/<seed>')
def whitelist(seed):
    rando = cs.randin(cs.wlendata, int(seed) if seed != None else 0)
    rando = checkrando(rando, wsc)
    wsc.append(rando)
    return render_template("whitelist.html", btnran=rando, seed=int(seed) if seed != None else 0)
    
@app.route('/random/<seed>', methods=['GET'])
def random(seed):
    ch = cs.cparser(cs.data[int(seed)])
    return ch

@app.route('/wrandom/<seed>', methods=['GET'])
def wrandom(seed):
    ch = cs.cparser(cs.wdata[int(seed)])
    return ch

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=56733)