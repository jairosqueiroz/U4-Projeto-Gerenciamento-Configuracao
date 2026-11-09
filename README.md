# U4 — Gerenciamento de Configuração de Software

**Disciplina:** Projeto de Software — Unidade 4: Projeto de Software Avançado  
**Autor:** Jairo da Silva Queiroz

## Finalidade do projeto
Organizar solicitações de uma equipe e demonstrar o controle de versões de código e documentação com Git e GitHub. O programa registra uma descrição, atribui um identificador e define o status inicial como `aberta`. Os registros ficam armazenados em um arquivo JSON local.

## Executar
Requisito: Python 3, sem bibliotecas externas.

```bash
git clone https://github.com/jairosqueiroz/U4-Projeto-Gerenciamento-Configuracao.git
cd U4-Projeto-Gerenciamento-Configuracao
python app.py "Revisar requisito de autenticação"
```

Saída esperada para um arquivo de dados novo:
```json
{"id": 1, "descricao": "Revisar requisito de autenticação", "status": "aberta"}
```

Execute novamente com outra descrição para acrescentar uma solicitação. O arquivo `solicitacoes.json` preserva os registros e não é versionado. Uma descrição vazia é rejeitada.

## Artefatos
| Arquivo | Finalidade |
| --- | --- |
| app.py | Registro e persistência das solicitações |
| README.md | Objetivo e instruções de execução |
| CHANGELOG.md | Resumo das alterações |
| .gitignore | Exclusão de dados locais e arquivos temporários |

## Gerenciamento de configuração
O histórico de commits permite identificar alterações de código e documentação. Cada commit possui autor, mensagem e identificador. A branch principal é `main`.

Fluxo para futuras alterações locais:
```bash
git status
git add app.py README.md CHANGELOG.md
git diff --cached
git commit -m "Descreve a alteração realizada"
git push origin main
git log --oneline -5
```

**Registro da execução:** a criação do repositório foi realizada pela interface do GitHub e os arquivos iniciais foram publicados pela integração autenticada. Os comandos acima constituem instruções para execução local; não comprovam, por si, clonagem ou push realizados no Git Bash.

## Escopo
Protótipo didático de linha de comando, sem autenticação, interface gráfica ou uso simultâneo por vários usuários.
