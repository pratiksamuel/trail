from flask import Flask ,render_template
import os
import random
app = Flask(__name__)

var=["aasdas","bqweqwe","ddfgdfgd"]
a=2.18

@app.route('/')
def Home():
    single = random.choice(var)
    print("yo")
    return single

@app.route('/new_page/<name>')
def new_page(name):
    new = random.choice(var)
    return new+"_new_page_"+name+str(a)

@app.route('/yo')
def yo():
    new = random.choice(var)
    return new+"_yo_"+str(a)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port =int(os.environ.get("PORT",4000)))