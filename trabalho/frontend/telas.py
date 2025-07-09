from reactpy import component, html, use_state
from LeituraDeDados import ler_arquivo
from funcoes import adicionar_hospede, salvar_arquivo
from modelos import Hospede
from datetime import datetime

# Estilos compartilhados
ESTILO_FUNDO = {
    "backgroundImage": "url('/static/praia.jpg')",
    "backgroundSize": "cover",
    "backgroundPosition": "center",
    "minHeight": "100vh",
    "display": "flex",
    "justifyContent": "center",
    "alignItems": "center",
    "padding": "2rem",
}

ESTILO_CAIXA = {
    "backgroundColor": "rgba(255, 255, 255, 0.85)",
    "padding": "2rem",
    "borderRadius": "10px",
    "maxWidth": "800px",
    "width": "100%",
}

# dentro de telas.py

@component
def menu_dashboard(ir_para_tela):
    estilo_fundo = {
        "backgroundImage": "url('/static/praia.jpg')",
        "backgroundSize": "cover",
        "backgroundPosition": "center",
        "minHeight": "100vh",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "padding": "2rem",
    }

    estilo_grid = {
        "display": "grid",
        "gridTemplateColumns": "1fr 1fr",
        "gap": "2rem",
        "maxWidth": "800px",
        "width": "100%",
    }

    estilo_botao = {
        "padding": "2rem",
        "fontSize": "1.5rem",
        "color": "white",
        "backgroundColor": "rgba(0, 0, 0, 0.4)",
        "border": "2px solid white",
        "borderRadius": "10px",
        "cursor": "pointer",
    }

    return html.div(
        {"style": estilo_fundo},
        html.div(
            {"style": estilo_grid},
            html.button({"on_click": lambda e: ir_para_tela("adicionar"), "style": estilo_botao}, "➕ Adicionar Cliente"),
            html.button({"on_click": lambda e: ir_para_tela("remover"), "style": estilo_botao}, "❌ Remover Cliente"),
            html.button({"on_click": lambda e: ir_para_tela("editar"), "style": estilo_botao}, "✏️ Editar Cliente"),
            html.button({"on_click": lambda e: ir_para_tela("relatorio"), "style": estilo_botao}, "📊 Relatório"),
            html.button({"on_click": lambda e: ir_para_tela("config"), "style": estilo_botao}, "⚙️ Configurações"),
            html.button({"on_click": lambda e: ir_para_tela("desligar"), "style": estilo_botao}, "⛔ Desligar Sistema"),
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
        {"style": ESTILO_FUNDO},
        html.div({"style": ESTILO_CAIXA},
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
        {"style": ESTILO_FUNDO},
        html.div({"style": ESTILO_CAIXA},
        html.h2("❌ Remover Cliente"),
        html.input({"type": "text", "placeholder": "Nome do cliente", "value": nome, "on_change": lambda e: set_nome(e["target"]["value"])}),
        html.br(),
        html.button({"on_click": remover}, "Remover"),
        html.br(),
        html.p(mensagem),
        html.button({"on_click": lambda _: voltar()}, "🔙 Voltar")
        )
    )

@component
def tela_editar(voltar, nome_preset=""):
    # Estados
    nome_busca, set_nome_busca = use_state(nome_preset)
    indice_encontrado, set_indice_encontrado = use_state(None)  # índice na lista para salvar depois
    idade, set_idade = use_state("")
    quarto, set_quarto = use_state("")
    diaria, set_diaria = use_state("")
    contatos, set_contatos = use_state("")
    status, set_status = use_state("")
    mensagem, set_mensagem = use_state("")

    def buscar(event):
        lista = ler_arquivo("dados/hotel_pequeno.txt")
        for idx, h in enumerate(lista):
            if nome_busca.lower() in h.nome.lower():
                set_indice_encontrado(idx)
                # Preenche campos
                set_idade(str(h.idade))
                set_quarto(str(h.quarto))
                set_diaria(str(h.diaria))
                set_contatos(",".join(h.contatos))
                set_status(h.status)
                set_mensagem("Hóspede encontrado! Faça alterações e clique em Salvar.")
                return
        set_mensagem("❌ Hóspede não encontrado.")

    def salvar(event):
        if indice_encontrado is None:
            set_mensagem("❌ Nenhum hóspede para salvar. Pesquise primeiro.")
            return
        try:
            lista = ler_arquivo("dados/hotel_pequeno.txt")
            h = lista[indice_encontrado]
            h.idade = int(idade) if idade else h.idade
            h.quarto = int(quarto) if quarto else h.quarto
            h.diaria = float(diaria) if diaria else h.diaria
            h.contatos = [c.strip() for c in contatos.split(",") if c.strip()]
            h.status = status if status else h.status
            salvar_arquivo(lista, "dados/hotel_pequeno.txt")
            set_mensagem("✅ Alterações salvas!")
        except Exception as e:
            set_mensagem(f"❌ Erro ao salvar: {str(e)}")

    return html.div(
        {"style": ESTILO_FUNDO},
        html.div({"style": ESTILO_CAIXA},
        html.h2("✏️ Editar Cliente"),
        html.input({"type": "text", "placeholder": "Nome para buscar", "value": nome_busca, "on_change": lambda e: set_nome_busca(e["target"]["value"])}),
        html.button({"on_click": buscar, "style": {"marginLeft": "0.5rem"}}, "🔍 Buscar"),
        html.br(),
        html.br(),
        html.label("Idade: "),
        html.input({"type": "number", "value": idade, "on_change": lambda e: set_idade(e["target"]["value"])}),
        html.br(),
        html.label("Quarto: "),
        html.input({"type": "number", "value": quarto, "on_change": lambda e: set_quarto(e["target"]["value"])}),
        html.br(),
        html.label("Diária: "),
        html.input({"type": "text", "value": diaria, "on_change": lambda e: set_diaria(e["target"]["value"])}),
        html.br(),
        html.label("Contatos (separados por vírgula): "),
        html.input({"type": "text", "value": contatos, "on_change": lambda e: set_contatos(e["target"]["value"])}),
        html.br(),
        html.label("Status: "),
        html.select({"value": status, "on_change": lambda e: set_status(e["target"]["value"])} ,
            html.option({"value": "Ativa"}, "Ativa"),
            html.option({"value": "Concluída"}, "Concluída"),
            html.option({"value": "Cancelada"}, "Cancelada"),
        ),
        html.br(),
        html.button({"on_click": salvar, "style": {"marginTop": "10px"}}, "💾 Salvar"),
        html.br(),
        html.p(mensagem),
        html.button({"on_click": lambda _: voltar()}, "🔙 Voltar")
        )
    )

@component
def tela_relatorio(voltar, ir_para_tela=None):
    # Estados para paginação e filtros de pesquisa
    pagina_atual, set_pagina_atual = use_state(0)  # página começa em 0
    filtro_nome, set_filtro_nome = use_state("")
    filtro_status, set_filtro_status = use_state("")  # reservado, hospedado, livre, offline
    filtro_checkin, set_filtro_checkin = use_state("")   # data_entrada (dd/mm/aaaa)
    filtro_checkout, set_filtro_checkout = use_state("")  # data_saida (dd/mm/aaaa)

    # Lê dados sempre que o componente renderiza
    try:
        lista = ler_arquivo("dados/hotel_pequeno.txt")
    except Exception as e:
        lista = []

    # Função auxiliar para aplicar filtros
    def corresponde_filtros(h):
        cond_nome = filtro_nome.lower() in h.nome.lower() if filtro_nome else True
        cond_status = (h.status.lower() == filtro_status.lower()) if filtro_status else True
        cond_checkin = filtro_checkin in h.data_entrada if filtro_checkin else True
        cond_checkout = filtro_checkout in h.data_saida if filtro_checkout else True
        return cond_nome and cond_status and cond_checkin and cond_checkout

    filtrados = [h for h in lista if corresponde_filtros(h)]

    # Lógica de relatório por nome completo
    if filtro_nome.strip():
        # Busca por nome exato (ignorando maiúsc/minúsc)
        pagina_itens = [h for h in lista if h.nome.lower() == filtro_nome.lower()]
    else:
        pagina_itens = []  # Nenhum resultado até informar o nome completo
    total_paginas = 1  # Paginação desativada

    def criar_item(h):
        # Cálculo de dias e total a pagar
        try:
            if h.data_saida:
                dt_entrada = datetime.strptime(h.data_entrada.split(" ")[0], "%d/%m/%Y")
                dt_saida = datetime.strptime(h.data_saida.split(" ")[0], "%d/%m/%Y")
                dias = (dt_saida - dt_entrada).days or 1
            else:
                dias = 0
        except Exception:
            dias = 0
        total_pagar = dias * h.diaria if dias else 0

        linhas = [
            "===== RELATÓRIO DO HÓSPEDE =====",
            f"Nome: {h.nome}",
            f"Idade: {h.idade}",
            f"Quarto: {h.quarto}",
            f"Diária: R$ {h.diaria:.2f}",
            f"Contatos: {', '.join(h.contatos)}" if h.contatos else "Contatos:",
            f"Data de entrada: {h.data_entrada}",
            f"Data de saída: {h.data_saida if h.data_saida else '-'}",
            f"Status: {h.status}",
            f"Total de dias: {dias}",
            f"💰 Total a pagar: R$ {total_pagar:.2f}",
            "===============================",
        ]
        bloco = "\n".join(linhas)

        if ir_para_tela:
            botao_editar = html.button({"on_click": lambda _, n=h.nome: ir_para_tela(f"editar:{n}")}, "✏️ Editar")
            return html.li({"style": {"whiteSpace": "pre-wrap", "marginBottom": "1rem"}}, html.pre(bloco), botao_editar)
        else:
            return html.li({"style": {"whiteSpace": "pre-wrap", "marginBottom": "1rem"}}, html.pre(bloco))

    lista_elementos = [criar_item(h) for h in pagina_itens] if pagina_itens else [html.li("Nenhum hóspede encontrado.")]

    # Handlers de alteração de filtro (resetam para página 0)
    def on_change_nome(e):
        set_filtro_nome(e["target"]["value"])
        set_pagina_atual(0)

    def on_change_status(e):
        set_filtro_status(e["target"]["value"])
        set_pagina_atual(0)

    def on_change_checkin(e):
        set_filtro_checkin(e["target"]["value"])
        set_pagina_atual(0)

    def on_change_checkout(e):
        set_filtro_checkout(e["target"]["value"])
        set_pagina_atual(0)

    return html.div(
        {"style": ESTILO_FUNDO},
        html.div({"style": ESTILO_CAIXA},
        html.h2("📊 Relatório de Hóspedes"),
        # Campos de busca
        html.div(
            {"style": {"marginBottom": "1rem"}},
            html.input({
                "type": "text",
                "placeholder": "Pesquisar por nome",
                "value": filtro_nome,
                "on_change": on_change_nome
            }),
            html.select({"value": filtro_status, "on_change": on_change_status, "style": {"marginLeft": "0.5rem"}},
                html.option({"value": ""}, "Todos Status"),
                html.option({"value": "reservado"}, "Reservado"),
                html.option({"value": "Ativa"}, "Ativa"),
                html.option({"value": "Concluída"}, "Concluída"),
                html.option({"value": "Cancelada"}, "Cancelada"),
            ),
            html.input({
                "type": "text",
                "placeholder": "Filtrar por check-in (dd/mm/aaaa)",
                "style": {"marginLeft": "0.5rem"},
                "value": filtro_checkin,
                "on_change": on_change_checkin
            }),
            html.input({
                "type": "text",
                "placeholder": "Filtrar por check-out (dd/mm/aaaa)",
                "style": {"marginLeft": "0.5rem"},
                "value": filtro_checkout,
                "on_change": on_change_checkout
            }),
        ),
        # Lista de resultado
        html.ul(lista_elementos),
        html.button({"on_click": lambda _: voltar()}, "🔙 Voltar")
        )
    )

@component
def tela_config(voltar):
    return html.div(
        {"style": ESTILO_FUNDO},
        html.div({"style": ESTILO_CAIXA},
        html.h2("⚙️ Configurações"),
        html.p("(Configurações do sistema em construção...)"),
        html.button({"on_click": lambda _: voltar()}, "🔙 Voltar")
        )
    )

@component
def tela_desligar(voltar):
    return html.div(
        {"style": ESTILO_FUNDO},
        html.div({"style": ESTILO_CAIXA},
        html.h2("⛔ Sistema Desligado"),
        html.p("Encerrado com sucesso."),
        html.button({"on_click": lambda _: voltar()}, "🔙 Voltar ao Menu")
        )
    )
