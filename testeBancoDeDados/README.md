# Teste de Banco de Dados
Este script SQL tem como objetivo a criação e manipulação de um banco de dados para armazenar e analisar dados de operadoras de planos de saúde. Os dados são extraídos de arquivos CSV e inseridos em tabelas estruturadas para permitir consultas específicas sobre despesas das operadoras.

## Estrutura do Banco de Dados
O banco de dados criado se chama `testeBancoDeDados` e contém duas tabelas principais:

### 1. Tabela `operadoras`
Armazena informações das operadoras de planos de saúde contidas no arquivo `Relatorio_cadop.csv`. Os principais campos incluem:
- Registro ANS
- CNPJ
- Razão Social
- Nome Fantasia
- Endereço e Contato
- Região de Comercialização
- Data de Registro

### 2. Tabela `demonstracoes_contabeis`
Armazena informações financeiras das operadoras, extraídas dos arquivos de demonstrações contábeis trimestrais dos últimos dois anos.
Os principais campos incluem:
- Data do registro
- Registro ANS da operadora
- Código da conta contábil
- Descrição da conta
- Valores de saldo inicial e final (criados como `TEXT` e depois convertidos para `NUMERIC(15,2)` para cálculos precisos)

## Importação de Dados
Os dados são importados via comando `\copy`, sendo extraídos de arquivos CSV delimitados por `;`, com cabeçalhos e codificação UTF-8.
Os arquivos de demonstrações contábeis são carregados de maneira iterativa para garantir que os últimos dois anos de dados estejam disponíveis no banco.

## Consultas Realizadas
O script inclui duas consultas SQL para análise financeira das operadoras:

### 1. Top 10 Operadoras com Maiores Despesas no Último Trimestre
Filtra as 10 operadoras com os maiores gastos na categoria "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE MÉDICO HOSPITALAR" no último trimestre. A data de análise é dinâmica e sempre considera o trimestre anterior ao atual.

### 2. Top 10 Operadoras com Maiores Despesas no Último Ano
Filtra as 10 operadoras com os maiores gastos na mesma categoria ao longo do último ano. Assim como na primeira consulta, a data de análise é dinâmica e sempre considera o ano anterior ao atual.

## Observações
- O script inclui uma conversão dos valores de saldo inicial e final para o tipo `NUMERIC(15,2)`, garantindo cálculos precisos.
- Os filtros de data utilizam `DATE_TRUNC` para garantir que os períodos analisados sejam exatos.

## Como Executar
1. Execute o script em um banco de dados PostgreSQL.
2. Certifique-se de que os arquivos CSV estão no caminho correto conforme especificado no script.
3. Após a importação dos dados, utilize as consultas SQL para análise das despesas das operadoras.