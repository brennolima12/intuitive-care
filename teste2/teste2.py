import os

import pandas as pd
from tabula import read_pdf
from zipfile import ZipFile

def ler_tabelas():
    pdf_path = "teste2/Anexo I.pdf"
    return read_pdf(pdf_path, pages="3-181", multiple_tables=True)

def organizar_dados(tabelas):
    print('Estruturando dados para o arquivo CSV')

    # Pega o cabeçalho da primeira tabela
    colunas = tabelas[0].columns
    tabelas_limpas = [tabelas[0]]

    # Força as colunas da primeira nas outras, se forem compatíveis
    for i, tabela in enumerate(tabelas[1:], start=2):
        if tabela.shape[1] == len(colunas):
            nova_tabela = tabela.copy()
            nova_tabela.columns = colunas
            tabelas_limpas.append(nova_tabela)
        else:
            print(f"⚠️ Tabela da página {i} ignorada (colunas incompatíveis: {tabela.shape[1]} vs {len(colunas)})")

    # Concatena tudo
    df = pd.concat(tabelas_limpas, ignore_index=True)

    # Limpeza
    df.dropna(how='all', inplace=True)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col] = df[col].fillna(0)
        else:
            df[col] = df[col].fillna("")

    # Substituições
    substituicoes = {
        "OD": "Seg. Odontológica",
        "AMB": "Seg. Ambulatorial"
    }
    df = df.replace(substituicoes)

    # Salva CSV
    df.to_csv("arquivo.csv", index=False)
    return "arquivo.csv"

def compactar_arquivo(arquivo_csv):
    if arquivo_csv:
        pasta_teste2 = os.path.dirname(os.path.abspath(__file__))
        with ZipFile(os.path.join(pasta_teste2, 'Teste_Brenno_Pinto_Lapa_Rego_Lima.zip'), 'w') as zip:
            zip.write(arquivo_csv)
        print("Compactação realizada com sucesso")
    else:
        print("Nenhum arquivo encontrado para compactar")


try:
    tabelas = ler_tabelas()
    csv_gerado = organizar_dados(tabelas)
    compactar_arquivo(csv_gerado)
except Exception as error:
    print(" Erro ao fazer transformação de dados:", error)
