-- Operadoras
LOAD DATA LOCAL INFILE 'C:/Teste de nivelamento/Parte 3/csv/operadoras.csv'
INTO TABLE operadoras
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(cnpj, nome_operadora, modalidade, segmento, status);

-- Demonstracoes contabeis
LOAD DATA LOCAL INFILE 'C:/Teste de nivelamento/Parte 3/csv/demonstracoes_contabeis.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(cnpj_operadora, trimestre, ano, desp_eventos_medico_hospitalar, desp_outros);

-- Operadoras
\copy operadoras(cnpj, nome_operadora, modalidade, segmento, status)
FROM 'C:/Teste de nivelamento/Parte 3/csv/operadoras.csv' DELIMITER ';' CSV HEADER;

-- Demonstracoes contabeis
\copy demonstracoes_contabeis(cnpj_operadora, trimestre, ano, desp_eventos_medico_hospitalar, desp_outros)
FROM 'C:/Teste de nivelamento/Parte 3/csv/demonstracoes_contabeis.csv' DELIMITER ';' CSV HEADER;