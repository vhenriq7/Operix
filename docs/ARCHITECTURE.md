# Operix — Arquitetura

**Status:** documento vivo  
**Última revisão estrutural:** 2026-09-30

Este documento registra decisões técnicas. Requisitos de negócio pertencem a [SPEC.md](SPEC.md); progresso pertence a [ROADMAP.md](ROADMAP.md).

## 1. Princípios

1. **Back-end first:** o aprendizado e a primeira versão do produto priorizam API e domínio.
2. **Monólito modular primeiro:** não usar microserviços sem necessidade real.
3. **Simplicidade antes de abstração:** novas camadas só entram quando resolvem um problema concreto.
4. **SQL deve ser aprendido de verdade:** ORM não substitui entendimento de SQL.
5. **Persistência e regras críticas devem ser testáveis.**
6. **Multi-tenancy é requisito de segurança**, não apenas filtro de interface.
7. **Documentação acompanha decisões reais**, distinguindo o que existe do que está planejado.

## 2. Estado técnico atual

Implementado hoje:

- Python 3.14 no ambiente local;
- FastAPI;
- Uvicorn;
- Pydantic;
- API REST inicial;
- Swagger/OpenAPI gerado pelo FastAPI;
- armazenamento temporário em lista Python para fins didáticos;
- PostgreSQL instalado localmente para estudo;
- banco local `operix` criado manualmente;
- SQL praticado manualmente via `psql`;
- tabelas didáticas em português: `organizacoes`, `filiais` e `clientes`;
- SQLAlchemy instalado como dependência;
- Alembic instalado como dependência;
- psycopg instalado como driver PostgreSQL;
- `app/database.py` com leitura de `DATABASE_URL`;
- `engine`, `SessionLocal` e `get_db` configurados para uso futuro nas rotas;
- `app/models.py` com models SQLAlchemy iniciais `Organizacao` e `Filial`;
- relacionamento SQLAlchemy entre organização e filiais;
- Alembic inicializado com `alembic.ini` e diretório `alembic/`;
- `alembic/env.py` configurado para usar `DATABASE_URL` e `Base.metadata`;
- primeira migration versionada criando `organizacoes` e `filiais`;
- banco local atualizado com `alembic upgrade head`;
- Git e GitHub.

Ainda não implementado:

- uso da sessão de banco nas rotas da API;
- autenticação;
- autorização/RBAC;
- multi-tenancy no código;
- testes automatizados;
- Docker;
- deploy.

## 3. Stack planejada

| Área | Tecnologia | Situação |
| --- | --- | --- |
| Linguagem | Python | Atual |
| API | FastAPI | Atual |
| Validação | Pydantic | Atual |
| Servidor ASGI local | Uvicorn | Atual |
| Banco relacional | PostgreSQL | Atual para estudo local; integração com a API planejada |
| Consultas | SQL | Atual para estudo manual; integração pela aplicação planejada |
| Driver PostgreSQL | psycopg | Instalado |
| ORM | SQLAlchemy | Instalado; conexão, sessão e models iniciais configurados |
| Migrações | Alembic | Configurado; primeira migration aplicada |
| Testes | Pytest | Planejado |
| Containers | Docker | Planejado |
| Versionamento | Git + GitHub | Atual |

O provedor de deploy ainda não foi escolhido.

## 4. Forma arquitetural inicial

O Operix começa como **monólito modular**.

Motivos:

- um único produto e um único time/desenvolvedor;
- aprendizado mais direto;
- transações atravessarão pedidos, estoque e conta do cliente;
- microserviços adicionariam complexidade sem benefício atual.

A estrutura interna será separada gradualmente conforme os módulos surgirem. Não criar pastas e camadas vazias antecipadamente apenas para parecer uma arquitetura "enterprise".

## 5. API

Diretrizes atuais:

- HTTP/JSON;
- estilo REST quando adequado;
- FastAPI como camada de entrada;
- Pydantic para validação de entrada/saída;
- status HTTP semânticos;
- documentação via OpenAPI/Swagger.

Exemplos já praticados:

```text
GET  /health
GET  /customers
GET  /customers/{customer_id}
POST /customers
```

Rotas educacionais atuais podem mudar quando o modelo persistente real for criado.

## 6. Persistência

### Agora

Clientes são guardados em uma lista Python apenas para demonstrar memória de processo.

Consequência intencional:

```text
reiniciar a aplicação
→ lista é recriada
→ dados desaparecem
```

Esse mecanismo não é persistência de produção.

Em paralelo, PostgreSQL já foi instalado localmente e o banco `operix` foi usado para praticar SQL manualmente com tabelas didáticas em português:

```text
organizacoes
filiais
clientes
```

Essas tabelas fizeram parte do aprendizado de SQL. Depois, o banco local foi limpo para que o Alembic passasse a controlar a criação do schema versionado.

### Etapa atual

Conectar a API ao PostgreSQL com SQLAlchemy e Alembic.

As dependências da Fase 4 já foram instaladas:

```text
SQLAlchemy
Alembic
psycopg
```

Configuração inicial criada em `app/database.py`:

```text
DATABASE_URL
engine
SessionLocal
get_db
```

A URL de conexão deve vir de variável de ambiente. Senhas reais não devem ser commitadas no repositório.

Models iniciais criados em `app/models.py`:

```text
Organizacao
Filial
```

Esses models já representam as tabelas `organizacoes` e `filiais` e possuem relacionamento Python entre organização e filiais. Eles já foram consultados manualmente via SQLAlchemy, mas ainda não são usados pelas rotas da API.

Alembic foi inicializado com:

```text
alembic.ini
alembic/env.py
alembic/versions/
```

O `env.py` lê `DATABASE_URL`, usa `Base.metadata` como referência para autogeração e não armazena senha real no repositório.

A primeira migration versionada é:

```text
81819ad65a8a_cria_tabelas_de_organizacoes_e_filiais.py
```

Ela cria `organizacoes` e `filiais` no `upgrade()` e remove essas tabelas no `downgrade()`.

O próximo passo técnico é criar rotas da API para inserir e consultar `Organizacao` e `Filial` usando sessão real do banco.

A sequência pedagógica é:

```text
SQL e banco relacional
→ PostgreSQL manual via psql
→ integração com a aplicação
→ SQLAlchemy
→ Alembic
```

Sempre que uma operação importante for implementada via ORM, o conceito SQL equivalente deve ser entendido.

## 7. Modelo multi-tenant

A unidade superior do SaaS é `Organization`; uma organização possui `Branches`.

Regra arquitetural obrigatória:

> Dados de uma organização nunca podem vazar para outra organização.

A estratégia técnica exata de isolamento ainda será definida antes da implementação do módulo multi-tenant.

Clientes poderão ter visibilidade restrita a uma filial ou compartilhada dentro da mesma organização, conforme [SPEC.md](SPEC.md).

## 8. Autenticação e autorização

Planejado:

- autenticação de usuário;
- hash seguro de senha;
- identidade do usuário nas requisições;
- autorização baseada em papéis/permissões (RBAC);
- escopo por organização e filial.

Detalhes de token, sessão e biblioteca de autenticação ainda não foram decididos.

## 9. Dinheiro, estoque e quantidades

Módulos que alteram dinheiro, crédito, estoque, atendimento parcial ou cargas deverão usar operações consistentes e, quando persistidos, transações de banco quando necessário.

Valores monetários não devem usar `float` como representação persistente.

A estratégia exata de tipo monetário será definida antes do módulo financeiro.

## 10. Testes

Testes serão introduzidos progressivamente.

Prioridade de cobertura:

1. isolamento entre organizações/filiais;
2. dinheiro e crédito;
3. estoque;
4. quantidades de pedido/entrega;
5. permissões;
6. fluxos de carga e transferência.

A fase de qualidade do roadmap é uma revisão ampla, não o primeiro momento em que testes podem existir.

## 11. Front-end

Front-end não é prioridade inicial.

Durante o desenvolvimento da API, Swagger/OpenAPI pode servir como interface de inspeção e teste.

Uma interface visual de demonstração poderá ser escolhida no futuro. Nenhuma tecnologia de front-end está decidida.

## 12. Decisões ainda abertas

Não assumir sem discussão:

- estratégia concreta de multi-tenancy;
- biblioteca/forma de autenticação;
- momento exato da baixa de estoque em transferências;
- representação monetária definitiva;
- política de excesso de capacidade de carga;
- provedor de deploy;
- tecnologia de front-end.

Quando uma dessas decisões for tomada, registrar aqui o motivo e a consequência.
