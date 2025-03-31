-- Script para criar o banco de dados
CREATE DATABASE IF NOT EXISTS testeBancoDeDados;

-- Script para criar a tabela operadoras para os dados do arquivo Relatorio_cadop.csv
CREATE TABLE operadoras (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(18),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(9),
    ddd VARCHAR(3),
    telefone VARCHAR(20),
    fax VARCHAR(15),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
  	regiao_de_comercializacao VARCHAR(10),
    data_registro_ans DATE
);

-- Script para importar os dados do arquivo Relatorio_cadop.csv para a tabela operadoras
\copy operadoras(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico,  representante, cargo_representante, regiao_de_comercializacao, data_registro_ans)
FROM 'C:\Users\Vinicius\Downloads\Relatorio_cadop.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8';

-- Script para criar a tabela demonstracoes_contabeis para os dados dos arquivos dos ultimos 2 anos do repositorio
CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans VARCHAR(20) NOT NULL,
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    vl_saldo_inicial TEXT, -- Colunas vl_saldo_inicial e vl_saldo_final como TEXT para evitar problemas na importação dos dados por conta da formatação dos numeros estar com virgula
    vl_saldo_final TEXT,
);

-- Script para importar os dados dos arquivos dos ultimos 2 anos do repositorio para a tabela demonstracoes_contabeis
\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\Vinicius\Downloads\1T2023\1T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\Vinicius\Downloads\2T2023\2T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\Vinicius\Downloads\3T2023\3T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\Vinicius\Downloads\4T2023\4T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\Vinicius\Downloads\1T2024\1T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\Vinicius\Downloads\2T2024\2T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\Vinicius\Downloads\3T2024\3T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\Vinicius\Downloads\4T2024\4T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8';

-- Script para alterar o tipo dos dados da coluna vl_saldo_inicial e vl_saldo_final criado anteriormente como TEXT.
-- E faz a conversão dos dados de TEXT para NUMERIC(15,2) e substitui a vírgula por ponto. Para melhor manipulação dos dados em cálculos.
ALTER TABLE demonstracoes_contabeis 
ALTER COLUMN vl_saldo_final 
TYPE NUMERIC(15,2) 
USING REPLACE(vl_saldo_final, ',', '.')::NUMERIC(15,2);

-- Script para fazer a primeira consulta filtrando as 10 operadoras com maiores despesas em 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR' no último trimestre
SELECT 
    op.razao_social, dc.data, dc.descricao,
    SUM(vl_saldo_final - vl_saldo_inicial) AS despesa_total -- Armazena o resultado da despesa total em uma nova coluna
FROM 
    demonstracoes_contabeis dc
JOIN
    -- Fazendo o join entre as tabelas demonstracoes_contabeis e operadoras para pegar o nome da operadora
    operadoras op ON dc.reg_ans = op.registro_ans
WHERE 
    descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND data BETWEEN
        --Pega o inicio do trimestre atual e subtrai 3 meses para garantir que pegue o ultimo trimestre
        DATE_TRUNC('quarter', CURRENT_DATE - INTERVAL '3 months') 
        AND
        --Pega o inicio do trimestre atual e subtrai 1 dia para garantir que pegue o ultimo dia do trimestre
        DATE_TRUNC('quarter', CURRENT_DATE) - INTERVAL '1 day'
GROUP BY
    op.registro_ans, dc.data, dc.descricao
ORDER BY
    despesa_total DESC
LIMIT 10;

-- Script para fazer a segunda consulta filtrando as 10 operadoras com maiores despesas nessa categoria no último ano
SELECT 
    op.razao_social, dc.descricao, 
    SUM(vl_saldo_final - vl_saldo_inicial) AS despesa_total
FROM 
    demonstracoes_contabeis dc
JOIN
    -- Fazendo o join entre as tabelas demonstracoes_contabeis e operadoras para pegar o nome da operadora
    operadoras op ON dc.reg_ans = op.registro_ans
WHERE 
    dc.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND dc.data BETWEEN
        --Pega o inicio do ano atual e subtrai 1 ano para garantir que pegue o ultimo ano
        DATE_TRUNC('year', CURRENT_DATE - INTERVAL '1 year') 
        AND
        --Pega o inicio do ano atual e subtrai 1 dia para garantir que pegue o ultimo dia do ano
        DATE_TRUNC('year', CURRENT_DATE) - INTERVAL '1 day'
GROUP BY 
    op.registro_ans, dc.descricao
ORDER BY 
    despesa_total DESC
LIMIT 10;