import os
import oracledb

usuario = os.environ.get("PYTHON_ORACLE_USER")
senha = os.environ.get("PYTHON_ORACLE_PASS")
db_path='oracle.fiap.com.br:1521/orcl'

print("Usuario: ", usuario)

con = oracledb.connect(
    user=usuario,
    password=senha,
    dsn=db_path
)

sql = """
    INSERT INTO times_futebol(id, nome, jogadores, vitorias, derrotas, empates, animo)
    VALUES(3, 'Vasco', 0, 0, 30, 0, 0)
"""

cursor = con.cursor()
cursor.execute(sql)
con.commit()
print("Feito com sucesso")