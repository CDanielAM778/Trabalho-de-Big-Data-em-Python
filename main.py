import subprocess
import sys
import time

# ==========================================
# FUNÇÃO EXECUTORA
# ==========================================

def executar(script):
    print("\n" + "=" * 70)
    print(f"EXECUTANDO: {script}")
    print("=" * 70)

    resultado = subprocess.run(
        [sys.executable, script]
    )

    if resultado.returncode != 0:
        print(f"\nERRO ao executar {script}")
        sys.exit(1)

    print(f"\n✓ {script} concluído com sucesso.")

# ==========================================
# PIPELINE
# ==========================================

inicio = time.time()

scripts = [
    "src/gerar_dados.py",
    "src/analise_vendas.py",
    "src/dashboard.py",
    "src/previsao.py"
]

print("=" * 70)
print("TRESSENZA BIG DATA ANALYTICS")
print("=" * 70)

for script in scripts:
    executar(script)

fim = time.time()

print("\n" + "=" * 70)
print("PIPELINE FINALIZADA")
print("=" * 70)

print(
    f"Tempo total: {(fim - inicio):.2f} segundos"
)

print("\nArquivos gerados:")

arquivos = [
    "data/vendas.csv",
    "data/previsao.csv",
    "relatorio/relatorio_gerencial.xlsx",
    "graficos/faturamento_mensal.png",
    "graficos/categorias.png",
    "graficos/pagamentos.png",
    "graficos/satisfacao_clientes.png",
    "graficos/top_produtos.png",
    "graficos/faturamento_categoria.png",
    "graficos/previsao_5_anos.png"
]

for arquivo in arquivos:
    print(f"✓ {arquivo}")

print("\nProjeto concluído com sucesso.")
print("=" * 70)
