import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# URL do site
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Pasta para salvar os PDFs
PASTA_DOWNLOAD = "anexos_ans"
os.makedirs(PASTA_DOWNLOAD, exist_ok=True)

# Nome do arquivo ZIP final
ZIP_FINAL = "anexos_ans.zip"

print("Acessando o site...")
response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Buscar links dos PDFs Anexo I e II
links_pdf = []

for link in soup.find_all("a", href=True):
    href = link["href"]
    texto = link.get_text(strip=True).lower()

    if "anexo i" in texto or "anexo ii" in texto:
        if href.endswith(".pdf"):
            if not href.startswith("http"):
                href = "https://www.gov.br" + href
            links_pdf.append(href)

if not links_pdf:
    raise Exception("Não foi possível localizar os Anexos I e II.")

print("Anexos encontrados:")
for link in links_pdf:
    print(link)

# Download dos PDFs
arquivos_baixados = []

for url_pdf in links_pdf:
    nome_arquivo = url_pdf.split("/")[-1]
    caminho_arquivo = os.path.join(PASTA_DOWNLOAD, nome_arquivo)

    print(f"Baixando {nome_arquivo}...")
    pdf_response = requests.get(url_pdf)
    pdf_response.raise_for_status()

    with open(caminho_arquivo, "wb") as f:
        f.write(pdf_response.content)

    arquivos_baixados.append(caminho_arquivo)

# Compactação em ZIP
print("Compactando arquivos...")
with ZipFile(ZIP_FINAL, "w") as zipf:
    for arquivo in arquivos_baixados:
        zipf.write(arquivo, arcname=os.path.basename(arquivo))

print("Processo finalizado com sucesso!")
print(f"Arquivo gerado: {ZIP_FINAL}")
