import random
import time
from faker import Faker
from datetime import datetime, timedelta
fake = Faker('pt_BR')  # Nomes e dados em português do Brasil

def gerar_dados(qtd):
    dados = []
    for _ in range(qtd):
        nome = fake.name()
        idade = random.randint(18, 70)
        quarto = random.randint(0, 500)
        diaria = round(random.uniform(100, 500), 2)
        contatos = [f"({random.randint(10,99)})9{random.randint(1000,9999)}-{random.randint(1000,9999)}"
                    for _ in range(random.randint(1, 3))]

        # Novas colunas 
        data_entrada = fake.date_between(start_date='-30d', end_date='today')
        data_saida = data_entrada + timedelta(days=random.randint(1, 14))
        status = random.choice(["Ativa", "Concluída", "Cancelada"])

        dados.append([
            nome, idade, quarto, diaria, contatos,
            data_entrada.strftime('%d/%m/%Y'),
            data_saida.strftime('%d/%m/%Y'),
            status
        ])
    return dados

def salvar_arquivo(dados, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        for nome, idade, quarto, diaria, contatos, data_entrada, data_saida, status in dados:
            contatos_str = ",".join(contatos)
            linha = f"{nome};{idade};{quarto};{diaria};{contatos_str};{data_entrada};{data_saida};{status}\n"
            f.write(linha)

def gerar_e_salvar_arquivo(tamanho, nome_arquivo):
    inicio = time.time()
    dados = gerar_dados(tamanho)
    salvar_arquivo(dados, nome_arquivo)
    fim = time.time()
    print(f"{nome_arquivo} gerado com {tamanho} registros em {round(fim - inicio, 2)} segundos.")

if __name__ == "__main__":
    while True:
        try:
            qtd = int(input("Quantos dados deseja gerar? "))
            if qtd <= 0:
                print("Por favor, insira um número inteiro positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    gerar_e_salvar_arquivo(qtd, "dados/hotel_pequeno.txt")
