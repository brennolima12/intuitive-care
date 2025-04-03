--Usar MySQL para rodar os scripts abaixo
CREATE TABLE relatorio_cadop (
    id INT AUTO_INCREMENT PRIMARY KEY,
    egistro_ANS TEXT,
    CNPJ TEXT,
    Razao_Social TEXT,
    Nome_Fantasia TEXT,
    Modalidade TEXT,
    Logradouro TEXT,
    Numero TEXT,
    Complemento TEXT,
    Bairro TEXT,
    Cidade TEXT,
    UF TEXT,
    CEP TEXT,
    DDD TEXT,
    Telefone TEXT,
    Fax TEXT,
    Endereco_eletronico TEXT,
    Representante TEXT,
    Cargo_Representante TEXT,
    Regiao_de_Comercializacao TEXT,
    Data_Registro_ANS DATE
);


LOAD DATA LOCAL INFILE
'C:/Users/Usuario/Downloads/Relatorio_cadop.csv'
INTO TABLE relatorio_cadop
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro,
Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax,
Endereco_eletronico, Representante, Cargo_Representante,
Regiao_de_Comercializacao, Data_Registro_ANS);