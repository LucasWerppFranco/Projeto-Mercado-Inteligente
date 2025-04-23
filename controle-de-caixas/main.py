# Importa bibliotecas padrão
import random  # Para gerar números aleatórios
import time    # Para adicionar pausas na execução

# Função que simula o número de clientes em um mercado
def gerar_numero_de_clientes():
    # Lista de mensagens que serão exibidas com base na quantidade de clientes
    mensagens = [
        "Número baixo! - Dois caixas abertos.",
        "Número médio! - Tres caixas abertos",
        "Número alto! - Quatro caixas abertos",
        "Número muito alto! - Cinco caixas abertos",
        "Número máximo! - Seis caixas abertos",
    ]

    # Variável para guardar o último número de clientes mostrado
    ultimo_numero = -1

    # Loop infinito que simula continuamente o fluxo de clientes
    while True:
        # Gera um número aleatório entre 10 e 60 representando o número de clientes
        clientes = random.randint(10, 60)
        print(f"Número de clientes no mercado: {clientes}")

        # Verifica se é a primeira execução ou se a variação no número de clientes foi significativa (>=10)
        if ultimo_numero == -1 or abs(clientes - ultimo_numero) >= 10:
            # Compara o número de clientes para escolher a mensagem apropriada
            if clientes < 20:
                print(mensagens[0])
            elif clientes < 30:
                print(mensagens[1])
            elif clientes < 40:
                print(mensagens[2])
            elif clientes < 50:
                print(mensagens[3])
            else:
                print(mensagens[4])

            # Atualiza o último número de clientes
            ultimo_numero = clientes

        # Aguarda 5 segundos antes de repetir o processo
        time.sleep(5)

# Chamada da função para iniciar a simulação
gerar_numero_de_clientes()
