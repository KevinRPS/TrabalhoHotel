# etapa3_interacao.py

from modelos import Hospede
from LeituraDeDados import ler_arquivo
import time
from datetime import datetime, date

import funcoes

def menu():
    print("\n===== MENU =====")
    print("1. Adicionar hóspede")
    print("2. Remover hóspede")
    print("3. Buscar hóspedes por filtro")
    print("5. Extrair relatório de hóspede")
    print("6. Editar hóspede existente")
    print("0. Sair")


def interacao(lista_hospedes):
        menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            nome = funcoes.validar_nome()
            idade = funcoes.validar_idade()
            quarto = funcoes.validar_quarto()
            diaria = funcoes.validar_diaria()
            contatos = funcoes.ler_contatos()
            data_entrada, data_checkin = funcoes.obter_checkin()
            data_saida = funcoes.ler_data_saida(data_checkin)
            status = funcoes.ler_status()
            novo = Hospede(nome, idade, quarto, diaria, contatos, data_entrada, data_saida, status)
            funcoes.adicionar_hospede(lista_hospedes, novo)
            funcoes.salvar_arquivo(lista_hospedes, "dados/hotel_pequeno.txt")


        elif escolha == "2":
            nome = input("Nome do hóspede a remover: ")
            funcoes.remover_hospede(lista_hospedes, nome)
        
        elif escolha == "3":
            print("\nFiltros disponíveis: nome, quarto, status, data_entrada")
            campo = input("Buscar por qual campo? ").lower()
            valor = input("Valor do filtro: ")
            encontrados = funcoes.buscar_hospedes(lista_hospedes, campo, valor)
            
            if encontrados:
                print(f"\n{len(encontrados)} hóspede(s) encontrado(s):\n")
                for h in encontrados:
                    print(f"{h.nome}, Quarto {h.quarto}, Entrada: {h.data_entrada}, Status: {h.status}")
            else:
                print("❌ Nenhum hóspede encontrado com esse filtro.")


        elif escolha == "4":
            nome_arquivo = input("Nome do arquivo para salvar (ex: dados/novo.txt): ")
            funcoes.salvar_arquivo(lista_hospedes, nome_arquivo)

        elif escolha == "5":
            nome = input("Nome do hóspede para gerar o relatório: ")
            funcoes.extrair_relatorio(lista_hospedes, nome)

        elif escolha == "6":
            nome = input("Nome do hóspede que deseja editar: ")
            funcoes.editar_hospede(lista_hospedes, nome)


        elif escolha == "0":
                print("Saindo...")

        else:
            print("Opção inválida. Tente novamente.")
            interacao(lista_hospedes)

if __name__ == "__main__":
    lista_hospedes = ler_arquivo("dados/hotel_pequeno.txt")
    interacao(lista_hospedes)


