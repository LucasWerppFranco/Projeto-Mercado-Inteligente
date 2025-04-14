import random
import time


def gerar_numero_de_clientes():
    mensagens = [
        "Número baixo! - Dois caixas abertos.\n ---",
        "Número médio! - Tres caixas abertos.\n ---",
        "Número alto! - Quatro caixas abertos.\n ---",
        "Número muito alto! - Cinco caixas abertos.\n ---",
        "Número máximo! - Seis caixas abertos.\n ---",
    ]

    ultimo_numero = -1
    while True:
        clientes = random.randint(10, 60)
        print(f"Número de clientes no mercado: {clientes}")

        if ultimo_numero == -1 or abs(clientes - ultimo_numero) >= 10:
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

            ultimo_numero = clientes

        time.sleep(5)


gerar_numero_de_clientes()
