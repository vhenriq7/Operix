# Operix — Roadmap

Este documento controla **ordem de aprendizagem, fases de desenvolvimento, progresso e critérios de conclusão**.

Regras detalhadas do produto ficam em [SPEC.md](SPEC.md). Decisões técnicas ficam em [ARCHITECTURE.md](ARCHITECTURE.md).

## Status geral

**Fase atual (trilha técnica):** Fase 5 — Usuários, autenticação e permissões

**Próxima fase técnica:** Fase 6 — Clientes

**Objetivo imediato:** levantar dados das contas de usuário, estudar senhas seguras e validar as regras do marco D0 antes da execução D1.

Legenda:

- ✅ concluída;
- 🟡 em andamento;
- ⬜ não iniciada.

## Visão do MVP

O primeiro corte demonstrável são os marcos D1–D5. O MVP ampliado prevê os fluxos abaixo sem exigir tudo antes da primeira apresentação.

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

### Estratégia de implementação

Por decisão do desenvolvedor, os fluxos serão construídos e validados primeiro em uma empresa com várias filiais. A ampliação para múltiplas organizações será planejada após estabilizar esses fluxos, para manter o aprendizado incremental. As fases existentes continuam na mesma ordem; a validação de segurança para oferecer acesso a outras empresas fica na etapa futura de ampliação descrita ao final deste roadmap.

---

## Plano de entrega por valor (sem alterar estado das fases técnicas)

Além das fases 0–20 abaixo, haverá **marcos D0–D8**. Estes marcos ordenam a demonstração para o gestor; a trilha técnica conserva seu status real. **Nenhum marco foi implementado pelo simples fato de estar documentado.** Não prometer datas sem estimativas.

| Marco | Meta de demonstração | Critério de aceite com dados fictícios | Estado |
| --- | --- | --- | --- |
| D0 — requisitos | Validar os cenários e as decisões abertas em PRODUCT_BLUEPRINT + SPEC | Os quatro casos de pagamento/adiantamento, caixas, cobrança e entrega parcial estão reproduzíveis em exemplos | 🟡 levantamento, não aprovado |
| D1 — acessos | Usuários e permissão por função/filial | Um caixa não consulta filial proibida; a administração acessa o consolidado | ⬜ |
| D2 — cadastros | Cliente PF/PJ, produto e estoque básico por filial | Cadastros persistem, respeitam regras e estoque/preço da filial | ⬜ |
| D3 — comercial | Orçamento, descontos com alerta, clone, pedido aberto, impressão | Salvar, converter e imprimir pedido com todos os itens e endereço sem gerar pagamento fictício | ⬜ |
| D4 — financeiro essencial | Recebimento misto/parcial, fiado, crédito livre separado, adiantamento, caixa e contagem | Dívida R$ 90 e crédito R$ 2.000 coexistem; pagamento misto concilia caixa e contas a receber | ⬜ |
| D5 — cobrança + gerencial | Cobranças, datas originais e próximo contato, painel comparativo | Dívida permanece vencida no relatório enquanto sai da fila diária até próxima cobrança; consolidar filiais | ⬜ |
| D6 — logística | Cargas, romaneio, entregas parciais, pendências, prestação de contas por pedido | Entrega parcial reaparece sem data obrigatória; dinheiro do motorista só entra após conferência | ⬜ |
| D7 — financeiro ampliado | Boleto real mediante integração, prazos configuráveis, cheques, bancos, contas a pagar | Parcelas somam valor exato; cheque repassado liga-se à despesa; saída bancária não reduz caixa físico | ⬜ |
| D8 — validação comercial | Testes, UX, relatórios e roteiro de demonstração sem dados reais | Gestor executa jornadas e confere números, relatórios e documentos | ⬜ |

### Portões de mudança de ambiente

- **G1 — Aprovação pela direção:** demonstrar funcionamento; registrar escopo, autorização, condições de uso, custos, suporte e responsabilidades.
- **G2 — Homologação/pré-produção:** implementar testes de autorização, finanças, estoque, caixa, carga e integrações bancárias; backup/restauração, proteção de dados, deploy, monitoramento e plano de rollback.
- **G3 — Produção controlada:** iniciar implantação apenas após G1 e G2; comparar resultados com sistema anterior e acompanhar suporte. **G3 não é automático.**
- Expansão para outras empresas só depois de validar isolamento multi-tenant e compromissos operacionais.

**Primeiro roteiro demonstrável (D1–D5):** cliente e produto → orçamento com desconto/alerta → pedido aberto e impressão → pagamentos Pix + fiado com vencimento e crédito livre intocado → caixa e dashboard das três filiais. Logística e contas a pagar entram em seguida sem bloquear a primeira apresentação.

**Foco fiscal/contábil completo:** visão de longo prazo, com requisitos especializados fora dos marcos D1–D8 atuais, salvo as integrações de boleto regularizadas em D7.

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

## ✅ Fase 3 — PostgreSQL e SQL

### Objetivo

Aprender persistência relacional antes de depender de ORM.

### Já praticado

- [x] PostgreSQL instalado e acessado com `psql`;
- [x] criação e conexão com o banco `operix`;
- [x] banco, tabela, linha e coluna;
- [x] tipos `INTEGER` e `TEXT`;
- [x] primary key;
- [x] id automático com `GENERATED ALWAYS AS IDENTITY`;
- [x] foreign key;
- [x] `NOT NULL`, `UNIQUE`, `CHECK`;
- [x] `INSERT`, `SELECT`, `UPDATE`, `DELETE`;
- [x] `WHERE`, `ORDER BY`;
- [x] `JOIN` e `LEFT JOIN`;
- [x] `GROUP BY`, `COUNT` e agregações simples;
- [x] tabelas didáticas em português: `organizacoes`, `filiais`, `clientes`.

### Ainda praticar antes de encerrar

- [x] consultas envolvendo mais de uma organização;
- [x] transações;
- [x] índices em nível introdutório;
- [x] explicar sem ajuda relacionamentos, `JOIN`, `LEFT JOIN`, `GROUP BY` e `COUNT`.

### Critério de conclusão

Criar tabelas e consultas SQL simples, incluindo relacionamento entre tabelas, sem depender exclusivamente de ORM.

### Próximo passo

Fase concluída. Próximo aprendizado: SQLAlchemy e Alembic.

---

## ✅ Fase 4 — SQLAlchemy e Alembic

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

### Já praticado

- [x] dependências instaladas no ambiente virtual: SQLAlchemy, Alembic e psycopg;
- [x] `requirements.txt` atualizado com as dependências da Fase 4.
- [x] configuração inicial de conexão em `app/database.py`;
- [x] criação de `engine`, `SessionLocal` e `get_db`;
- [x] teste manual de conexão com `SELECT 1`.
- [x] models SQLAlchemy criados para `Organizacao` e `Filial`;
- [x] relacionamento configurado entre `Organizacao.filiais` e `Filial.organizacao`;
- [x] consultas manuais via SQLAlchemy para `Organizacao`, `Filial` e relacionamento.
- [x] Alembic inicializado no projeto;
- [x] `alembic/env.py` configurado para usar `Base.metadata` e `DATABASE_URL`;
- [x] primeira migration criada e aplicada no PostgreSQL;
- [x] tabela `alembic_version` verificada com a revision `81819ad65a8a`.
- [x] cadastro e listagem de organizações pela API usando sessão SQLAlchemy;
- [x] cadastro e listagem de filiais pela API usando sessão SQLAlchemy;
- [x] verificação da existência da organização antes de cadastrar uma filial;
- [x] tratamento de URL codificada na configuração do Alembic.

### Validações realizadas

- `POST /organizacoes/` retornou `201` com `id` e `nome`; o cadastro apareceu depois em `GET /organizacoes`, com `200`;
- `POST /organizacoes/` com corpo `{}` retornou `422` por ausência do campo obrigatório `nome`;
- `POST /filiais` com organização inexistente retornou `404`;
- `POST /filiais` com organização existente retornou `201`; a filial salva apareceu depois em `GET /filiais`, com `200`;
- o Alembic preservou uma URL fictícia codificada e gerou SQL em modo offline, sem acessar o banco;
- a ausência de `DATABASE_URL` manteve o erro esperado, e `alembic current` no banco local confirmou `81819ad65a8a (head)`;
- revisão conceitual concluída: o desenvolvedor distinguiu a validação de entrada antes da rota, o objeto em memória e as operações da sessão para persistir os dados.

Essas verificações foram manuais ou pontuais; ainda não há uma suíte de testes automatizados no projeto.

### Checklist de conclusão

- [x] configurar conexão com PostgreSQL;
- [x] criar sessão de banco;
- [x] criar models SQLAlchemy para `Organizacao` e `Filial`;
- [x] iniciar Alembic;
- [x] criar e aplicar primeira migration;
- [x] criar e consultar organizações e filiais pela API usando persistência real;
- [x] explicar a diferença entre model de banco e schema de API.

### Primeiras entidades persistentes

- Organizacao;
- Filial.

### Critério de conclusão

Criar e consultar organizações e filiais persistidas no PostgreSQL e reproduzir o schema por migração.

### Próximo passo

Fase concluída após validar o fluxo persistente, a criação das tabelas por migração e a revisão conceitual. Próximo aprendizado: usuários, autenticação e permissões.

---

## 🟡 Fase 5 — Usuários, autenticação e permissões

### Objetivo

Construir a base de segurança para a organização em foco e suas filiais.

### Aprender

- autenticação x autorização;
- hash de senha;
- identidade do usuário;
- tokens/sessões conforme decisão futura;
- RBAC;
- vínculo da conta com a organização;
- permissões e isolamento de acesso entre filiais.

### Já praticado

- [x] distinção conceitual entre autenticação e autorização;
- [x] introdução à unicidade de valores no banco com `UNIQUE`;
- [x] distinção entre organização e filial ao definir o alcance de acesso;
- [x] decisões iniciais sobre identificação e alcance das contas registradas na SPEC.
- [x] foco inicial em uma organização com várias filiais definido antes da ampliação para outras empresas.

### Próximo passo

Levantar os dados necessários para as contas da organização em foco e estudar o armazenamento seguro de senhas antes de implementar o modelo de usuário. A questão do mesmo e-mail em organizações diferentes fica para a ampliação futura. As regras de negócio e questões pendentes ficam na SPEC. Nenhuma implementação de autenticação ou autorização foi concluída nesta etapa.

### Critério de conclusão

Na organização em foco, usuários autenticados só acessam as filiais e executam as ações autorizadas para suas contas. Esse critério não comprova que o sistema está pronto para atender várias organizações.

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

O fluxo mínimo deve aparecer antes no marco D4, sem marcar esta fase avançada inteira como concluída.

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

O painel financeiro inicial entra em D5; a revisão avançada desta fase permanece futura. Indicadores por filial e consolidados da organização.

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

## Ampliação futura — múltiplas organizações

Etapa ainda não iniciada, a planejar quando os fluxos principais da primeira versão estiverem estáveis.

Antes de disponibilizar acesso a outras empresas:

- resolver as regras pendentes de contas e login entre organizações na SPEC;
- definir e registrar a estratégia técnica de isolamento na arquitetura;
- testar que uma conta não consegue ler ou alterar dados de outra organização, inclusive ao informar identificadores de registros dessa organização.

Essa validação é requisito para a oferta multi-organização; concluir os fluxos de uma empresa não encerra essa etapa automaticamente.

## Regra de atualização

Quando algo relevante for concluído:

1. atualizar os checkboxes correspondentes;
2. revisar o critério da fase;
3. se o critério foi cumprido, marcar a fase como ✅;
4. marcar a próxima como 🟡;
5. atualizar **Status geral** e **Próximo passo**;
6. refletir a mudança de fase no `README.md`.

As instruções detalhadas para agentes estão em [../AGENTS.md](../AGENTS.md).
