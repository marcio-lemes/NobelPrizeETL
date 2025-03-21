# ETL de Dados do Prêmio Nobel

Este projeto Python conecta-se a um banco de dados MongoDB e faz requisições HTTP à API do Nobel Prize para importar dados sobre prêmios e laureados. Os dados são armazenados em coleções do MongoDB e contados ao final do script.

## Como funciona
O código realiza os seguintes passos:
1. **Conexão com o MongoDB:** Estabelece uma conexão com o servidor local do MongoDB na porta padrão.
2. **Requisição e Importação de Dados:** Faz requisições à API do Nobel Prize para coletar dados JSON sobre prêmios e laureados e insere esses dados nas coleções `prizes` e `laureates`.
3. **Contagem de Documentos:** Conta o número de documentos em cada coleção e exibe os totais no terminal.

## Como Executar
Para executar o projeto, certifique-se de que as dependências estão instaladas e o MongoDB está em execução localmente.

1. **Clone o repositório (se aplicável):**
   ```bash
   git clone <URL_DO_REPOSITORIO>
2. **Instale as dependências:**
   ```bash
   pip install requests pymongo
3. **Execute o script:**
   ```bash
   python nome_do_script.py

## Habilidades e Frameworks Usados

- Python: Manipulação de APIs, processamento JSON e integração com MongoDB.
- Requests: Biblioteca utilizada para realizar requisições HTTP.
- Pymongo: Cliente MongoDB para conexão e manipulação do banco de dados.
- MongoDB: Banco de dados NoSQL onde os dados JSON são armazenados.