import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

def definir_url():
    return 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

def obter_html(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def download(site):
    arquivos_baixados = []
    texto = site.find('div', attrs={'class': 'cover-richtext-tile tile-content'})
    pdfs = texto.find_all('a', attrs={'class': 'internal-link'})
    pasta_teste1 = os.path.dirname(os.path.abspath(__file__))

    for pdf in pdfs:
        pdf_url = pdf.attrs['href']
        pdf_name = pdf.text.strip().replace('.', '')
        formato = '.pdf'

        if 'Anexo' in pdf_name and pdf_url.endswith(formato):
            print("Fazendo download de " + pdf_name)
            pdf_response = requests.get(pdf_url)
            nome_arquivo = pdf_name + formato

            caminho_arquivo = os.path.join(pasta_teste1, nome_arquivo)

            with open(caminho_arquivo, 'wb') as novo_arquivo:
                novo_arquivo.write(pdf_response.content)
                print("Download concluido: " + nome_arquivo)
            arquivos_baixados.append(caminho_arquivo)

    return arquivos_baixados

def compactar_pdfs(arquivos_baixados):
    if arquivos_baixados:
        pasta_teste1 = os.path.dirname(os.path.abspath(__file__))
        with ZipFile(os.path.join(pasta_teste1, "Arquivo_Compactado.zip"), "w") as zip:
            for arquivo in arquivos_baixados:
                zip.write(arquivo)
        print("Compactação realizada com sucesso")
    else:
        print("Nenhum arquivo encontrado para compactar")


try:
    url = definir_url()
    site = obter_html(url)
    arquivos_baixados = download(site)
    compactar_pdfs(arquivos_baixados)
except Exception as error:
    print("Erro ao fazer scraping: ", error)
