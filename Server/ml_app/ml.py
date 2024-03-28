import pandas as pd
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from . import model as md
bp = Blueprint('ml', __name__, url_prefix='/')

@bp.route('', methods=('GET', 'POST'))
def predict():
    # print(request.form.get('cut'))
    result = -1
    if request.method == 'POST':
        info = {
            'carat': [request.form.get('carat')],
            'cut': [request.form.get('cut')],
            'color': [request.form.get('color')],
            'clarity': [request.form.get('clarity')],
            'depth': [request.form.get('depth')],
            'table': [request.form.get('table')],
            'x': [request.form.get('x')],
            'y': [request.form.get('y')],
            'z': [request.form.get('z')],
        }
        #"carat","cut","color","clarity","depth","table","price","x","y","z"
        for item in info:
            if (info[item] is None or info[item] == ''):
                flash("missing info")
                return render_template('index.html', result=result, error=True)

        df = pd.DataFrame.from_dict(info)
        df = md.encoder.transform(df)
        print(df)
        result = md.model.predict(df)[0]

    return render_template('index.html', result=result, error=False)
