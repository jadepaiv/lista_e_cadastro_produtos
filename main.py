import json

def carregar_produtos():
    try:
        with open('produtos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_produtos(produtos):
    with open('produtos.json', 'w') as file:
        json.dump(produtos, file, indent=4)

def cadastrar_produto(produtos):
    nome = input("Nome do Produto: ")
    descricao = input("Descrição do Produto: ")
    valor = float(input("Valor do Produto: "))
    disponivel = input("Disponível para Venda (sim/não): ").strip().lower()
    
    produto = {
        'nome': nome,
        'descricao': descricao,
        'valor': valor,
        'disponivel': disponivel
    }
    
    produtos.append(produto)
    salvar_produtos(produtos)
    print("Produto cadastrado com sucesso!")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    produtos_ordenados = sorted(produtos, key=lambda x: x['valor'])
    print(f"{'Nome':<20} {'Valor':<10}")
    print("-" * 30)
    for produto in produtos_ordenados:
        print(f"{produto['nome']:<20} {produto['valor']:<10}")

def menu():
    produtos = carregar_produtos()
    
    while True:
        print("\n1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cadastrar_produto(produtos)
        elif escolha == '2':
            listar_produtos(produtos)
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
