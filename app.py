from flask import Flask, render_template, request, url_for, redirect
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from database import Base, nova_sessao, engine
from models import Livro, Usuario

app = Flask(__name__)
Base.metadata.create_all(engine)

# .options(joinedload(Usuario.livros))
@app.route('/')
def index():

    with nova_sessao() as session:
        usuarios = session.scalars(select(Usuario).options(selectinload(Usuario.livros))).unique().all()
        livros = session.scalars(select(Livro).options(selectinload(Livro.usuario)))

    return render_template('index.html', usuarios=usuarios, livros=livros)


@app.route('/usuario/novo', methods=['POST', 'GET'])
def form_usuario():
    if request.method == 'POST':
        usuario = Usuario(
            nome=request.form.get('nome'),
            email=request.form.get('email')
        )
        with nova_sessao() as session:
            session.add(usuario)
            session.commit()

        return redirect(url_for('index'))
    return render_template('form_usuario.html')


@app.route('/livros/novo', methods=['GET', 'POST'])
def form_livro():

    if request.method == 'GET':
        with nova_sessao() as session:
            usuarios = session.scalars(select(Usuario).order_by(Usuario.nome)).all()
            return render_template('form_livro.html', usuarios=usuarios)
        
    if request.method == 'POST':
        with nova_sessao() as session:
            
            livro = Livro(
                titulo=request.form.get('titulo'),
                id_usuario=int(request.form.get('usuario_id')),
            )

            session.add(livro)
            session.commit()
            return redirect(url_for('index'))
        
    

@app.route('/livros/listar', methods=['GET'])
def listar_livros():
    with nova_sessao() as session:
        statement = select(Livro).order_by(Livro.titulo)
        livros = session.scalars(statement).all()

        return render_template('index.html', livros=livros)

@app.route('/usuarios/listar', methods=['GET'])
def listar_usuarios():
    with nova_sessao() as session:
        statement = select(Usuario).order_by(Usuario.nome)
        usuarios = session.scalars(statement).all()

        return render_template('index.html', usuarios=usuarios)

@app.route('/logout')
def logout():
    pass

if __name__ == "__main__":
    app.run(debug=True)