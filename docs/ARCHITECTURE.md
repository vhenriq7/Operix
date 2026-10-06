# Operix — Arquitetura

**Status:** documento vivo  
**Última atualização:** 2026-10-06

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
- armazenamento temporário de clientes em lista Python para fins didáticos;
- PostgreSQL local integrado à API para organizações e filiais;
- banco local `operix` criado manualmente;
- SQL praticado manualmente via `psql`;
- estudo prévio de SQL com tabelas didáticas `organizacoes`, `filiais` e `clientes`;
- SQLAlchemy usado para consultas e cadastros persistentes;
- Alembic usado para versionar o schema do banco;
- psycopg usado como driver PostgreSQL;
- `app/database.py` com leitura de `DATABASE_URL`;
- `engine`, `SessionLocal` e `get_db` usados nas rotas persistentes;
- `app/models.py` com models SQLAlchemy iniciais `Organizacao` e `Filial`;
- relacionamento SQLAlchemy entre organização e filiais;
- Alembic inicializado com `alembic.ini` e diretório `alembic/`;
- `alembic/env.py` configurado para usar `DATABASE_URL` e `Base.metadata`;
- primeira migration versionada criando `organizacoes` e `filiais`;
- banco local atualizado com `alembic upgrade head`;
- cadastro e listagem de organizações e filiais pela API;
- schemas Pydantic `OrganizacaoCriacao` e `FilialCriacao` para validar os dados de entrada;
- verificação da organização vinculada antes do cadastro de uma filial;
- escape de `%` na configuração do Alembic para aceitar URLs codificadas;
- Git e GitHub.

Ainda não implementado:

- autenticação;
- autorização/RBAC;
- multi-tenancy no código;
- testes automatizados;
- Docker;
- deploy.

## 3. Stack atual e planejada

| Área | Tecnologia | Situação |
| --- | --- | --- |
| Linguagem | Python | Atual |
| API | FastAPI | Atual |
| Validação | Pydantic | Atual |
| Servidor ASGI local | Uvicorn | Atual |
| Banco relacional | PostgreSQL | Atual; integrado à API para organizações e filiais |
| Consultas | SQL | Praticado via `psql`; consultas da aplicação executadas pelo ORM |
| Driver PostgreSQL | psycopg | Atual; usado na conexão com PostgreSQL |
| ORM | SQLAlchemy | Atual; conexão, modelos, relacionamentos e sessões usados pela API |
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
- Pydantic para validação de entrada; as respostas de organizações e filiais são montadas explicitamente como dicionários e listas, sem schemas Pydantic de saída;
- status HTTP semânticos;
- documentação via OpenAPI/Swagger.

Rotas didáticas de clientes em memória e verificação da aplicação:

```text
GET  /
GET  /health
GET  /customers
GET  /customers/{cliente_id}
POST /customers
PATCH /customers/{cliente_id}
DELETE /customers/{cliente_id}
```

Rotas com persistência no PostgreSQL:

```text
GET  /organizacoes
POST /organizacoes/
GET  /filiais
POST /filiais
```

As rotas de clientes continuam como exercício em memória; o módulo persistente de clientes será construído em etapa posterior.

## 6. Persistência

### Clientes em memória

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

### Organizações e filiais no PostgreSQL

A API já usa SQLAlchemy para cadastrar e consultar organizações e filiais no PostgreSQL, com schema versionado pelo Alembic.

As dependências da Fase 4 já foram instaladas:

```text
SQLAlchemy
Alembic
psycopg
```

Configuração de conexão e sessão em `app/database.py`:

```text
DATABASE_URL
engine
SessionLocal
get_db
```

A URL de conexão deve vir de variável de ambiente. Senhas reais não devem ser commitadas no repositório.

As rotas persistentes recebem uma sessão por meio de `Depends(get_db)`. A dependência cria a sessão, disponibiliza-a para a requisição e a fecha no bloco `finally`.

Modelos SQLAlchemy em `app/models.py`:

```text
Organizacao
Filial
```

Esses modelos representam as tabelas `organizacoes` e `filiais`, possuem relacionamento Python entre organização e filiais e são usados pelas rotas da API. `Filial.organizacao_id` é uma chave estrangeira que referencia `Organizacao.id`.

No cadastro, os schemas Pydantic validam a entrada; a rota cria uma instância do modelo SQLAlchemy, adiciona-a à sessão e confirma a transação com `commit()`. O cadastro de filial consulta a organização vinculada antes da inserção e responde `404` se ela não existir.

Na listagem, a consulta ORM devolve objetos dos modelos. As rotas montam listas de dicionários com os campos da resposta, que o FastAPI serializa em JSON.

Alembic foi inicializado com:

```text
alembic.ini
alembic/env.py
alembic/versions/
```

O `env.py` lê `DATABASE_URL`, usa `Base.metadata` como referência para autogeração e não armazena senha real no repositório.

A leitura verifica a ausência de `DATABASE_URL` antes de tratar o texto. Ao fornecer a URL à configuração do Alembic, cada `%` é escapado como `%%`, pois o leitor de configuração interpreta esse caractere. Ao recuperar a opção, a URL original codificada é preservada para o SQLAlchemy. Esse escape não criptografa nem oculta credenciais.

A primeira migration versionada é:

```text
81819ad65a8a_cria_tabelas_de_organizacoes_e_filiais.py
```

Ela cria `organizacoes` e `filiais` no `upgrade()` e remove essas tabelas no `downgrade()`.

O progresso, as validações realizadas e o próximo passo de aprendizagem ficam em [ROADMAP.md](ROADMAP.md).

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

A unidade superior do SaaS é a organização; uma organização possui filiais, representadas inicialmente pelos modelos `Organizacao` e `Filial`.

Regra arquitetural obrigatória:

> Dados de uma organização nunca podem vazar para outra organização.

A estratégia técnica exata de isolamento ainda será definida antes da implementação do módulo multi-tenant.

As rotas atuais ainda não autenticam usuários nem restringem consultas por organização. A API desta etapa é destinada ao estudo local, não ao uso como SaaS em produção.

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
