from reactpy import component, use_state
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from frontend.telas import (
    menu_dashboard,
    tela_adicionar,
    tela_remover,
    tela_editar,
    tela_relatorio,
    tela_config,
    tela_desligar,
)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")  # Servindo imagem

@component
def App():
    tela_atual, set_tela_atual = use_state("menu")

    def ir_para_tela(nome):
        set_tela_atual(nome)

    def voltar():
        set_tela_atual("menu")

    if tela_atual == "adicionar":
        return tela_adicionar(voltar)
    elif tela_atual == "remover":
        return tela_remover(voltar)
    elif tela_atual == "editar":
        return tela_editar(voltar, "")
    elif tela_atual == "relatorio":
        return tela_relatorio(voltar, ir_para_tela)
    elif tela_atual.startswith("editar:"):
        # Formato editar:Nome do hospede
        nome_preset = tela_atual.split(":", 1)[1]
        return tela_editar(voltar, nome_preset)
    elif tela_atual == "config":
        return tela_config(voltar)
    elif tela_atual == "desligar":
        return tela_desligar(voltar)
    else:
        return menu_dashboard(ir_para_tela)

configure(app, App)
