from reactpy import component, html, use_state
from LeituraDeDados import ler_arquivo
from funcoes import adicionar_hospede, salvar_arquivo
from modelos import Hospede
from datetime import datetime
# dentro de telas.py

@component
def menu_dashboard(ir_para_tela):
    return html.div(
        {"style": {"padding": "2rem", "color": "black"}},
        html.h2("🏨 Menu Principal"),
        html.ul(
            html.li(html.button({"on_click": lambda e: ir_para_tela("adicionar")}, "➕ Adicionar Cliente")),
            html.li(html.button({"on_click": lambda e: ir_para_tela("remover")}, "❌ Remover Cliente")),
            html.li(html.button({"on_click": lambda e: ir_para_tela("editar")}, "✏️ Editar Cliente")),
            html.li(html.button({"on_click": lambda e: ir_para_tela("relatorio")}, "📊 Relatório")),
            html.li(html.button({"on_click": lambda e: ir_para_tela("config")}, "⚙️ Configurações")),
            html.li(html.button({"on_click": lambda e: ir_para_tela("desligar")}, "⛔ Desligar Sistema")),
        )
    )


@component
def tela_adicionar(voltar):
    nome, set_nome = use_state("")
    idade, set_idade = use_state("")
    quarto, set_quarto = use_state("")
    diaria, set_diaria = use_state("")
    contatos, set_contatos = use_state("")
    status, set_status = use_state("reservado")
    mensagem, set_mensagem = use_state("")

    def registrar(event):
        try:
            contatos_formatados = [c.strip() for c in contatos.split(",") if c.strip()]
            entrada = datetime.now().strftime("%d/%m/%Y %H:%M")
            novo = Hospede(
                nome=nome,
                idade=int(idade),
                quarto=int(quarto),
                diaria=float(diaria),
                contatos=contatos_formatados,
                data_entrada=entrada,
                data_saida="",
                status=status
            )
            lista = ler_arquivo("dados/hotel_pequeno.txt")
            adicionar_hospede(lista, novo)
            salvar_arquivo(lista, "dados/hotel_pequeno.txt")
            set_mensagem("✅ Hóspede cadastrado com sucesso!")
            set_nome("")
            set_idade("")
            set_quarto("")
            set_diaria("")
            set_contatos("")
            set_status("reservado")
        except Exception as e:
            set_mensagem(f"❌ Erro: {str(e)}")

    return html.div(
        {"style": {"padding": "2rem", "color": "black"}},
        html.h2("➕ Adicionar Cliente"),
        html.input({"type": "text", "placeholder": "Nome", "value": nome, "on_change": lambda e: set_nome(e["target"]["value"])}),
        html.br(),
        html.input({"type": "number", "placeholder": "Idade", "value": idade, "on_change": lambda e: set_idade(e["target"]["value"])}),
        html.br(),
        html.input({"type": "number", "placeholder": "Quarto", "value": quarto, "on_change": lambda e: set_quarto(e["target"]["value"])}),
        html.br(),
        html.input({"type": "text", "placeholder": "Diária", "value": diaria, "on_change": lambda e: set_diaria(e["target"]["value"])}),
        html.br(),
        html.input({"type": "text", "placeholder": "Contatos (DDD+Número separados por vírgula)", "value": contatos, "on_change": lambda e: set_contatos(e["target"]["value"])}),
        html.br(),
        html.label("Status: "),
        html.select(
            {"value": status, "on_change": lambda e: set_status(e["target"]["value"])},
            html.option({"value": "reservado"}, "Reservado"),
            html.option({"value": "hospedado"}, "Hospedado"),
            html.option({"value": "livre"}, "Livre"),
            html.option({"value": "offline"}, "Offline")
        ),
        html.br(),
        html.button({"on_click": registrar, "style": {"marginTop": "10px"}}, "Salvar Hóspede"),
        html.br(),
        html.p(mensagem),
        html.button({"on_click": lambda _: voltar()}, "🔙 Voltar")
    )

@component
def tela_remover(voltar):
    nome, set_nome = use_state("")
    mensagem, set_mensagem = use_state("")

    def remover(event):
        try:
            lista = ler_arquivo("dados/hotel_pequeno.txt")
            nova_lista = [h for h in lista if h.nome != nome]
            salvar_arquivo(nova_lista, "dados/hotel_pequeno.txt")
            set_mensagem("✅ Hóspede removido com sucesso!")
            set_nome("")
        except Exception as e:
            set_mensagem(f"❌ Erro: {str(e)}")

    return html.div(
        {"style": {"padding": "2rem", "color": "black"}},
        html.h2("❌ Remover Cliente"),
        html.input({"type": "text", "placeholder": "Nome do cliente", "value": nome, "on_change": lambda e: set_nome(e["target"]["value"])}),
        html.br(),
        html.button({"on_click": remover}, "Remover"),
        html.br(),
        html.p(mensagem),
        html.button({"on_click": lambda _: voltar()}, "🔙 Voltar")
    )

@component
def tela_editar(voltar):
    return html.div(
        {"style": {"padding": "2rem", "color": "black"}},
        html.h2("✏️ Editar Cliente"),
        html.p("(Funcionalidade em construção)"),
        html.button({"on_click": lambda _: voltar()}, "🔙 Voltar")
    )

@component
def tela_relatorio(voltar):
    try:
        lista = ler_arquivo("dados/hotel_pequeno.txt")
        itens = [
            html.li(f"{h.nome} | Quarto: {h.quarto} | Status: {h.status} | Entrada: {h.data_entrada}") for h in lista
        ]
    except Exception as e:
        itens = [html.li(f"Erro: {str(e)}")]

    return html.div(
        {"style": {"padding": "2rem", "color": "black"}},
        html.h2("📊 Relatório de Hóspedes"),
        html.ul(itens),
        html.button({"on_click": lambda _: voltar()}, "🔙 Voltar")
    )

@component
def tela_config(voltar):
    return html.div(
        {"style": {"padding": "2rem", "color": "black"}},
        html.h2("⚙️ Configurações"),
        html.p("(Configurações do sistema em construção...)"),
        html.button({"on_click": lambda _: voltar()}, "🔙 Voltar")
    )

@component
def tela_desligar(voltar):
    return html.div(
        {"style": {"padding": "2rem", "color": "black"}},
        html.h2("⛔ Sistema Desligado"),
        html.p("Encerrado com sucesso."),
        html.button({"on_click": lambda _: voltar()}, "🔙 Voltar ao Menu")
    )