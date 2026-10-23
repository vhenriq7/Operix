# Operix

ERP operacional e financeiro multi-filial em desenvolvimento.

O Operix integra os processos de cadastros, vendas, pedidos, estoque, contas de clientes, caixa, cobrança, logística e gestão financeira de uma organização com filiais. O produto é desenvolvido inicialmente como demonstração funcional com dados sintéticos, visando avaliação empresarial e eventual evolução para produção.

**Status:** desenvolvimento inicial. Não homologado, não implantado e não indicado para uso com dados reais. O repositório permanece público nesta etapa.

## Documentação

- [Projeto — requisitos, arquitetura e entregas](docs/PROJECT.md).
- [AGENTS.md](AGENTS.md) — diretrizes para agentes de IA.

## Implementação atual

API com Python, FastAPI e Pydantic; PostgreSQL, SQLAlchemy, psycopg e Alembic para persistência de organizações e filiais. Os endpoints de clientes ainda armazenam dados apenas em memória. Autenticação, permissões e isolamento de dados ainda não estão implementados.

## Executar localmente

Com Python e PostgreSQL configurados, defina `DATABASE_URL` por variável de ambiente, sem versionar credenciais:

```bash
python -m pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

API: `http://127.0.0.1:8000`; OpenAPI: `http://127.0.0.1:8000/docs`. A configuração, o banco e o ambiente são de responsabilidade de quem executa a instância local.
