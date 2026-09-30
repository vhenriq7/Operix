# Operix

> SaaS de gestão operacional para empresas com múltiplas filiais.

O **Operix** é um projeto de estudo e portfólio focado em back-end. O produto busca integrar vendas, clientes, conta comercial, estoque, transferências entre filiais, cargas e entregas, enquanto o desenvolvimento é usado para aprender Python, APIs, SQL, PostgreSQL e arquitetura de software na prática.

## Estado atual

**Fase 4 — SQLAlchemy e Alembic (em andamento).**

As fases de fundamentos de API e SQL foram concluídas. Já foram praticados:

- aplicação FastAPI executada com Uvicorn;
- endpoints `GET`, `POST`, `PATCH` e `DELETE`;
- path parameters;
- query parameters;
- request body;
- validação com Pydantic;
- status codes como `200`, `201`, `404` e `422`;
- Swagger/OpenAPI;
- armazenamento temporário de clientes em memória;
- PostgreSQL local com banco `operix`;
- SQL básico com tabelas, chaves primárias, chaves estrangeiras, restrições, `JOIN`, `GROUP BY`, transações e índices introdutórios;
- modelagem didática em português com `organizacoes`, `filiais` e `clientes`;
- dependências iniciais da Fase 4 instaladas: SQLAlchemy, Alembic e psycopg.
- configuração inicial de banco em `app/database.py` com `DATABASE_URL`, `engine`, `SessionLocal` e `get_db`.

A API ainda usa lista em memória para clientes. Isso foi intencional nas fases iniciais; o próximo bloco de aprendizagem é conectar a API ao PostgreSQL usando SQLAlchemy e Alembic.

O progresso detalhado e o próximo passo ficam em [docs/ROADMAP.md](docs/ROADMAP.md).

## Como navegar pelo projeto

| Arquivo | Responsabilidade |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Como Codex e outros agentes de IA devem trabalhar e ensinar neste repositório |
| [docs/SPEC.md](docs/SPEC.md) | Requisitos de negócio, regras do SaaS e limites de escopo |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Decisões técnicas, stack e princípios de arquitetura |
| [docs/ROADMAP.md](docs/ROADMAP.md) | Fases de desenvolvimento, aprendizagem, progresso e critérios de conclusão |
| `app/` | Código da aplicação |
| `requirements.txt` | Dependências Python atualmente instaladas |

## Estrutura

```text
Operix/
├── AGENTS.md
├── docs/
│   ├── SPEC.md
│   ├── ARCHITECTURE.md
│   └── ROADMAP.md
├── app/
│   ├── database.py
│   └── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

> O `AGENTS.md` fica na raiz de propósito: agentes como Codex procuram instruções `AGENTS.md` a partir da raiz do repositório e ao longo do caminho até o diretório de trabalho.

## Stack e ferramentas

Resumo atual/planejado:

| Tecnologia/ferramenta | Situação |
| --- | --- |
| Python | Atual |
| FastAPI | Atual |
| Pydantic | Atual |
| Uvicorn | Atual |
| Swagger/OpenAPI | Atual via FastAPI |
| PostgreSQL | Atual para estudo local |
| SQL | Atual para estudo manual via `psql` |
| SQLAlchemy | Instalado; integração com a API em andamento |
| Alembic | Instalado; migrações ainda serão configuradas |
| psycopg | Instalado como driver PostgreSQL |
| Git/GitHub | Atual |
| Pytest | Planejado |
| Docker | Planejado |

As decisões e o que já está efetivamente adotado estão em [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Executando localmente

Com o ambiente virtual ativo:

```powershell
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Para usar a configuração de banco da Fase 4, defina `DATABASE_URL` no terminal antes de importar `app.database` ou executar funcionalidades persistentes:

```powershell
$env:DATABASE_URL = "postgresql+psycopg://postgres:SUA_SENHA@localhost:5432/operix"
```

Não commite senhas reais no repositório.

A API fica disponível em:

```text
http://127.0.0.1:8000
```

Documentação interativa:

```text
http://127.0.0.1:8000/docs
```

## Objetivo de aprendizagem

O projeto segue uma regra simples:

> Primeiro entender. Depois implementar. Depois melhorar.

Assistentes de IA devem atuar em modo professor, com mudanças incrementais e sem inventar regras de negócio. As instruções completas estão em [AGENTS.md](AGENTS.md).

## Princípio de engenharia

> Primeiro simples, correto e compreensível. Depois testável, refatorado e otimizado.
