from flask import Blueprint, render_template, request, flash, redirect
from database import db
from models import Autor

bp_autores = Blueprint('autores', __name__, template_folder="templates")

@bp_autores.route('/')
def index():
    a = Autor.query.all()
    return render_template('autores.html', autor = a)

@bp_autores.route('/add')
def add():
    return render_template('autores_add.html')

@bp_autores.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    instituicao = request.form.get('instituicao')
    if nome and instituicao:
        bd_autor = Autor(nome, instituicao)
        db.session.add(bd_autor)
        db.session.commit()
        flash('Autor salvo com sucesso!!!')
        return redirect('/autores')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/autores/add')
    