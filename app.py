from flask import Flask ,render_template
import os
import random
app = Flask(__name__)

var=["aasdas","bqweqwe","ddfgdfgd"]

@app.route('/')
def Home():
    single = random.choice(var)
    
    return single

if __name__ == "__main__":
    app.run(host="0.0.0.0",port =int(os.environ.get("PORT",4000)))