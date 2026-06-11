import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.linear_model import LinearRegression

# ==========================================
# CONFIGURAÇÕES
# ==========================================

ARQUIVO_VENDAS = "data/vendas.csv"

if not os.path.exists(ARQUIVO_VENDAS):
    print("Arquivo vendas.csv não encontrado.")
    print("Execute gerar_dados.py primeiro.")
    exit()

os.makedirs("data", exist_ok=True)
os.makedirs("graficos", exist_ok=True)

# ==========================================
# LEITURA DOS DADOS
# ==========================================

df = pd.read_csv(ARQUIVO_VENDAS)

df["data"] = pd.to_datetime(df["data"])

# ==========================================
# FATURAMENTO MENSAL
# ==========================================

df["ano_mes"] = df["data"].dt.to_period("M")

mensal = (
    df.groupby("ano_mes")["valor_total"]
    .sum()
    .reset_index()
)

mensal["ano_mes"] = mensal["ano_mes"].astype(str)

# ==========================================
# PREPARAÇÃO PARA ML
# ==========================================

mensal["indice"] = np.arange(len(mensal))

X = mensal[["indice"]]
y = mensal["valor_total"]

# ==========================================
# TREINAMENTO
# ==========================================

modelo = LinearRegression()
modelo.fit(X, y)

# ==========================================
# PREVISÃO 5 ANOS
# ==========================================

MESES_PREVISAO = 60

ultimo_indice = mensal["indice"].max()

indices_futuros = np.arange(
    ultimo_indice + 1,
    ultimo_indice + 1 + MESES_PREVISAO
)

previsoes = modelo.predict(
    indices_futuros.reshape(-1, 1)
)

# ==========================================
# DATAS FUTURAS
# ==========================================

ultima_data = pd.Period(
    mensal["ano_mes"].iloc[-1],
    freq="M"
)

datas_futuras = []

for i in range(1, MESES_PREVISAO + 1):
    datas_futuras.append(
        str(ultima_data + i)
    )

# ==========================================
# DATAFRAME FINAL
# ==========================================

df_previsao = pd.DataFrame({
    "mes": datas_futuras,
    "faturamento_previsto": previsoes
})

# ==========================================
# EXPORTAÇÃO CSV
# ==========================================

arquivo_saida = "data/previsao.csv"

df_previsao.to_csv(
    arquivo_saida,
    index=False,
    encoding="utf-8-sig"
)

# ==========================================
# GRÁFICO
# ==========================================

plt.figure(figsize=(14, 6))

plt.plot(
    mensal["ano_mes"],
    mensal["valor_total"],
    label="Histórico"
)

plt.plot(
    df_previsao["mes"],
    df_previsao["faturamento_previsto"],
    label="Previsão 5 anos"
)

plt.xticks(rotation=90)

plt.title(
    "Projeção de Crescimento da Empresa"
)

plt.xlabel("Período")
plt.ylabel("Faturamento (R$)")
plt.legend()

plt.tight_layout()

plt.savefig(
    "graficos/previsao_5_anos.png"
)

plt.close()

# ==========================================
# RESUMO
# ==========================================

print("=" * 60)
print("PREVISÃO CONCLUÍDA")
print("=" * 60)

print(
    f"Meses previstos: {MESES_PREVISAO}"
)

print(
    f"Arquivo gerado: {arquivo_saida}"
)

print(
    "Gráfico gerado:"
)

print(
    "graficos/previsao_5_anos.png"
)

print("=" * 60)

print("\nPrimeiras previsões:")

print(df_previsao.head())
