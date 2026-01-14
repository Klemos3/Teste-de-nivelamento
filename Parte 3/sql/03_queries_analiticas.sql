-- 10 operadoras com maiores despesas no último trimestre
SELECT o.nome_operadora,
       SUM(d.desp_eventos_medico_hospitalar) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.cnpj_operadora = o.cnpj
WHERE d.ano = EXTRACT(YEAR FROM CURRENT_DATE)
  AND d.trimestre = 
GROUP BY o.nome_operadora
ORDER BY total_despesas DESC
LIMIT 10;

-- 10 operadoras com maiores despesas no último ano
SELECT o.nome_operadora,
       SUM(d.desp_eventos_medico_hospitalar) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.cnpj_operadora = o.cnpj
WHERE d.ano = EXTRACT(YEAR FROM CURRENT_DATE) - 1
GROUP BY o.nome_operadora
ORDER BY total_despesas DESC
LIMIT 10;
