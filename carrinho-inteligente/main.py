# Define uma classe para representar um produto
class Produto:
    def __init__(self, chave, nome, preco):
        # Atributos do produto: chave identificadora, nome e preço
        self.chave = chave
        self.nome = nome
        self.preco = preco

# Define uma classe para representar o carrinho de compras
class Carrinho:
    def __init__(self):
        # Dicionário para armazenar os itens no carrinho, usando a chave do produto como índice
        self.itens = {}

    # Método para adicionar um item ao carrinho
    def adicionar_item(self, produto, quantidade):
        if produto.chave in self.itens:
            # Se o produto já está no carrinho, incrementa a quantidade
            self.itens[produto.chave]['quantidade'] += quantidade
        else:
            # Caso contrário, adiciona o produto com a quantidade informada
            self.itens[produto.chave] = {'produto': produto, 'quantidade': quantidade}

    # Método para remover um item do carrinho
    def remover_item(self, chave, quantidade):
        if chave in self.itens:
            if self.itens[chave]['quantidade'] > quantidade:
                # Se há mais do que a quantidade a ser removida, apenas subtrai
                self.itens[chave]['quantidade'] -= quantidade
            elif self.itens[chave]['quantidade'] == quantidade:
                # Se a quantidade é igual, remove o produto do carrinho
                del self.itens[chave]
            else:
                # Se a quantidade a remover é maior do que a existente, mostra erro
                print("Quantidade a remover é maior do que a quantidade no carrinho.")
        else:
            # Caso o produto não exista no carrinho
            print("Produto não encontrado no carrinho.")

    # Método para calcular o valor total do carrinho
    def calcular_total(self):
        # Multiplica o preço pela quantidade de cada produto e soma tudo
        return sum(item['produto'].preco * item['quantidade'] for item in self.itens.values())

    # Método para listar os itens do carrinho em formato de string
    def listar_itens(self):
        lista = []
        for item in self.itens.values():
            produto = item['produto']
            quantidade = item['quantidade']
            lista.append(f"{produto.nome} (x{quantidade}): R${produto.preco * quantidade:.2f}")
        return lista

# Função principal do programa
def main():
    # Criação do dicionário de produtos disponíveis
    produtos = {
        "001": Produto("001", "Arroz", 5.50),
        "002": Produto("002", "Feijão", 4.00),
        "003": Produto("003", "Macarrão", 3.00),
        "004": Produto("004", "Açúcar", 2.50),
        "005": Produto("005", "Sal", 1.20),
        "006": Produto("006", "Óleo", 6.00),
        "007": Produto("007", "Leite", 3.50),
        "008": Produto("008", "Pão", 2.00),
        "009": Produto("009", "Queijo", 10.00),
        "010": Produto("010", "Presunto", 8.00),
    }

    # Criação de um novo carrinho
    carrinho = Carrinho()
    
    # Exibe a lista de produtos disponíveis
    print("Produtos disponíveis:")
    for chave, produto in produtos.items():
        print(f"Chave: {chave} - Produto: {produto.nome} - Preço: R${produto.preco:.2f}")

    # Loop principal do menu
    while True:
        print("\nOpções:")
        print("1. Adicionar produto ao carrinho")
        print("2. Ver itens no carrinho e total")
        print("3. Remover produto do carrinho")
        print("4. Finalizar compra")
        print("5. Sair")

        # Lê a opção do usuário
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            # Adicionar item ao carrinho
            chave = input("Digite a chave do produto que deseja adicionar ao carrinho: ")
            if chave in produtos:
                quantidade = int(input("Digite a quantidade que deseja adicionar: "))
                carrinho.adicionar_item(produtos[chave], quantidade)
                print(f"{quantidade} unidade(s) de '{produtos[chave].nome}' adicionada(s) ao carrinho.")
            else:
                print("Produto não encontrado. Tente novamente.")
        
        elif opcao == '2':
            # Exibir itens do carrinho e total
            print("\nItens no carrinho:")
            if carrinho.itens:
                for item in carrinho.listar_itens():
                    print(item)
                total = carrinho.calcular_total()
                print(f"\nValor total da compra: R${total:.2f}")
            else:
                print("O carrinho está vazio.")

        elif opcao == '3':
            # Remover item do carrinho
            chave = input("Digite a chave do produto que deseja remover do carrinho: ")
            if chave in produtos:
                quantidade = int(input("Digite a quantidade que deseja remover: "))
                carrinho.remover_item(chave, quantidade)
                print(f"{quantidade} unidade(s) de '{produtos[chave].nome}' removida(s) do carrinho.")
            else:
                print("Produto não encontrado no carrinho.")

        elif opcao == '4':
            # Finalizar compra e exibir total
            print("\nFinalizando a compra...")
            total = carrinho.calcular_total()
            print(f"Valor total da compra: R${total:.2f}")
            break

        else:
            # Opção inválida
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
