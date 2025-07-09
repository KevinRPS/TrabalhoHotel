# etapa2_leitura.py

from modelos import Hospede
import time

def ler_arquivo(nome_arquivo):
    hospedes = []
    inicio = time.time()

    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            partes = linha.strip().split(";")

            nome = partes[0]
            idade = partes[1]
            quarto = partes[2]
            diaria = partes[3]
            contatos = partes[4].split(",")  # Convertendo string para lista
            data_entrada = partes[5]
            data_saida = partes[6]
            status = partes[7]

            hospede = Hospede(nome, idade, quarto, diaria, contatos, data_entrada, data_saida, status)
            hospedes.append(hospede)

    fim = time.time()
    print(f"Leitura de {nome_arquivo} feita em {round(fim - inicio, 2)} segundos.")
    return hospedes

# Exemplo de teste:
if __name__ == "__main__":
    lista = ler_arquivo("dados/hotel_pequeno.txt")
    print(lista[0])
