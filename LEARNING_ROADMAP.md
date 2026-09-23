# Operix — Learning Roadmap

Este documento define a ordem de aprendizagem e implementação do Operix.

O objetivo é evitar dois extremos:

1. estudar meses de teoria antes de construir;
2. gerar um sistema inteiro sem compreender o código.

Cada fase deve introduzir apenas os conceitos necessários para o próximo passo.

---

## Como estudar neste projeto

Fluxo recomendado para cada assunto:

```text
1. entender o problema
2. aprender o conceito
3. ver um exemplo pequeno
4. tentar implementar
5. testar
6. revisar erros
7. refatorar se necessário
8. fazer commit
```

Sempre que possível, o desenvolvedor deve tentar escrever a solução antes de receber código completo.

---

# Fase 0 — Preparação do projeto

## Objetivo

Entender como um projeto real começa antes da primeira funcionalidade.

## Aprender

- diferença entre Git e GitHub;
- repositório;
- commit;
- working tree;
- `.gitignore`;
- README;
- documentação;
- estrutura básica de projeto;
- ambiente virtual Python;
- dependências.

## Entregáveis

- repositório criado;
- `README.md`;
- `PROJECT_SPEC.md`;
- `LEARNING_ROADMAP.md`;
- `.gitignore`;
- ambiente local preparado.

## Critério de conclusão

O desenvolvedor consegue clonar/abrir o projeto, explicar para que servem os arquivos iniciais e fazer um commit conscientemente.

---

# Fase 1 — Python aplicado ao back-end

## Objetivo

Garantir os fundamentos de Python necessários para construir a API sem interromper o projeto para revisar sintaxe básica constantemente.

## Aprender/revisar conforme necessário

- variáveis;
- tipos;
- condicionais;
- loops;
- funções;
- argumentos e retorno;
- listas;
- dicionários;
- conjuntos;
- módulos;
- imports;
- exceções;
- classes e objetos em nível introdutório;
- type hints;
- leitura de documentação.

## Exercício dentro do projeto

Criar pequenos módulos ou scripts apenas quando servirem para compreender um conceito que será usado logo em seguida.

## Critério de conclusão

O desenvolvedor consegue ler e escrever funções simples, manipular estruturas de dados e compreender erros comuns de Python.

---

# Fase 2 — HTTP, APIs e FastAPI

## Objetivo

Entender o que uma API faz antes de conectar banco de dados.

## Aprender

- cliente e servidor;
- HTTP;
- request e response;
- métodos GET, POST, PUT/PATCH e DELETE;
- status codes;
- JSON;
- endpoint;
- path parameter;
- query parameter;
- request body;
- FastAPI;
- Pydantic;
- Swagger/OpenAPI.

## Primeiras funcionalidades

Criar endpoints temporários em memória para praticar os conceitos.

Exemplos educacionais:

- health check;
- listar recursos fictícios;
- criar recurso em memória;
- validar payload.

## Critério de conclusão

O desenvolvedor consegue explicar o caminho:

```text
requisição
→ rota
→ validação
→ função
→ resposta
```

---

# Fase 3 — PostgreSQL e SQL

## Objetivo

Aprender banco relacional antes de depender de ORM.

## Aprender

- banco de dados relacional;
- tabela;
- linha;
- coluna;
- tipo de dado;
- primary key;
- foreign key;
- NOT NULL;
- UNIQUE;
- CHECK;
- INSERT;
- SELECT;
- UPDATE;
- DELETE;
- WHERE;
- ORDER BY;
- JOIN;
- GROUP BY;
- agregações;
- transações;
- índices em nível introdutório.

## Regra pedagógica

Sempre que uma operação importante for criada via ORM, entender também a ideia equivalente em SQL.

## Critério de conclusão

O desenvolvedor consegue criar tabelas simples e escrever consultas relacionando dados sem depender exclusivamente do ORM.

---

# Fase 4 — SQLAlchemy e Alembic

## Objetivo

Conectar a API ao PostgreSQL de maneira organizada.

## Aprender

- conexão com banco;
- sessão;
- model;
- ORM;
- relacionamento;
- migration;
- Alembic;
- diferença entre model de banco e schema de API.

## Primeiras entidades

- Organization
- Branch

## Critério de conclusão

Criar e consultar organizações e filiais persistidas no PostgreSQL.

---

# Fase 5 — Usuários, autenticação e permissões básicas

## Objetivo

Criar a base de segurança antes de abrir dados de múltiplas empresas.

## Aprender

- autenticação x autorização;
- hash de senha;
- identidade do usuário;
- token;
- permissões;
- RBAC;
- isolamento por organização.

## Entidades

- User
- Role
- associações necessárias

## Critério de conclusão

Usuários autenticados acessam apenas os dados permitidos de sua organização.

---

# Fase 6 — Clientes

## Objetivo

Implementar o primeiro módulo de negócio completo.

## Aprender

- CRUD;
- validação;
- regras de negócio;
- organização de serviços;
- tratamento de erros;
- filtros;
- paginação inicial.

## Funcionalidades

- criar cliente;
- consultar cliente;
- editar cliente;
- ativar/desativar compartilhamento entre filiais;
- configurar limite de compra a prazo;
- listar clientes.

## Critério de conclusão

As regras de visibilidade entre filiais respeitam a especificação.

---

# Fase 7 — Produtos e estoque por filial

## Objetivo

Aprender modelagem em que dados globais e dados por filial coexistem.

## Entidades conceituais

- Product
- BranchProduct
- StockMovement

## Aprender

- relacionamentos;
- estoque derivado de movimentações;
- transações;
- consistência;
- filtros por filial.

## Funcionalidades

- cadastrar produto;
- associar produto a filial;
- definir preço;
- registrar entrada;
- consultar estoque;
- consultar histórico de movimentações.

---

# Fase 8 — Orçamentos e pedidos

## Objetivo

Construir o núcleo comercial.

## Entidades conceituais

- Quote
- QuoteItem
- Order
- OrderItem

## Aprender

- cabeçalho/itens;
- relacionamentos 1:N;
- snapshots de preço;
- estados;
- conversão de orçamento em pedido;
- regras transacionais.

## Funcionalidades

- criar orçamento;
- adicionar itens;
- calcular total;
- registrar desconto;
- converter em pedido;
- preservar vendedor;
- preservar filial comercial.

---

# Fase 9 — Atendimento parcial

## Objetivo

Modelar retirada e entrega por quantidade.

## Aprender

- modelagem de quantidades;
- invariantes;
- validação de soma;
- estados derivados.

## Regras

O sistema deverá saber quanto foi:

- comprado;
- retirado;
- destinado à entrega;
- entregue;
- pendente.

## Critério de conclusão

Nenhuma quantidade pode ser retirada ou entregue acima da quantidade vendida.

---

# Fase 10 — Conta do cliente e pagamentos

## Objetivo

Construir o núcleo financeiro diretamente ligado a cliente e pedido.

## Aprender

- ledger/histórico;
- alocação de pagamento;
- pagamento parcial;
- crédito;
- aplicação de crédito;
- transações atômicas;
- precisão monetária;
- regras de limite.

## Funcionalidades

- registrar pagamento;
- pagar pedido parcialmente;
- gerar crédito;
- aplicar crédito explicitamente;
- consultar débitos;
- consultar créditos;
- validar limite de compra a prazo.

## Regra crítica

Crédito não compensa débito automaticamente.

---

# Fase 11 — Devoluções

## Objetivo

Integrar pedidos, estoque e conta do cliente.

## Aprender

- reversões;
- rastreabilidade;
- transações envolvendo múltiplos módulos.

## Possíveis efeitos

Uma devolução poderá:

- gerar entrada no estoque;
- gerar crédito ao cliente;
- registrar histórico.

As regras exatas deverão ser definidas antes da implementação.

---

# Fase 12 — Comissão

## Objetivo

Calcular indicadores de venda sem perder origem comercial.

## Funcionalidades

- percentual configurável;
- valor bruto vendido;
- desconto total;
- valor líquido;
- comissão prevista;
- comissão adquirida após pagamento.

## Regra crítica

A filial operacional não altera vendedor nem filial comercial do pedido.

---

# Fase 13 — Veículos e pessoas da logística

## Objetivo

Preparar o módulo de cargas.

## Entidades conceituais

- Vehicle
- Driver/Employee
- associações necessárias

## Funcionalidades

- cadastrar veículo;
- associar veículo a filial;
- registrar capacidade;
- cadastrar motorista;
- registrar ajudantes.

---

# Fase 14 — Cargas

## Objetivo

Implementar a principal funcionalidade logística.

## Aprender

- relação N:N com dados adicionais;
- cálculos de peso;
- estados;
- regras de capacidade;
- agregações.

## Funcionalidades

- criar carga;
- escolher veículo;
- escolher motorista;
- escolher ajudantes;
- adicionar itens de vários pedidos;
- dividir pedido entre cargas;
- calcular peso;
- consultar capacidade utilizada.

---

# Fase 15 — Conferência e expedição

## Objetivo

Criar rastreabilidade da saída da carga.

## Funcionalidades

- iniciar carregamento;
- marcar aguardando conferência;
- registrar conferente;
- liberar carga;
- registrar saída;
- mudar para em entrega.

---

# Fase 16 — Tentativas de entrega

## Objetivo

Manter histórico sem destruir dados anteriores.

## Funcionalidades

- registrar tentativa;
- marcar entregue;
- marcar não entregue;
- informar motivo;
- devolver quantidade pendente à fila de entrega;
- adicionar novamente em carga futura.

---

# Fase 17 — Transferências entre filiais

## Objetivo

Integrar estoque de várias filiais.

## Estados iniciais

- SOLICITADA
- APROVADA
- RECEBIDA

## Aprender

- workflow;
- transações;
- autorização;
- movimentação entre estoques.

Antes de implementar, decidir exatamente em qual estado ocorre cada movimentação de estoque.

---

# Fase 18 — Dashboards e consultas

## Objetivo

Transformar dados operacionais em informação.

## Aprender

- JOINs mais complexos;
- GROUP BY;
- agregações;
- consultas otimizadas;
- índices;
- filtros por período e filial.

## Indicadores possíveis

- vendas por filial;
- vendas por vendedor;
- pedidos do dia;
- entregas pendentes;
- cargas abertas;
- estoque;
- inadimplência;
- comissão prevista;
- comissão adquirida.

---

# Fase 19 — Testes e qualidade

Testes deverão existir antes desta fase, mas aqui haverá uma revisão ampla.

## Aprender

- testes unitários;
- testes de integração;
- fixtures;
- banco de teste;
- casos de borda;
- cobertura como indicador, não como objetivo isolado.

## Prioridade

Testar principalmente regras que movimentam:

- dinheiro;
- estoque;
- quantidades;
- permissões;
- filiais.

---

# Fase 20 — Docker e deploy

## Objetivo

Executar o Operix de forma reproduzível fora da máquina local.

## Aprender

- variáveis de ambiente;
- Docker;
- container;
- imagem;
- volumes;
- aplicação + PostgreSQL;
- produção x desenvolvimento;
- logs;
- deploy.

---

# Regras para uso do Codex/assistentes

Durante o desenvolvimento:

- não pedir "faça o projeto";
- pedir explicação da próxima tarefa;
- tentar implementar antes de solicitar solução completa;
- pedir revisão do código;
- perguntar por que determinado padrão é usado;
- exigir explicação de bibliotecas novas;
- atualizar `PROJECT_SPEC.md` quando regras de negócio mudarem;
- fazer commits pequenos e claros.

---

# Próximo passo

A documentação inicial está pronta.

O próximo passo técnico é preparar o ambiente local:

1. clonar o repositório;
2. criar ambiente virtual;
3. configurar `.gitignore`;
4. confirmar versão do Python;
5. criar a estrutura mínima;
6. executar o primeiro programa conscientemente.

Não instalar todo o ecossistema do projeto de uma vez.
