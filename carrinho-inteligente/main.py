class Produto:
    def __init__(self, chave, nome, preco):
        self.chave = chave
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, produto, quantidade):
        if produto.chave in self.itens:
            self.itens[produto.chave]['quantidade'] += quantidade
        else:
            self.itens[produto.chave] = {'produto': produto, 'quantidade': quantidade}

    def remover_item(self, chave, quantidade):
        if chave in self.itens:
            if self.itens[chave]['quantidade'] > quantidade:
                self.itens[chave]['quantidade'] -= quantidade
            elif self.itens[chave]['quantidade'] == quantidade:
                del self.itens[chave]
            else:
                print("Quantidade a remover é maior do que a quantidade no carrinho.")
        else:
            print("Produto não encontrado no carrinho.")

    def calcular_total(self):
        return sum(item['produto'].preco * item['quantidade'] for item in self.itens.values())

    def listar_itens(self):
        lista = []
        for item in self.itens.values():
            produto = item['produto']
            quantidade = item['quantidade']
            lista.append(f"{produto.nome} (x{quantidade}): R${produto.preco * quantidade:.2f}")
        return lista

def main():
    # Criando alguns produtos
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

    carrinho = Carrinho()

    # Exibindo as chaves e produtos disponíveis
    print("Produtos disponíveis:")
    for chave, produto in produtos.items():
        print(f"Chave: {chave} - Produto: {produto.nome} - Preço: R${produto.preco:.2f}")

    while True:
        print("\nOpções:")
        print("1. Adicionar produto ao carrinho")
        print("2. Ver itens no carrinho e total")
        print("3. Remover produto do carrinho")
        print("4. Finalizar compra")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            chave = input("Digite a chave do produto que deseja adicionar ao carrinho: ")
            if chave in produtos:
                quantidade = int(input("Digite a quantidade que deseja adicionar: "))
                carrinho.adicionar_item(produtos[chave], quantidade)
                print(f"{quantidade} unidade(s) de '{produtos[chave].nome}' adicionada(s) ao carrinho.")
            else:
                print("Produto não encontrado. Tente novamente.")
        
        elif opcao == '2':
            print("\nItens no carrinho:")
            if carrinho.itens:
                for item in carrinho.listar_itens():
                    print(item)
                total = carrinho.calcular_total()
                print(f"\nValor total da compra: R${total:.2f}")
            else:
                print("O carrinho está vazio.")

        elif opcao == '3':
            chave = input("Digite a chave do produto que deseja remover do carrinho: ")
            if chave in produtos:
                quantidade = int(input("Digite a quantidade que deseja remover: "))
                carrinho.remover_item(chave, quantidade)
                print(f"{quantidade} unidade(s) de '{produtos[chave].nome}' removida(s) do carrinho.")
            else:
                print("Produto não encontrado no carrinho.")

        elif opcao == '4':
            print("\nFinalizando a compra...")
            total = carrinho.calcular_total()
            print(f"Valor total da compra: R${total:.2f}")
            break

        else:

            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":

    main()
