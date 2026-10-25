# Operix

ERP modular para comércio físico: **Vendas, Estoque, CRM, Caixa, Financeiro, Fiscal, Contábil, Frota, Transportes, BI e Mobile**, contratados conforme a necessidade da empresa. Versões web e desktop previstas.

**Projeto em fase inicial de desenvolvimento**, com demonstração planejada usando dados sintéticos. Não está homologado nem pronto para uso com dados reais.

## Por onde começar

**Leia só [a visão do projeto](docs/PROJECT.md).** Ela explica o objetivo, a situação atual e a ordem de desenvolvimento.

Se precisar de mais detalhes:
- [Catálogo dos módulos comerciais](docs/MODULOS.md): o que cada módulo faz.
- [Regras levantadas](docs/specs/): especificações de referência para a IA.
- [Roadmap técnico](docs/ROADMAP.md), [arquitetura](docs/TECHNICAL.md) e [instruções para IA](AGENTS.md): consulta apenas quando necessário.

## Código existente

API Python/FastAPI; PostgreSQL, SQLAlchemy e Alembic em organizações/filiais. Clientes ainda são mantidos em memória; login, permissões e módulos comerciais completos **não estão prontos**.

Para execução local, configure o PostgreSQL e a variável `DATABASE_URL` sem versionar senhas:

```bash
python -m pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

Documentação da API local: `http://127.0.0.1:8000/docs`.
