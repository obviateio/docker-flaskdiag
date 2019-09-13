#from __future__ import print_function
import json
from flask import Flask, request, redirect, make_response
app = Flask(__name__)
app.debug = True

#@app.route("/")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    s = "<html><pre>"
    f = "</pre></html>"
    sep = '\n============================\n'
    #return(request.data + request.args + 
    p = "Path: " + path + "\n" 
    arg = str(json.dumps(request.args, sort_keys=True, indent=4, separators=(',', ': ')))
    dat = str(request.data)
    final = s + p + sep + str(request.headers) + sep + arg + sep + dat + f
    if path == "auth":
        print(final)
        resp = make_response("")
        resp.headers['x-polyauth-username'] = 'jdavis@smule.com'
        return(resp,200)
        #return("",401)
        #return(redirect("https://www.google.com"))
    else:
        return(final)

if __name__ == '__main__':
    app.run(port=3001,host='0.0.0.0')
