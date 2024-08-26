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

menu = """
        INFORME O QUE DESEJA
    ----------------------------
    -(C)riar Table
    -(I)nserir no Banco
    -(S)elecionar Table
    -(V)azar
"""

while True:
    print(menu)
    opcao = input("Informe a escolha: ").upper()[0]
    cursor = con.cursor()

    if opcao == "C":
        ddl_pets = """
        CREATE TABLE pets(
        id NUMBER(10),
        nome VARCHAR2(50),
        raca VARCHAR2(25),
        nome_tutor VARCHAR2(100),
        CONSTRAINT pets_pk PRIMARY KEY (id)
        )
        """
        cursor.execute(ddl_pets)
        print("Tabela Criada")
        print("Database version: ", con.version)
        con.commit()
    
    elif opcao == "I":
        id = input("Informe o id: ")
        nome = input("Informe o nome: ")
        raca = input("Informe a raça: ")
        nome_tutor = input("Informe o nome do Dono: ")

        sql = f"""
            INSERT INTO pets(id, nome, raca, nome_tutor)
            VALUES({id}, '{nome}', '{raca}', '{nome_tutor}')
        """
        cursor.execute(sql)
        con.commit()
    elif opcao == "S":
        sql = "SELECT * FROM pets ORDER BY id"
        times = cursor.execute(sql)
        for time in times:
            print(time)
    elif opcao == "V":
        print("Até Breve")
        break
    else:
        print("Por Favor um Valor Válido")