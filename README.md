# Tressenza Big Data Analytics

Projeto acadêmico desenvolvido para a disciplina de Tópicos de Big Data em Python.

O objetivo do projeto é demonstrar a operação de uma empresa de médio porte do setor de perfumaria e cosméticos, chamada Tressanza, com quem firmamos uma parceria, utilizando técnicas de análise de dados, Business Intelligence e Machine Learning para geração de insights estratégicos.

---

# Objetivos

- Analisar indicadores de desempenho
- Identificar produtos mais vendidos
- Avaliar satisfação dos clientes
- Gerar dashboards executivos
- Projetar crescimento para os próximos 5 anos

---

# Tecnologias Utilizadas

- Python 3
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- OpenPyXL
- Faker

---

# Estrutura do Projeto

```text
tressenza-bigdata/
│
├── data/
│   ├── vendas.csv
│   └── previsao.csv
│
├── src/
│   ├── gerar_dados.py
│   ├── analise_vendas.py
│   ├── dashboard.py
│   ├── previsao.py
│   └── main.py
│
├── graficos/
│
├── relatorio/
│
├── notebooks/
│
├── requirements.txt
│
└── README.md
```

---

# Funcionalidades

## Geração de Dados

O sistema gera automaticamente:

- 50.000 vendas imuladas
- Clientes
- Produtos de cosméticos
- Categorias
- Métodos de pagamento
- Avaliações de clientes

---

## Análise de Dados

Indicadores calculados:

- Faturamento total
- Ticket médio
- Volume de vendas
- Produtos mais vendidos
- Categorias mais vendidas
- Formas de pagamento
- Avaliação média

---

## Dashboard

Gráficos gerados automaticamente:

- Faturamento Mensal
- Categorias Mais Vendidas
- Formas de Pagamento
- Top Produtos
- Satisfação dos Clientes
- Faturamento por Categoria

---

## Machine Learning

O projeto utiliza Regressão Linear para prever:

- Crescimento da receita
- Tendência de vendas
- Projeção dos próximos 5 anos

---

# Como Executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python src/main.py
```

---

# Arquivos Gerados

## Dados

```text
data/vendas.csv
data/previsao.csv
```

## Relatório

```text
relatorio/relatorio_gerencial.xlsx
```

## Gráficos

```text
graficos/faturamento_mensal.png
graficos/categorias.png
graficos/pagamentos.png
graficos/satisfacao_clientes.png
graficos/top_produtos.png
graficos/faturamento_categoria.png
graficos/previsao_5_anos.png
```

---

# Desempenho

| Indicador | Valor Médio |
|------------|------------|
| Pedidos por dia | 95 |
| Pedidos por semana | 665 |
| Pedidos por mês | 2.850 |
| Ticket Médio | R$ 168 |
| Satisfação | 4.7/5 |
| NPS | 82 |

---

# Resultados Esperados

- Melhor entendimento do comportamento dos clientes
- Identificação dos produtos mais lucrativos
- Apoio à tomada de decisão
- Planejamento de crescimento
- Ambiente corporativo real

---


Projeto desenvolvido para fins acadêmicos na disciplina de Tópicos de Big Data em Python.
