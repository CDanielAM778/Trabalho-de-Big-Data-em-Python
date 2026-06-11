import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# CONFIGURAÇÃO
# ==========================================

ARQUIVO_VENDAS = "data/vendas.csv"

if not os.path.exists(ARQUIVO_VENDAS):
    print("Arquivo vendas.csv não encontrado.")
    print("Execute gerar_dados.py primeiro.")
    exit()

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

faturamento_mensal = (
    df.groupby("ano_mes")["valor_total"]
    .sum()
)

plt.figure(figsize=(12, 6))
faturamento_mensal.plot()
plt.title("Faturamento Mensal")
plt.xlabel("Mês")
plt.ylabel("Faturamento (R$)")
plt.grid(True)

plt.tight_layout()
plt.savefig("graficos/faturamento_mensal.png")
plt.close()

# ==========================================
# CATEGORIAS MAIS VENDIDAS
# ==========================================

categorias = (
    df.groupby("categoria")["quantidade"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
categorias.plot(kind="bar")

plt.title("Categorias Mais Vendidas")
plt.xlabel("Categoria")
plt.ylabel("Quantidade")

plt.tight_layout()
plt.savefig("graficos/categorias.png")
plt.close()

# ==========================================
# FORMAS DE PAGAMENTO
# ==========================================

pagamentos = (
    df["forma_pagamento"]
    .value_counts()
)

plt.figure(figsize=(8, 8))

plt.pie(
    pagamentos,
    labels=pagamentos.index,
    autopct="%1.1f%%"
)

plt.title("Formas de Pagamento")

plt.tight_layout()
plt.savefig("graficos/pagamentos.png")
plt.close()

# ==========================================
# SATISFAÇÃO DOS CLIENTES
# ==========================================

avaliacoes = (
    df["avaliacao"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(8, 5))

avaliacoes.plot(kind="bar")

plt.title("Distribuição das Avaliações")
plt.xlabel("Nota")
plt.ylabel("Quantidade")

plt.tight_layout()
plt.savefig("graficos/satisfacao_clientes.png")
plt.close()

# ==========================================
# TOP 10 PRODUTOS
# ==========================================

top_produtos = (
    df.groupby("produto")["quantidade"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

top_produtos.plot(kind="bar")

plt.title("Top 10 Produtos Mais Vendidos")
plt.xlabel("Produto")
plt.ylabel("Quantidade")

plt.tight_layout()
plt.savefig("graficos/top_produtos.png")
plt.close()

# ==========================================
# FATURAMENTO POR CATEGORIA
# ==========================================

fat_categoria = (
    df.groupby("categoria")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

fat_categoria.plot(kind="bar")

plt.title("Faturamento por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Faturamento (R$)")

plt.tight_layout()
plt.savefig("graficos/faturamento_categoria.png")
plt.close()

# ==========================================
# RESUMO
# ==========================================

print("=" * 60)
print("DASHBOARD GERADO COM SUCESSO")
print("=" * 60)

print("Arquivos criados:")

arquivos = [
    "graficos/faturamento_mensal.png",
    "graficos/categorias.png",
    "graficos/pagamentos.png",
    "graficos/satisfacao_clientes.png",
    "graficos/top_produtos.png",
    "graficos/faturamento_categoria.png"
]

for arquivo in arquivos:
    print(f"✔ {arquivo}")

print("=" * 60)
