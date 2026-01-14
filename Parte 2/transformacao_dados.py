import pdfplumber
import pandas as pd
from zipfile import ZipFile

PDF_ANEXO_I = "Anexo_I.pdf"
CSV_FINAL = "rol_procedimentos.csv"
ZIP_FINAL = "Teste_Kim_Bazilio.zip"

print("Extraindo tabelas do PDF...")

todas_linhas = []

with pdfplumber.open(PDF_ANEXO_I) as pdf:
    for pagina in pdf.pages:
        tabelas = pagina.extract_tables()
        for tabela in tabelas:
            for linha in tabela:
                if linha and any(linha):
                    todas_linhas.append(linha)

# Cria DataFrame
df = pd.DataFrame(todas_linhas)

# Remove linhas vazias
df.dropna(how="all", inplace=True)

# Usa a primeira linha como cabeçalho
df.columns = df.iloc[0]
df = df[1:]

# Substituição OD e AMB
df.replace({
    "OD": "Odontológico",
    "AMB": "Ambulatorial"
}, inplace=True)

# Salva CSV
df.to_csv(CSV_FINAL, index=False, encoding="utf-8-sig")

# Compacta ZIP
with ZipFile(ZIP_FINAL, "w") as zipf:
    zipf.write(CSV_FINAL)

print("Processo finalizado com sucesso!")
