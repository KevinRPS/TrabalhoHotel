# TrabalhoHotel
RELATÓRIO DO PROJETO DE SISTEMA DE HOSPEDAGEM

O projeto inicialmente consistia em desenvolver um sistema simples em Python que fosse capaz de gerar, armazenar, ler e manipular dados de hóspedes em um hotel. A proposta envolvia a utilização de arquivos .txt e operações básicas de CRUD: adicionar, remover, editar e listar dados.

Etapas Realizadas

1. Geração de Arquivos de Dados

O sistema já vem com um arquivo de dados .txt previamente gerado (por padrão, o hotel_pequeno.txt). No entanto, o professor pode optar por gerar um novo arquivo com quantidades variadas de hóspedes:

hotel_pequeno.txt

hotel_medio.txt

hotel_grande.txt

hotel_gigante.txt


Para gerar um novo arquivo, basta rodar o script de geração de dados:

python gerador_dados.py

Esse script permite que o professor escolha a quantidade de dados a serem gerados. Após isso, o sistema estará pronto para ser utilizado com base nos dados criados.


---

2. Execução Apenas com o Back-End

Para rodar o sistema sem interface gráfica (somente terminal), basta executar o seguinte comando:

python interacoes.py

Esse modo abre um menu no terminal onde o usuário pode:

Adicionar novo hóspede

Remover hóspede existente

Editar dados de um hóspede

Ver relatório dos hóspedes

Encerrar o sistema



---

3. Interface Front-End com ReactPy + FastAPI

Além do back-end, o projeto foi evoluído para conter uma interface gráfica acessada via navegador. Para isso, utilizamos:

FastAPI como servidor HTTP

ReactPy para renderização dos componentes front-end


Como Rodar:

1. Instale as dependências (se necessário):



pip install -r requirements.txt

2. Rode o projeto com:



uvicorn app:app --reload

3. Acesse o sistema no navegador:



http://localhost:8000

A interface traz um menu principal com as opções:

➕ Adicionar Cliente

❌ Remover Cliente

✏️ Editar Cliente

📊 Relatório

⚙️ Configurações

⛔ Desligar Sistema


Incluí também um plano de fundo temático de hotel/praia para tornar a interface mais atrativa visualmente.


---

Funcionalidades

Adição de hóspedes com validações (idade, diária, contatos)

Remoção de hóspedes por nome

Relatório completo com lista formatada de hóspedes

Sistema modular baseado em componentes front-end

Arquivo .txt atualizado automaticamente a cada operação

Interface limpa e funcional



---

Uso da Inteligência Artificial

Durante o processo, utilizei a inteligência artificial como ferramenta de apoio para:

Modelar o projeto inicial

Resolver erros de sintaxe e execução

Reorganizar o código em funções/componentes

Ajustar a navegação entre telas e eventos

Aplicar estilização no front-end

Criar o relatório final de documentação


Em vez de simplesmente copiar código, eu aprendi no processo, interpretei os erros, apliquei correções, e fui moldando um sistema robusto e funcional, muito além do que foi inicialmente proposto.


---

Considerações Finais

O projeto final está 100% funcional, permite executar tanto pelo terminal quanto com interface gráfica, e supera as expectativas da proposta inicial. Todo o código foi cuidadosamente ajustado e testado.

Estou à disposição para eventuais dúvidas e pronto para apresentar qualquer parte do sistema. Obrigado pela oportunidade.
