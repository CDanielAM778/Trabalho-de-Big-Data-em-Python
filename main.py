import subprocess
import sys
import time
import os

# ==========================================
# CONFIGURAÇÕES
# ==========================================

SCRIPTS = [
    "src/gerar_dados.py",
    "src/analise_vendas.py",
    "src/dashboard.py",
    "src/previsao.py",
    "src/gerar_apresentacao.py"
]

# ==========================================
# FUNÇÃO PARA EXECUTAR SCRIPTS
# ==========================================

def executar_script(script):
    print("\n" + "=" * 70)
    print(f"EXECUTANDO: {script}")
    print("=" * 70)

    if not os.path.exists(script):
        print(f"ERRO: Arquivo não encontrado -> {script}")
        return False

    try:
        resultado = subprocess.run(
            [sys.executable, script],
            check=True
        )

        print(f"✓ Concluído: {script}")
        return True

    except subprocess.CalledProcessError as erro:
        print(f"✗ Falha ao executar {script}")
        print(f"Código de saída: {erro.returncode}")
        return False

    except Exception as erro:
        print(f"✗ Erro inesperado em {script}")
        print(str(erro))
        return False

# ==========================================
# EXECUÇÃO PRINCIPAL
# ==========================================

def main():

    inicio = time.time()

    print("=" * 70)
    print("TRESSENZA BIG DATA ANALYTICS")
    print("=" * 70)
    print("Iniciando pipeline...\n")

    sucessos = 0

    for script in SCRIPTS:

        executado = executar_script(script)

        if executado:
            sucessos += 1
        else:
            print("\nPipeline interrompida.")
            sys.exit(1)

    fim = time.time()

    print("\n" + "=" * 70)
    print("PIPELINE FINALIZADA COM SUCESSO")
    print("=" * 70)

    print(f"Scripts executados: {sucessos}/{len(SCRIPTS)}")
    print(f"Tempo total: {fim - inicio:.2f} segundos")

    print("\nArquivos gerados:")

    arquivos = [
        "data/vendas.csv",
        "data/previsao.csv",
        "relatorio/relatorio_gerencial.xlsx",
        "relatorio/apresentacao_executiva.pptx",
        "graficos/faturamento_mensal.png",
        "graficos/categorias.png",
        "graficos/pagamentos.png",
        "graficos/satisfacao_clientes.png",
        "graficos/top_produtos.png",
        "graficos/faturamento_categoria.png",
        "graficos/previsao_5_anos.png"
    ]

    for arquivo in arquivos:

        if os.path.exists(arquivo):
            print(f"✓ {arquivo}")
        else:
            print(f"⚠ Não encontrado: {arquivo}")

    print("\nProjeto concluído com sucesso.")
    print("=" * 70)

# ==========================================
# INÍCIO
# ==========================================

if __name__ == "__main__":
    main()
