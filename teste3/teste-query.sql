--Usar MySQL para rodar os scripts abaixo
SELECT relatorio_cadop.Razao_Social, demonstracoes_contabeis.VL_SALDO_FINAL, DATA
FROM relatorio_cadop, demonstracoes_contabeis
WHERE relatorio_cadop.Registro_ANS = demonstracoes_contabeis.REG_ANS
  AND demonstracoes_contabeis.DESCRICAO LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS%ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
  AND demonstracoes_contabeis.DATA = '2024-10-01'
ORDER BY VL_SALDO_FINAL DESC
LIMIT 10;

SELECT relatorio_cadop.Razao_Social,
SUM(demonstracoes_contabeis.VL_SALDO_FINAL) AS Total_Despesas
FROM relatorio_cadop, demonstracoes_contabeis
WHERE relatorio_cadop.Registro_ANS = demonstracoes_contabeis.REG_ANS
    AND demonstracoes_contabeis.DESCRICAO LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS%ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND YEAR(demonstracoes_contabeis.DATA) = 2024
GROUP BY
    relatorio_cadop.Razao_Social
ORDER BY
    Total_Despesas DESC
LIMIT 10;
