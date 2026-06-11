pip install -r requirements.txt

import subprocess
import sys
import time

# ==========================================
# LISTA DE SCRIPTS
# ==========================================

SCRIPTS = [
    "src/gerar_dados.py",
    "src/analise_vendas.py",
    "src/dashboard.py",
    "src/previsao.py",
    "src/gerar_apresentacao.py"
]

# ==========================================
# EXECUTAR SCRIPT
# ==========================================

def executar(script):

    print("\n" + "=" * 60)
    print(f"Executando: {script}")
    print("=" * 60)

    subprocess.run(
        [sys.executable, script],
        check=True
    )

    print(f"✓ Finalizado: {script}")

# ==========================================
# MAIN
# ==========================================

def main():

    inicio = time.time()

    print("=" * 60)
    print("TRESSENZA BIG DATA ANALYTICS")
    print("=" * 60)

    for script in SCRIPTS:
        executar(script)

    fim = time.time()

    print("\n" + "=" * 60)
    print("PROJETO FINALIZADO")
    print("=" * 60)

    print(f"Tempo total: {fim - inicio:.2f} segundos")

    print("\nArquivos gerados:")

    print("- data/vendas.csv")
    print("- data/previsao.csv")
    print("- relatorio/relatorio_gerencial.xlsx")
    print("- relatorio/apresentacao_executiva.pptx")

    print("\nGráficos:")

    print("- graficos/faturamento_mensal.png")
    print("- graficos/categorias.png")
    print("- graficos/pagamentos.png")
    print("- graficos/satisfacao_clientes.png")
    print("- graficos/top_produtos.png")
    print("- graficos/faturamento_categoria.png")
    print("- graficos/previsao_5_anos.png")

    print("\n✓ Pipeline executada com sucesso!")

# ==========================================
# INÍCIO
# ==========================================

if __name__ == "__main__":
    main()
