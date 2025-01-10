from peewee import Model, CharField, DateField, SqliteDatabase

db = SqliteDatabase('emprestimos.db')

class BaseModel(Model):
    class Meta:
        database = db

class Emprestimo(BaseModel):
    nome_aluno = CharField(max_length=255)   # Nome do aluno
    turma_aluno = CharField(max_length=50)   # Turma do aluno
    data_emprestimo = DateField()            # Data do empréstimo
    data_entrega = DateField(null=True)      # Data de entrega, pode ser nula
    titulo_livro = CharField(max_length=255) # Título do livro
    estado_livro = CharField(max_length=100) # Estado do livro


db.create_tables([Emprestimo])