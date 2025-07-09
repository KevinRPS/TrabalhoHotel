from modelos import Hospede
from LeituraDeDados import ler_arquivo
import time
from datetime import datetime, date



def buscar_hospedes(lista, campo, valor):
    resultados = []
    for h in lista:
        if campo == "nome" and valor.lower() in h.nome.lower():
            resultados.append(h)
        elif campo == "quarto" and str(h.quarto) == str(valor):
            resultados.append(h)
        elif campo == "status" and valor.lower() in h.status.lower():
            resultados.append(h)
        elif campo == "data_entrada" and valor == h.data_entrada:
            resultados.append(h)
    return resultados



def ler_data_saida(data_checkin: date) -> str:
    """
    Solicita ao usuário uma data de saída no formato dd/mm/aaaa,
    valida o formato e garante que seja POSTERIOR a data_checkin.
    Retorna a string da data no formato dd/mm/aaaa.
    """
    while True:
        entrada = input("Data de saída (dd/mm/aaaa): ")
        try:
            saida = datetime.strptime(entrada, "%d/%m/%Y").date()
            if saida <= data_checkin:
                print("❌ Data de saída deve ser após o check‑in.")
            else:
                return entrada
        except ValueError:
            print("❌ Formato inválido. Use dd/mm/aaaa.")

def obter_checkin():
    """
    Retorna a data atual no formato dd/mm/aaaa (sem hora)
    e a data como objeto para validação posterior.
    """
    agora = datetime.now()
    data_str = agora.strftime("%d/%m/%Y")  # <-- só data
    data_obj = agora.date()                # <-- objeto date
    return data_str, data_obj

def ler_contatos():
    contatos = []
    qtd = int(input("Quantos contatos de emergência quer cadastrar? "))
    for _ in range(qtd):
        # Lê e valida DDD
        while True:
            ddd = input("DDD (2 dígitos): ")
            if ddd.isdigit() and len(ddd) == 2:
                break
            print("DDD inválido. Informe 2 dígitos.")
        # Lê e valida número de 9 dígitos
        while True:
            num = input("Número (9 dígitos, sem espaço): ")
            if num.isdigit() and len(num) == 9:
                break
            print("Número inválido. Deve ter 9 dígitos.")
        contatos.append(f"({ddd})9{num[:4]}-{num[4:]}")
    return contatos


def adicionar_hospede(lista_hospedes, novo_hospede):
    inicio = time.time()
    lista_hospedes.append(novo_hospede)
    fim = time.time()
    print(f"Hóspede adicionado em {round((fim - inicio)*1000, 2)} ms.")
    salvar_arquivo(lista_hospedes, "dados/hotel_pequeno.txt")

def remover_hospede(lista_hospedes, nome):
    inicio = time.time()
    removidos = [h for h in lista_hospedes if h.nome == nome]
    lista_hospedes[:] = [h for h in lista_hospedes if h.nome != nome]
    fim = time.time()
    print(f"Remoção de {len(removidos)} hóspede(s) em {round((fim - inicio)*1000, 2)} ms.")
    salvar_arquivo(lista_hospedes, "dados/hotel_pequeno.txt")


def buscar_hospede(lista_hospedes, nome):
    inicio = time.time()
    encontrados = [h for h in lista_hospedes if nome.lower() in h.nome.lower()]
    fim = time.time()
    print(f"Busca retornou {len(encontrados)} hóspede(s) em {round((fim - inicio)*1000, 2)} ms.")
    return encontrados

def salvar_arquivo(lista_hospedes, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        for h in lista_hospedes:
            contatos_str = ",".join(h.contatos)
            linha = f"{h.nome};{h.idade};{h.quarto};{h.diaria};{contatos_str};{h.data_entrada};{h.data_saida};{h.status}\n"
            f.write(linha)
    print(f"✅ Arquivo salvo com sucesso em: {nome_arquivo}")


def extrair_relatorio(lista_hospedes, nome):
    encontrados = [h for h in lista_hospedes if h.nome.lower() == nome.lower()]
    
    if not encontrados:
        print("❌ Hóspede não encontrado.")
        return

    for h in encontrados:
        data_entrada = datetime.strptime(h.data_entrada, "%d/%m/%Y")
        saida = datetime.strptime(h.data_saida, "%d/%m/%Y")
        dias = (saida - data_entrada).days
        total = dias * h.diaria

        print("\n===== RELATÓRIO DO HÓSPEDE =====")
        print(f"Nome: {h.nome}")
        print(f"Idade: {h.idade}")
        print(f"Quarto: {h.quarto}")
        print(f"Diária: R$ {h.diaria:.2f}")
        print("Contatos:", ", ".join(h.contatos))
        print(f"Data de entrada: {h.data_entrada}")
        print(f"Data de saída: {h.data_saida}")
        print(f"Status: {h.status}")
        print(f"Total de dias: {dias}")
        print(f"💰 Total a pagar: R$ {total:.2f}")
        print("===============================")

def ler_status():
    opcoes = ["reservado", "hospedado", "livre", "offline"]
    
    print("Escolha o novo status:")
    for i, status in enumerate(opcoes, 1):
        print(f"{i}. {status.title()}")

    while True:
        escolha = input("Opção (1-4): ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(opcoes):
                return opcoes[escolha - 1]
        print("❌ Opção inválida. Tente novamente.")


def editar_hospede(lista_hospedes, nome):
    encontrados = [h for h in lista_hospedes if nome.lower() in h.nome.lower()]
    if not encontrados:
        print("❌ Hóspede não encontrado.")
        return
    
    for h in encontrados:
        print(f"\nEditando: {h.nome} (Quarto {h.quarto})")

        if input("Editar idade? (s/n): ").lower() == 's':
            h.idade = int(input("Nova idade: "))
        
        if input("Editar quarto? (s/n): ").lower() == 's':
            h.quarto = int(input("Novo número do quarto: "))
        
        if input("Editar diária? (s/n): ").lower() == 's':
            h.diaria = float(input("Nova diária: "))
        
        if input("Editar contatos? (s/n): ").lower() == 's':
            h.contatos = ler_contatos()

        if input("Editar data de saída? (s/n): ").lower() == 's':
            entrada = datetime.strptime(h.data_entrada, "%d/%m/%Y").date()
            h.data_saida = ler_data_saida(entrada)

        if input("Editar status? (s/n): ").lower() == 's':
            h.status = ler_status()

        print(f"✅ Hóspede '{h.nome}' atualizado com sucesso.\n")

 
# Validadores
def validar_nome():
    while True:
        try:
            nome = input("Digite seu nome! ")
            if nome == "":
                print("❌ Campo obrigatório. Digite algo.")
        except ValueError:
            print("❌ Você precisa digitar seu nome.")
        
def validar_idade():
    while True:
        entrada = input("Digite a idade: ").strip()
        if entrada == "":
            print("❌ Campo obrigatório. Digite algo.")
            continue
        if not entrada.isdigit():
            print("❌ Apenas números inteiros são aceitos.")
            continue

        idade = int(entrada)
        if idade <= 17:
            print("🚫 O usuário precisa ter 18 anos ou mais.")
            continue
        return idade


       


def validar_diaria():
    while True:
        try:
            diaria = input("Digite o valor da diaria!")
            if not diaria:
                print("❌ Campo obrigatório. Digite algo.")
            diaria = int(diaria)
            while diaria <= 0:
                print("Valor inválido")
                diaria = validar_diaria(int(input("Digite uma diaria valida!")))
            return diaria
        except ValueError:
            print("❌ Você precisa digitar números inteiros.")

def validar_quarto():
    while True:
        entrada = input("Digite o Quarto: ").strip()
        if not entrada:
            print("❌ Campo obrigatório. Digite algo.")
            continue
        try:
            valor = int(entrada)
            if valor <= 0:
                print("❌ O número do quarto deve ser positivo.")
            else:
                return valor
        except ValueError:
            print("❌ Você deve digitar um número inteiro válido.")


# Função segura de input
def ler_inteiro_seguro(mensagem, minimo=1):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"❌ Valor deve ser ≥ {minimo}")
                continue
            return valor
        except ValueError:
            print("❌ Valor inválido.")