from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('ml', __name__, url_prefix='/ml')

@bp.route('/', methods=('GET', 'POST'))
def predict():
    if request.method == 'POST':
        cut = request.form['cut']
        carat = request.form['carat']
        error = None

        if not cut:
            error = 'Cut is required.'
        elif not carat:
            error = 'Carat is required.'

        if error is None:
            print("ok")
        else:
            return redirect(url_for("auth.login", ))

        flash(error)

    return render_template('index.html')

@bp.route('/results')
def results():
    return "hello"
