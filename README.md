# Operix

> SaaS de gestão operacional para empresas com múltiplas filiais.

O **Operix** é um projeto de estudo e portfólio focado em back-end. O produto busca integrar vendas, clientes, conta comercial, estoque, transferências entre filiais, cargas e entregas, enquanto o desenvolvimento é usado para aprender Python, APIs, SQL, PostgreSQL e arquitetura de software na prática.

## Estado atual

**Fase 5 — Usuários, autenticação e permissões (em andamento).**

O foco inicial é desenvolver e validar os fluxos de uma empresa com várias filiais. A ampliação para outras empresas permanece planejada, conforme [docs/SPEC.md](docs/SPEC.md).

As fases de fundamentos de API, SQL e integração com SQLAlchemy e Alembic foram concluídas. A etapa atual prepara as contas de usuário, o login e as permissões entre filiais, ainda sem implementação de segurança na API. Já foram praticados:

- aplicação FastAPI executada com Uvicorn;
- endpoints `GET`, `POST`, `PATCH` e `DELETE`;
- parâmetros de caminho;
- parâmetros de consulta;
- corpo da requisição;
- validação com Pydantic;
- códigos de resposta HTTP como `200`, `201`, `404` e `422`;
- Swagger/OpenAPI;
- armazenamento temporário de clientes em memória;
- PostgreSQL local com banco `operix`;
- SQL básico com tabelas, chaves primárias, chaves estrangeiras, restrições, `JOIN`, `GROUP BY`, transações e índices introdutórios;
- modelagem didática em português com `organizacoes`, `filiais` e `clientes`;
- dependências iniciais da Fase 4 instaladas: SQLAlchemy, Alembic e psycopg;
- conexão e sessões de banco em `app/database.py` com `DATABASE_URL`, `engine`, `SessionLocal` e `get_db`;
- modelos SQLAlchemy em `app/models.py` para `Organizacao` e `Filial`, com relacionamento entre elas;
- Alembic inicializado e configurado para ler `DATABASE_URL` e `Base.metadata`;
- primeira migração aplicada no PostgreSQL, criando `organizacoes` e `filiais`;
- cadastro e listagem de organizações e filiais pela API, com persistência no PostgreSQL;
- verificação da existência da organização antes de cadastrar uma filial, com resposta `404` quando ela não é encontrada.

Clientes continuam armazenados em uma lista em memória para fins didáticos. Organizações e filiais já são cadastradas e consultadas no PostgreSQL por meio do SQLAlchemy.

A API é destinada ao estudo local nesta etapa. Autenticação e isolamento de dados entre organizações ainda não foram implementados.

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
├── alembic/
│   ├── env.py
│   └── versions/
├── app/
│   ├── database.py
│   ├── main.py
│   └── models.py
├── alembic.ini
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
| PostgreSQL | Atual; integrado à API para organizações e filiais |
| SQL | Atual para estudo manual via `psql` |
| SQLAlchemy | Atual; modelos e sessões usados no cadastro e na listagem pela API |
| Alembic | Configurado; primeira migração aplicada |
| psycopg | Atual; driver de conexão com PostgreSQL |
| Git/GitHub | Atual |
| Pytest | Planejado |
| Docker | Planejado |

As decisões e o que já está efetivamente adotado estão em [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Executando localmente

Execute os comandos abaixo na raiz do projeto, com o ambiente virtual ativo. O PostgreSQL deve estar em execução e o banco `operix` deve existir. Não é necessário manter o `psql` aberto.

### 1. Instalar as dependências

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 2. Configurar a conexão com o banco

Defina `DATABASE_URL` antes de executar o Alembic ou iniciar a API. A senha é solicitada sem aparecer no terminal, e os caracteres especiais são codificados para montar a URL:

```powershell
$senhaBanco = Read-Host "Senha do usuario postgres" -AsSecureString
$senhaUrl = [uri]::EscapeDataString([System.Net.NetworkCredential]::new("", $senhaBanco).Password)
$env:DATABASE_URL = "postgresql+psycopg://postgres:${senhaUrl}@localhost:5432/operix"
```

A variável é definida para essa sessão do PowerShell; configure-a novamente ao abrir um novo terminal. Codificar a senha não a torna secreta: não compartilhe o conteúdo de `DATABASE_URL` nem inclua credenciais reais em commits.

### 3. Aplicar as migrações

Com a conexão configurada, aplique as migrações pendentes:

```powershell
.\.venv\Scripts\alembic.exe upgrade head
```

### 4. Iniciar a API

No mesmo terminal:

```powershell
.\.venv\Scripts\uvicorn.exe app.main:app --reload
```

Mantenha o terminal aberto enquanto usar a API. Para encerrar o servidor, pressione `Ctrl+C`.

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
