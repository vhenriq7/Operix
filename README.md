# Operix

> SaaS de gestão operacional para empresas com múltiplas filiais.

O **Operix** é um projeto de estudo e portfólio focado em back-end. O produto busca integrar vendas, clientes, conta comercial, estoque, transferências entre filiais, cargas e entregas, enquanto o desenvolvimento é usado para aprender Python, APIs, SQL, PostgreSQL e arquitetura de software na prática.

## Estado atual

**Fase 3 — PostgreSQL e SQL (em andamento).**

A fase de fundamentos de API foi concluída. Já foram praticados no código:

- aplicação FastAPI executada com Uvicorn;
- endpoints `GET`, `POST`, `PATCH` e `DELETE`;
- path parameters;
- query parameters;
- request body;
- validação com Pydantic;
- status codes como `200`, `201`, `404` e `422`;
- Swagger/OpenAPI;
- armazenamento temporário de clientes em memória.

Os clientes em memória desaparecem quando a aplicação reinicia. Isso foi intencional na fase de API e agora prepara o próximo bloco de aprendizagem: persistência com PostgreSQL e SQL.

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
│   └── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

> O `AGENTS.md` fica na raiz de propósito: agentes como Codex procuram instruções `AGENTS.md` a partir da raiz do repositório e ao longo do caminho até o diretório de trabalho.

## Stack

Resumo atual/planejado:

- Python
- FastAPI
- Pydantic
- Uvicorn
- PostgreSQL
- SQL
- SQLAlchemy
- Alembic
- Pytest
- Git/GitHub
- Docker

As decisões e o que já está efetivamente adotado estão em [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Executando localmente

Com o ambiente virtual ativo:

```powershell
pip install -r requirements.txt
uvicorn app.main:app --reload
```

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
