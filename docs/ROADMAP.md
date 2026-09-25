# Operix — Roadmap

Este documento controla **ordem de aprendizagem, fases de desenvolvimento, progresso e critérios de conclusão**.

Regras detalhadas do produto ficam em [SPEC.md](SPEC.md). Decisões técnicas ficam em [ARCHITECTURE.md](ARCHITECTURE.md).

## Status geral

**Fase atual:** Fase 3 — PostgreSQL e SQL  
**Próxima fase:** Fase 4 — SQLAlchemy e Alembic  
**Objetivo imediato:** aprender persistência relacional com SQL antes de conectar a API ao banco.

Legenda:

- ✅ concluída;
- 🟡 em andamento;
- ⬜ não iniciada.

## Visão do MVP

O MVP pretendido deve demonstrar um fluxo operacional coerente de uma organização multi-filial, incluindo:

```text
organização/filiais
→ usuários
→ clientes
→ produtos/estoque
→ orçamento/pedido
→ conta do cliente
→ atendimento
→ carga/entrega
→ visão gerencial
```

O escopo poderá ser reduzido se necessário para manter qualidade e aprendizagem. "MVP" não significa implementar todos os recursos futuros descritos na SPEC.

---

## ✅ Fase 0 — Preparação do projeto

### Objetivo

Criar um ambiente de trabalho versionado, reproduzível e documentado.

### Concluído

- repositório Git/GitHub;
- ambiente virtual;
- `.gitignore`;
- dependências iniciais;
- README;
- documentação estruturada;
- commits e push realizados conscientemente.

### Critério de conclusão

O desenvolvedor consegue abrir/clonar o projeto, ativar o ambiente, entender os arquivos principais e usar o ciclo básico `status → add → commit → push`.

---

## ✅ Fase 1 — Python aplicado ao back-end

### Objetivo

Ter base suficiente de Python para aprender back-end dentro do próprio projeto.

### Base usada até aqui

- variáveis e tipos;
- funções;
- argumentos e retorno;
- listas e `.append()`;
- dicionários;
- imports;
- classes em nível introdutório;
- type hints;
- `None`;
- leitura de erros de sintaxe.

Esta fase não significa "Python concluído". Novos conceitos serão aprendidos conforme forem necessários.

### Critério de conclusão

O desenvolvedor consegue ler e alterar pequenas funções Python e entender as estruturas usadas nas rotas iniciais.

---

## ✅ Fase 2 — HTTP, APIs e FastAPI

### Objetivo

Entender o caminho de uma requisição antes de conectar banco de dados.

### Já praticado

- [x] cliente x servidor;
- [x] iniciar FastAPI com Uvicorn;
- [x] endpoint;
- [x] `GET`;
- [x] `POST`;
- [x] JSON;
- [x] request/response;
- [x] path parameter;
- [x] query parameter;
- [x] request body;
- [x] Pydantic `BaseModel`;
- [x] campo obrigatório x opcional;
- [x] status `200 OK`;
- [x] status `201 Created`;
- [x] erro de validação `422`;
- [x] Swagger/OpenAPI;
- [x] armazenamento temporário em memória;
- [x] observar perda dos dados ao reiniciar o processo.

### Ainda praticar antes de encerrar

- [x] `PATCH` ou `PUT` em exemplo simples;
- [x] `DELETE` em exemplo simples;
- [x] resposta `404 Not Found` criada pela aplicação;
- [x] explicar sem ajuda o fluxo completo de uma requisição.

### Critério de conclusão

O desenvolvedor consegue explicar:

```text
cliente
→ requisição HTTP
→ rota
→ validação
→ função
→ resposta HTTP
```

e entende quando usar GET, POST, PATCH/PUT e DELETE em um CRUD básico.

### Próximo passo

Fase concluída. Próximo aprendizado: PostgreSQL e SQL.

---

## 🟡 Fase 3 — PostgreSQL e SQL

### Objetivo

Aprender persistência relacional antes de depender de ORM.

### Aprender

- banco, tabela, linha e coluna;
- tipos;
- primary key;
- foreign key;
- `NOT NULL`, `UNIQUE`, `CHECK`;
- `INSERT`, `SELECT`, `UPDATE`, `DELETE`;
- `WHERE`, `ORDER BY`;
- `JOIN`;
- `GROUP BY` e agregações;
- transações;
- índices em nível introdutório.

### Critério de conclusão

Criar tabelas e consultas SQL simples, incluindo relacionamento entre tabelas, sem depender exclusivamente de ORM.

---

## ⬜ Fase 4 — SQLAlchemy e Alembic

### Objetivo

Conectar FastAPI ao PostgreSQL com persistência organizada.

### Aprender

- conexão;
- sessão;
- model;
- ORM;
- relacionamentos;
- migration;
- diferença entre modelo de banco e schema de API.

### Primeiras entidades persistentes

- Organization;
- Branch.

### Critério de conclusão

Criar e consultar organizações e filiais persistidas no PostgreSQL e reproduzir o schema por migração.

---

## ⬜ Fase 5 — Usuários, autenticação e permissões

### Objetivo

Construir a base de segurança do SaaS multi-tenant.

### Aprender

- autenticação x autorização;
- hash de senha;
- identidade do usuário;
- tokens/sessões conforme decisão futura;
- RBAC;
- isolamento por organização e filial.

### Critério de conclusão

Usuários autenticados só acessam dados autorizados de sua organização/filial.

---

## ⬜ Fase 6 — Clientes

### Objetivo

Implementar o primeiro módulo de negócio persistente.

### Funcionalidades

- criar;
- consultar;
- editar;
- listar;
- compartilhar ou restringir entre filiais;
- configurar limite de compra a prazo;
- filtros e paginação inicial.

### Critério de conclusão

CRUD persistente e regras de visibilidade de clientes coerentes com a SPEC.

---

## ⬜ Fase 7 — Produtos e estoque por filial

### Entidades conceituais

- Product;
- BranchProduct;
- StockMovement.

### Funcionalidades

- catálogo;
- preço por filial;
- estoque por filial;
- entrada/saída;
- histórico de movimentações.

### Critério de conclusão

O estoque atual pode ser explicado por movimentações rastreáveis.

---

## ⬜ Fase 8 — Orçamentos e pedidos

### Entidades conceituais

- Quote;
- QuoteItem;
- Order;
- OrderItem.

### Funcionalidades

- criar orçamento;
- itens;
- desconto;
- conversão para pedido;
- preservar vendedor e filial comercial.

### Critério de conclusão

Um orçamento pode virar pedido sem perder a origem comercial e os valores relevantes.

---

## ⬜ Fase 9 — Atendimento parcial

### Objetivo

Representar retirada e entrega por item e quantidade.

### Critério de conclusão

O sistema sabe quanto foi comprado, retirado, destinado à entrega, entregue e ainda está pendente, sem exceder a quantidade vendida.

---

## ⬜ Fase 10 — Conta do cliente e pagamentos

### Funcionalidades

- pagamento integral/parcial;
- débito por pedido;
- crédito;
- aplicação explícita de crédito;
- limite de compra a prazo;
- histórico.

### Regra crítica

Crédito não compensa débito automaticamente.

### Critério de conclusão

É possível rastrear qual pagamento/crédito foi aplicado a qual obrigação.

---

## ⬜ Fase 11 — Devoluções

### Objetivo

Integrar devolução, estoque e conta do cliente.

Antes da implementação, validar todas as regras ainda abertas sobre devolução.

---

## ⬜ Fase 12 — Comissão

### Funcionalidades

- percentual configurável;
- valor bruto;
- descontos;
- valor líquido;
- comissão prevista;
- comissão adquirida quando o pedido estiver pago.

A filial operacional não altera vendedor nem filial comercial.

---

## ⬜ Fase 13 — Veículos, motoristas e ajudantes

Preparar os cadastros e vínculos necessários para a logística.

---

## ⬜ Fase 14 — Cargas

### Funcionalidades

- criar carga;
- veículo;
- motorista;
- ajudantes;
- itens de múltiplos pedidos;
- divisão de um pedido em várias cargas;
- peso/capacidade.

---

## ⬜ Fase 15 — Conferência e expedição

Registrar carregamento, conferência, liberação e saída com rastreabilidade.

---

## ⬜ Fase 16 — Tentativas de entrega

Registrar entregue/não entregue, motivo, histórico e retorno do que ficou pendente para nova carga.

---

## ⬜ Fase 17 — Transferências entre filiais

Fluxo inicial:

```text
SOLICITADA
→ APROVADA
→ RECEBIDA
```

Antes de implementar, decidir em qual momento cada estoque é movimentado.

---

## ⬜ Fase 18 — Dashboards e consultas

Indicadores por filial e consolidados da organização.

Aprender consultas agregadas, filtros, índices e otimização conforme necessidade.

---

## ⬜ Fase 19 — Testes e qualidade

Testes podem ser introduzidos antes desta fase. Aqui ocorre a revisão abrangente:

- testes unitários;
- integração;
- fixtures;
- banco de teste;
- casos de borda;
- revisão de segurança e regras críticas.

Prioridade: dinheiro, estoque, quantidades, permissões e isolamento multi-tenant.

---

## ⬜ Fase 20 — Docker e deploy

### Objetivo

Executar o Operix de maneira reproduzível fora do ambiente local.

### Aprender

- variáveis de ambiente;
- containers;
- imagem;
- volumes;
- API + PostgreSQL;
- logs;
- diferenças entre desenvolvimento e produção;
- deploy.

---

## Regra de atualização

Quando algo relevante for concluído:

1. atualizar os checkboxes correspondentes;
2. revisar o critério da fase;
3. se o critério foi cumprido, marcar a fase como ✅;
4. marcar a próxima como 🟡;
5. atualizar **Status geral** e **Próximo passo**;
6. refletir a mudança de fase no `README.md`.

As instruções detalhadas para agentes estão em [../AGENTS.md](../AGENTS.md).
