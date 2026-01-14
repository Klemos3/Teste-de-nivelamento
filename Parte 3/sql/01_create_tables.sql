-- Tabela de Operadoras
CREATE TABLE IF NOT EXISTS operadoras (
    cnpj VARCHAR(20) PRIMARY KEY,
    nome_operadora VARCHAR(255),
    modalidade VARCHAR(100),
    segmento VARCHAR(100),
    status VARCHAR(50)
);

-- Tabela de Demonstracoes Contabeis
CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    id SERIAL PRIMARY KEY, -- MySQL: AUTO_INCREMENT, Postgres: SERIAL
    cnpj_operadora VARCHAR(20),
    trimestre VARCHAR(10),
    ano INT,
    desp_eventos_medico_hospitalar DECIMAL(18,2),
    desp_outros DECIMAL(18,2),
    FOREIGN KEY (cnpj_operadora) REFERENCES operadoras(cnpj)
);
