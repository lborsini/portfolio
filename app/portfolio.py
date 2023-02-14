from flask import(
    Blueprint, render_template, request, url_for, redirect, current_app
)

bp = Blueprint('portfolio', __name__, url_prefix="/")


@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')

@bp.route('/mail', methods=['GET', 'POST'])
def mail():
    return render_template('portfolio/sent-mail.html')
