import csv

class Usuario:
    def __init__(self, nome, email, senha, nivel, categorias):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.nivel = nivel
        self.categorias = categorias

class Registro:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def carregar_usuarios(self):
        try:
            with open('usuarios.csv', 'r') as arquivo:
                reader = csv.DictReader(arquivo)
                for linha in reader:
                    usuario = Usuario(
                        linha['nome'],
                        linha['email'],
                        linha['senha'],
                        linha['nivel'],
                        [linha['categoria'] for linha in reader]
                    )
                    self.usuarios.append(usuario)
        except FileNotFoundError:
            pass

    def salvar_usuarios(self):
        with open('usuarios.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['nome', 'email', 'senha', 'nivel', 'categoria'])
            for usuario in self.usuarios:
                writer.writerow([usuario.nome, usuario.email, usuario.senha, usuario.nivel, ', '.join(usuario.categorias)])

    def imprimir_usuarios(self):
        for usuario in self.usuarios:
            print(f"Nome: {usuario.nome}, Email: {usuario.email}, Senha: {usuario.senha}, Nível: {usuario.nivel}, Categorias: {', '.join(usuario.categorias)}")


registro = Registro()
registro.carregar_usuarios()

while True:
    print("\n1. Adicionar usuário")
    print("2. Imprimir usuários")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        nivel = input("Nível: ")
        categorias = input("Categorias (separadas por vírgula): ").split(',')
        usuario = Usuario(nome, email, senha, nivel, categorias)
        registro.adicionar_usuario(usuario)
        registro.salvar_usuarios()
    elif opcao == '2':
        registro.imprimir_usuarios()
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")

# Cadastro de produtos 

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Registro:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def carregar_produtos(self):
        try:
            with open('produtos.csv', 'r') as arquivo:
                reader = csv.DictReader(arquivo)
                for linha in reader:
                    produto = Produto(
                        linha['nome'],
                        float(linha['preco']),
                        int(linha['quantidade'])
                    )
                    self.produtos.append(produto)
        except FileNotFoundError:
            pass

    def salvar_produtos(self):
        with open('produtos.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['nome', 'preco', 'quantidade'])
            for produto in self.produtos:
                writer.writerow([produto.nome, produto.preco, produto.quantidade])

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        return None

    def imprimir_produtos_ordenados_nome(self):
        for produto in sorted(self.produtos, key=lambda x: x.nome):
            print(f"Nome: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}")

    def imprimir_produtos_ordenados_preco(self):
        for produto in sorted(self.produtos, key=lambda x: x.preco):
            print(f"Nome: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}")

    def deletar_produto(self, nome):
        self.produtos = [produto for produto in self.produtos if produto.nome != nome]

    def atualizar_produto(self, nome, preco, quantidade):
        for produto in self.produtos:
            if produto.nome == nome:
                produto.preco = preco
                produto.quantidade = quantidade
                return
        print("Produto não encontrado.")

    def criar_produto(self, nome, preco, quantidade):
        self.produtos.append(Produto(nome, preco, quantidade))
        self.salvar_produtos()


registro = Registro()
registro.carregar_produtos()

while True:
    print("\n1. Adicionar produto")
    print("2. Buscar produto")
    print("3. Imprimir produtos ordenados por nome")
    print("4. Imprimir produtos ordenados por preço")
    print("5. Deletar produto")
    print("6. Atualizar produto")
    print("7. Criar produto")
    print("8. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        registro.adicionar_produto(Produto(nome, preco, quantidade))
        registro.salvar_produtos()
    elif opcao == '2':
        nome = input("Nome do produto: ")
        produto = registro.buscar_produto(nome)
        if produto:
            print(f"Nome: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}")
        else:
            print("Produto não encontrado.")
    elif opcao == '3':
        registro.imprimir_produtos_ordenados_nome()
    elif opcao == '4':
        registro.imprimir_produtos_ordenados_preco()
    elif opcao == '5':
        nome = input("Nome do produto: ")
        registro.deletar_produto(nome)
    elif opcao == '6':
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        registro.atualizar_produto(nome, preco, quantidade)
    elif opcao == '7':
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        registro.criar_produto(nome, preco, quantidade)
    elif opcao == '8':
        break
    else:
        print("Opção inválida. Tente novamente.")
