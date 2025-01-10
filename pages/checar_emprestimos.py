import streamlit as st
import pandas as pd
from datetime import datetime
from database.models import Emprestimo 

def mostrar_registros_hoje():
    # Obtém a data de hoje
    hoje = datetime.now().date()
    
    # Busca os registros de empréstimo com a data de hoje
    registros_hoje = Emprestimo.select().where(Emprestimo.data_emprestimo == hoje)
    
    # Verifica se não encontrou registros
    if registros_hoje.count() == 0:
        return "Não há registros"
    
    # Cria uma lista de dicionários com os dados dos registros
    registros = [
        {
            "ID": emprestimo.id,
            "Nome": emprestimo.nome_aluno,
            "Turma": emprestimo.turma_aluno,
            "Data Empréstimo": emprestimo.data_emprestimo,
            "Data Entrega": emprestimo.data_entrega,
            "Título": emprestimo.titulo_livro,
            "Estado do Livro": emprestimo.estado_livro
        }
        for emprestimo in registros_hoje
    ]
    
    # Converte a lista de dicionários em um DataFrame
    df = pd.DataFrame(registros)
    
    return df

st.subheader("Estes são os empréstimos de hoje:")

emprestimosDeHoje = mostrar_registros_hoje()
st.write(emprestimosDeHoje)