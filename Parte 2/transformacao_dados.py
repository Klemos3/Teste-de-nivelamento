import pdfplumber
import pandas as pd
from zipfile import ZipFile
import os

PDF_ANEXO_I = "Anexo_I.pdf"
CSV_FINAL = "rol_procedimentos.csv"
ZIP_FINAL = "Teste_Kim_Bazilio.zip"

if not os.path.exists(PDF_ANEXO_I):
    raise FileNotFoundError(f"Arquivo {PDF_ANEXO_I} não encontrado.")

print("Extraindo tabelas do PDF...")

linhas = []

with pdfplumber.open(PDF_ANEXO_I) as pdf:
    for pagina in pdf.pages:
        tabelas = pagina.extract_tables()
        for tabela in tabelas:
            for linha in tabela:
                if linha and any(c is not None and c.strip() != "" for c in linha):
                    linhas.append(linha)

df = pd.DataFrame(linhas)

# Remove linhas totalmente vazias
df.dropna(how="all", inplace=True)

# Remove cabeçalhos duplicados
df = df[df.iloc[:, 0] != df.iloc[0, 0]]

# Define cabeçalho
df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)

# Substituição apenas na coluna correta
if "Segmento Assistencial" in df.columns:
    df["Segmento Assistencial"] = df["Segmento Assistencial"].replace({
        "OD": "Odontológico",
        "AMB": "Ambulatorial"
    })

# Salva CSV
df.to_csv(CSV_FINAL, index=False, encoding="utf-8-sig")

# Compacta ZIP
with ZipFile(ZIP_FINAL, "w") as zipf:
    zipf.write(CSV_FINAL)

print("Processo finalizado com sucesso!")
