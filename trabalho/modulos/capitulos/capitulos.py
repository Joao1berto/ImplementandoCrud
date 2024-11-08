from flask import Blueprint, render_template, request, flash, redirect
from database import db
from models import Capitulos

bp_capitulos = Blueprint('capitulos', __name__, template_folder="templates")

@bp_capitulos.route('/')
def index():
    c = Capitulos.query.all()
    return render_template('capitulo.html', capitulo = c)

@bp_capitulos.route('/add')
def add():
    return render_template('capitulo_add.html')

@bp_capitulos.route('/save', methods=['POST'])
def save():
    titulo = request.form.get('titulo')
    pagina_inicial = request.form.get('pagina_inicial')
    id_autor = request.form.get('id_autor')
    if titulo and pagina_inicial and id_autor:
        bd_capitulo = Capitulos(titulo, pagina_inicial, id_autor)
        db.session.add(bd_capitulo)
        db.session.commit()
        flash('Capitulo salvo com sucesso!!!')
        return redirect('/capitulos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/capitulos/add')
    