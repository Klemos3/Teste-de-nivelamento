from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def carregar_dados():
    try:
        df = pd.read_csv('Relatorio_cadop.csv', sep=';', encoding='utf-8')
        df.columns = df.columns.str.strip()
        df = df.fillna("")
        print("✅ Base de dados carregada com acentuação correta!")
        return df
    except Exception as e:
        print(f"❌ Erro ao carregar CSV: {e}")
        return pd.DataFrame()

df_dados = carregar_dados()

@app.get("/buscar")
async def buscar(termo: str = Query(..., min_length=1)):
    if df_dados.empty:
        return {"erro": "Base de dados vazia"}
    
    # Busca na Razao Social ou Registro
    mask = (
        df_dados['Razao_Social'].str.contains(termo, case=False, na=False) |
        df_dados['REGISTRO_OPERADORA'].astype(str).str.contains(termo, case=False, na=False)
    )
    
    resultado = df_dados[mask].head(20)
    return resultado.to_dict(orient='records')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)