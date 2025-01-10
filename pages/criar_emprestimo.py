import streamlit as st
from datetime import datetime, timedelta
from peewee import fn
from database.models import Emprestimo, db  # Importando o modelo e o banco de dados

def create_emprestimo(nome_aluno, turma_aluno, data_emprestimo, titulo_livro, estado_livro, data_entrega=None):
    with db.atomic():
        nome_formatado = ' '.join([nome.capitalize() for nome in nome_aluno.split()])
        Emprestimo.create(
            nome_aluno=nome_formatado,
            turma_aluno=turma_aluno,
            data_emprestimo=data_emprestimo,
            data_entrega=data_entrega,
            titulo_livro=titulo_livro,
            estado_livro=estado_livro
        )

def read_emprestimos():
    emprestimos = Emprestimo.select()
    return [
        {
            "id": e.id,
            "nome_aluno": e.nome_aluno,
            "turma_aluno": e.turma_aluno,
            "data_emprestimo": e.data_emprestimo.isoformat(),
            "data_entrega": e.data_entrega.isoformat() if e.data_entrega else None,
            "titulo_livro": e.titulo_livro,
            "estado_livro": e.estado_livro
        }
        for e in emprestimos
    ]

def update_emprestimo(filtros, novos_dados):
    query = Emprestimo.select()
    
    if 'id' in filtros:
        query = query.where(Emprestimo.id == filtros['id'])
    if 'nome_aluno' in filtros:
        query = query.where(Emprestimo.nome_aluno == filtros['nome_aluno'])
    if 'turma_aluno' in filtros:
        query = query.where(Emprestimo.turma_aluno == filtros['turma_aluno'])
    if 'data_emprestimo' in filtros:
        query = query.where(Emprestimo.data_emprestimo == filtros['data_emprestimo'])
    if 'titulo_livro' in filtros:
        query = query.where(Emprestimo.titulo_livro == filtros['titulo_livro'])
    if 'estado_livro' in filtros:
        query = query.where(Emprestimo.estado_livro == filtros['estado_livro'])
    
    with db.atomic():
        for emprestimo in query:
            emprestimo.nome_aluno = novos_dados.get('nome_aluno', emprestimo.nome_aluno)
            emprestimo.turma_aluno = novos_dados.get('turma_aluno', emprestimo.turma_aluno)
            emprestimo.data_emprestimo = novos_dados.get('data_emprestimo', emprestimo.data_emprestimo)
            emprestimo.data_entrega = novos_dados.get('data_entrega', emprestimo.data_entrega)
            emprestimo.titulo_livro = novos_dados.get('titulo_livro', emprestimo.titulo_livro)
            emprestimo.estado_livro = novos_dados.get('estado_livro', emprestimo.estado_livro)
            emprestimo.save()

def delete_emprestimo(filtros):
    query = Emprestimo.select()
    
    if 'id' in filtros:
        query = query.where(Emprestimo.id == filtros['id'])
    if 'nome_aluno' in filtros:
        query = query.where(Emprestimo.nome_aluno == filtros['nome_aluno'])
    if 'turma_aluno' in filtros:
        query = query.where(Emprestimo.turma_aluno == filtros['turma_aluno'])
    if 'data_emprestimo' in filtros:
        query = query.where(Emprestimo.data_emprestimo == filtros['data_emprestimo'])
    if 'titulo_livro' in filtros:
        query = query.where(Emprestimo.titulo_livro == filtros['titulo_livro'])
    if 'estado_livro' in filtros:
        query = query.where(Emprestimo.estado_livro == filtros['estado_livro'])
    
    with db.atomic():
        query.delete_instance()


def prazo_padrao():
    # Obtém a data atual
    data_emprestimo = datetime.now()
    
    # Adiciona 7 dias à data de empréstimo
    data_entrega = data_emprestimo + timedelta(days=7)
    
    return data_entrega




st.subheader("Informações do Livro")
col1, col2 = st.columns(2)
with col1:
    estadoLivro = st.selectbox('Estado:', ["OK", "Danificado"])
with col2:
    tituloLivro = st.text_input("Título:")

st.subheader("Informações do aluno")
nomeAluno = st.text_input("Nome completo do aluno:")
turmaAluno = st.text_input("Turma do Aluno:")
col1,col2 = st.columns(2)
with col1:
    dataEmprestimo = st.date_input('Data do Empréstimo:', value='today', format="DD/MM/YYYY")
with col2:
    dataEntrega = st.date_input('Data da Entrega:', value=prazo_padrao(), format="DD/MM/YYYY")
criarRegistro = st.button('Cadastrar empréstimo', use_container_width=True, on_click=create_emprestimo, args=[nomeAluno, turmaAluno, dataEmprestimo, tituloLivro, estadoLivro, dataEntrega])