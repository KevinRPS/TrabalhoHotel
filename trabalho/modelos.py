class Hospede:
    def __init__(self, nome, idade, quarto, diaria, contatos, data_entrada, data_saida, status):
        self.nome = nome
        self.idade = int(idade)
        self.quarto = int(quarto)
        self.diaria = float(diaria)
        self.contatos = contatos
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.status = status

    def __str__(self):
        return f"{self.nome}, Quarto: {self.quarto}, Status: {self.status}"
