import streamlit as st

st.set_page_config(layout='wide')

criarEmprestimo = st.Page(
    "pages/criar_emprestimo.py",
    title="Cadastrar empréstimo",
    icon=":material/add_circle:",
    default=True
)

checarEmprestimo = st.Page(
    "pages/checar_emprestimos.py",
    title="Empréstimos de hoje",
    icon=":material/today:"
)

visualizarEmprestimo = st.Page(
    "pages/visualizar_emprestimos.py",
    title="Visualizar Empréstimos",
    icon=":material/date_range:"
)



acoesEmprestimo = [criarEmprestimo, checarEmprestimo, visualizarEmprestimo]

st.title("Bem vindo(a) ao Bibliocheck**")
st.caption("**seu assistente de empréstimos!")

page_dict = {}


page_dict["Ações de Empréstimo"] = acoesEmprestimo


pg = st.navigation(page_dict)
pg.run()
