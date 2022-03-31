from flask import Blueprint, render_template, request
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix="/")

@bp.route('/', methods=['GET'])
def index():
    search = request.args.get('search')
    db, c = get_db()

    if search is None:
        c.execute('SELECT * FROM estado')

    elif len(search) == 5:
        c.execute(
            '''SELECT estado, municipio, ciudad, cp, asentamiento FROM estado, municipio, colonia
            WHERE colonia.id_municipio = municipio.id AND municipio.id_estado = estado.id_estado 
            AND cp like %s''', ( '%' + search + '%', ))

    else:
        c.execute(
            '''SELECT estado, municipio, ciudad, cp, asentamiento FROM estado, municipio, colonia
            WHERE colonia.id_municipio = municipio.id AND municipio.id_estado = estado.id_estado 
            AND municipio like %s''', ( '%' + search + '%', ) )
    busq = c.fetchall()

    return render_template('cp/index.html', busq = busq)