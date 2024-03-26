from flask import Flask, render_template

app = Flask(__name__)

@app.route('/:param1')
def index():
    print()
    return render_template('index.html')
  
