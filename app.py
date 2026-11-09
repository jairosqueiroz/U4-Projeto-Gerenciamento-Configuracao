"""Registro de solicitações: exemplo didático para a Unidade 4."""
import argparse
import json
from pathlib import Path

def registrar_solicitacao(descricao, caminho):
    descricao = descricao.strip()
    if not descricao:
        raise ValueError("A descrição não pode estar vazia.")
    arquivo = Path(caminho)
    registros = json.loads(arquivo.read_text(encoding="utf-8")) if arquivo.exists() else []
    registro = {"id": len(registros) + 1, "descricao": descricao, "status": "aberta"}
    registros.append(registro)
    arquivo.write_text(json.dumps(registros, ensure_ascii=False, indent=2), encoding="utf-8")
    return registro

def main():
    parser = argparse.ArgumentParser(description="Registro de solicitações — U4")
    parser.add_argument("descricao", help="Descrição da solicitação")
    parser.add_argument("--arquivo", default="solicitacoes.json")
    args = parser.parse_args()
    print(json.dumps(registrar_solicitacao(args.descricao, args.arquivo), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
