import pyodbc

# Define connection string

option = input(
    "Digite a opção desejada (get / insert / update / delete/ id): ").lower()


def verifica_input(operation):
    list_operations = ["get", "insert", "update", "delete", "id"]
    if operation == list_operations[0]:  # get
        get(sql_connection)
    if operation == list_operations[1]:  # insert
        insert(sql_connection)
    if operation == list_operations[2]:  # update
        update(sql_connection)
    if operation == list_operations[3]:  # delete
        delete(sql_connection)
    if operation == list_operations[4]:  # get id
        get_id(sql_connection)


# Conexão  SQL server
sql_connection = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-5PQD9F8\SQLEXPRESS;"
    "Database=LOJA;"
    "Trusted_Connection=yes;")


def get(sql_connection):  # Select todos os itens
    cursor = sql_connection.cursor()
    cursor.execute("SELECT * FROM SIMPLES")
    for row in cursor:
        print(f'{row}')


def insert(sql_connection):  # Insert produto e preço
    nome = input("Digite o nome do produto a ser inserido: ")
    preco = int(input("Digite o preço do produto a ser inserido: "))

    # Inserindo os itens que deram entrada pelo usuário
    cursor = sql_connection.cursor()
    cursor.execute(
        "INSERT INTO SIMPLES (NOME, PRECO) VALUES (?,?)", (nome, preco))
    sql_connection.commit()

    # Pegando agora o ID do último valor inserido (máximo já que incrementa aut.)
    cursor.execute("SELECT MAX(IDPRODUTO) FROM SIMPLES ")
    for ID in cursor:
        last_id = ID[0]

    # Printando todos os valores
    print(f"Produto {nome} com valor {preco} inserido com id {last_id}")


def update(sql_connection):  # update price
    id_produto = int(input("Digite ID que deseja atualizar"))
    preco = int(input("Digite o novo preço"))
    cursor = sql_connection.cursor()
    cursor.execute(
        "UPDATE SIMPLES SET PRECO = ? WHERE IDPRODUTO = ?", (preco, id_produto))
    sql_connection.commit()


def delete(sql_connection):  # Delete produto por ID
    id_produto = int(input("Digite ID que deseja deletar"))
    cursor = sql_connection.cursor()
    cursor.execute(
        "DELETE FROM SIMPLES WHERE IDPRODUTO = ?", (id_produto))
    sql_connection.commit()
    print("Produto deletado")


def get_id(sql_connection):  # Nome pelo ID
    nome = input("Digite o nome do produto que deseja ver o ID: ")
    cursor = sql_connection.cursor()
    cursor.execute("SELECT IDPRODUTO FROM SIMPLES WHERE NOME = ?", (nome))
    for ID in cursor:  # a cada linha
        product_id = ID[0]  # pega o ID
    print(f"O ID do produto {nome} é {product_id}")
    return product_id


while option not in ["get", "insert", "update", "delete", "id"]:
    option = input(
        "Selecione opção get / insert / update / delete/ id ou 0 para sair").lower()
verifica_input(option)
