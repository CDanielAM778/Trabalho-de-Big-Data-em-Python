import pandas as pd
import numpy as np
from faker import Faker
import random

# Configuração
fake = Faker('pt_BR')
np.random.seed(42)
random.seed(42)

# Quantidade de vendas
NUM_VENDAS = 50000

# Produtos e categorias
produtos = {
    "Perfume Essence": ("Perfumes", 199.90),
    "Perfume Luxury": ("Perfumes", 299.90),
    "Base Matte Pro": ("Maquiagem", 89.90),
    "Batom Velvet": ("Maquiagem", 39.90),
    "Creme Facial Premium": ("Cuidados com a Pele", 129.90),
    "Sérum Vitamina C": ("Cuidados com a Pele", 149.90),
    "Shampoo Nutritivo": ("Cabelos", 49.90),
    "Máscara Capilar": ("Cabelos", 69.90),
    "Kit Presente Gold": ("Kits", 249.90),
    "Kit Presente Silver": ("Kits", 149.90)
}

formas_pagamento = [
    "Pix",
    "Cartão de Crédito",
    "Cartão de Débito",
    "Boleto"
]

cidades = [
    "Rio de Janeiro",
    "São Paulo",
    "Belo Horizonte",
    "Curitiba",
    "Salvador",
    "Brasília",
    "Recife"
]

dados = []

for i in range(NUM_VENDAS):

    produto = random.choice(list(produtos.keys()))

    categoria = produtos[produto][0]
    preco = produtos[produto][1]

    quantidade = random.randint(1, 5)

    desconto = round(random.uniform(0, 0.15), 2)

    valor_total = round(
        (preco * quantidade) * (1 - desconto),
        2
    )

    data_venda = fake.date_between(
        start_date='-2y',
        end_date='today'
    )

    avaliacao = random.randint(3, 5)

    dados.append([
        i + 1,
        data_venda,
        fake.name(),
        cidade := random.choice(cidades),
        produto,
        categoria,
        quantidade,
        preco,
        desconto,
        valor_total,
        random.choice(formas_pagamento),
        avaliacao
    ])

colunas = [
    "id_venda",
    "data",
    "cliente",
    "cidade",
    "produto",
    "categoria",
    "quantidade",
    "preco_unitario",
    "desconto",
    "valor_total",
    "forma_pagamento",
    "avaliacao"
]

df = pd.DataFrame(dados, columns=colunas)

df.to_csv(
    "vendas.csv",
    index=False,
    encoding="utf-8-sig"
)

print("=" * 50)
print("DATASET GERADO COM SUCESSO")
print(f"Total de vendas: {len(df)}")
print("Arquivo salvo: vendas.csv")
print("=" * 50)

print("\nAmostra dos dados:")
print(df.head())
