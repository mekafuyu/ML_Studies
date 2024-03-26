from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('ml', __name__, url_prefix='/ml')

@bp.route('/hello', methods=('GET', 'POST'))
def register():
    return render_template('index.html')