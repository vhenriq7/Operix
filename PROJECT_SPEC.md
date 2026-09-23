# Operix — Project Specification

**Versão:** 0.1  
**Status:** Planejamento inicial  
**Tipo:** SaaS de gestão operacional multi-filial  
**Stack principal:** Python, FastAPI, PostgreSQL e SQL

---

## 1. Visão geral

O **Operix** é um SaaS voltado para empresas com uma ou mais filiais que precisam integrar operação comercial, estoque, conta do cliente, logística e entregas.

O sistema é inspirado em um problema empresarial real, mas deve ser desenvolvido de forma genérica, sem depender de uma empresa específica.

O objetivo inicial não é substituir um ERP completo. O foco será construir um sistema operacional consistente para:

- clientes;
- produtos;
- orçamentos;
- pedidos;
- pagamentos;
- créditos e débitos;
- estoque;
- transferências entre filiais;
- veículos;
- cargas;
- expedição;
- entregas;
- visão consolidada da organização.

O projeto também possui finalidade educacional: servir como ambiente principal para aprender desenvolvimento back-end na prática.

---

## 2. Problema que o sistema resolve

Empresas com múltiplas filiais podem ter dificuldades para acompanhar, de forma integrada:

- vendas realizadas em cada filial;
- clientes compartilhados ou restritos a uma filial;
- créditos e débitos de clientes;
- pedidos atendidos parcialmente;
- estoque individual por filial;
- transferência de produtos entre filiais;
- pedidos vendidos por uma filial e atendidos por outra;
- montagem e conferência de cargas;
- tentativas de entrega;
- indicadores consolidados da organização.

O Operix deve tornar esse fluxo rastreável sem tentar assumir, inicialmente, responsabilidades fiscais, contábeis ou financeiras de um ERP completo.

---

## 3. Público-alvo inicial

Empresas com uma ou mais filiais que realizem vendas e entregas próprias, especialmente operações com:

- materiais de construção;
- ferro e aço;
- telhas;
- distribuição;
- produtos pesados;
- frota própria;
- estoque por filial.

A arquitetura deve permitir expansão futura para outros segmentos sem acoplar o domínio a um tipo específico de produto.

---

## 4. Estrutura organizacional

O sistema deverá suportar múltiplas organizações.

Uma organização poderá possuir várias filiais.

Estrutura conceitual:

```text
Organization
└── Branches
    ├── Users
    ├── Customers
    ├── Products / Stock
    ├── Orders
    ├── Vehicles
    └── Loads
```

O administrador da organização poderá visualizar informações consolidadas de todas as filiais às quais possuir acesso.

---

## 5. Multi-tenancy

O Operix será multi-tenant.

Regras:

1. Cada organização possui seus próprios dados.
2. Dados de uma organização não podem ser acessados por usuários de outra organização.
3. As principais entidades deverão manter vínculo com a organização, direta ou indiretamente.
4. Toda consulta que envolva dados operacionais deverá respeitar o tenant do usuário autenticado.
5. O isolamento entre organizações é requisito de segurança, não apenas de interface.

A estratégia técnica exata de multi-tenancy será definida durante a implementação.

---

## 6. Filiais

Cada organização poderá possuir uma ou mais filiais.

Uma filial poderá possuir:

- usuários;
- vendedores;
- clientes restritos à filial;
- preços;
- estoque;
- pedidos;
- veículos;
- cargas;
- transferências;
- indicadores.

Um pedido poderá ter uma **filial comercial** e, quando necessário, uma **filial operacional** diferente.

---

## 7. Usuários e papéis

Papéis iniciais:

- Administrador
- Gerente
- Vendedor
- Caixa
- Estoque
- Conferente

O sistema deverá evoluir para controle de acesso baseado em papéis e permissões.

Conceito de referência:

**RBAC — Role-Based Access Control**

As permissões exatas devem ser definidas conforme cada módulo for implementado.

---

## 8. Administrador

O administrador da organização deverá poder, futuramente:

- administrar filiais;
- administrar usuários;
- configurar papéis e permissões;
- visualizar todas as filiais autorizadas;
- consultar indicadores consolidados;
- consultar vendas;
- consultar pedidos;
- consultar estoque;
- consultar cargas;
- configurar parâmetros gerais da organização.

---

## 9. Gerente

O gerente deverá possuir acesso operacional e gerencial da filial.

Possíveis responsabilidades:

- consultar pedidos;
- consultar estoque;
- acompanhar cargas;
- consultar vendas;
- visualizar indicadores;
- alterar limite de compra a prazo de clientes;
- acompanhar vendedores;
- aprovar operações específicas quando necessário.

---

## 10. Clientes

O cliente será cadastrado dentro de uma organização e associado inicialmente a uma filial de origem.

Cada cadastro possuirá a configuração:

```text
Compartilhar entre filiais: SIM / NÃO
```

### 10.1 Cliente não compartilhado

Quando o compartilhamento estiver desativado:

- o cadastro operacional fica restrito à filial de origem;
- outras filiais não consultam sua conta comercial;
- créditos não podem ser usados em outras filiais;
- débitos não podem ser recebidos por outras filiais;
- histórico comercial não fica disponível para outras filiais.

### 10.2 Cliente compartilhado

Quando o compartilhamento estiver ativado, filiais autorizadas da mesma organização poderão acessar, conforme permissão:

- cadastro;
- crédito;
- débito;
- histórico financeiro;
- pedidos;
- informações comerciais.

### 10.3 Regra de consistência

Créditos, débitos e histórico comercial só podem circular entre filiais quando o cadastro do cliente estiver compartilhado.

---

## 11. Conta comercial do cliente

O sistema não deverá representar a situação financeira do cliente com um único campo simples de saldo.

Débitos e créditos deverão ser rastreados separadamente.

Exemplo:

```text
Débitos: R$ 1.000
Créditos disponíveis: R$ 300
```

O sistema não deve transformar isso automaticamente em:

```text
Saldo devedor: R$ 700
```

O crédito somente será utilizado quando houver uma ação explícita de aplicação em um pedido ou débito.

Essa regra preserva a rastreabilidade de qual pedido foi pago e qual crédito foi utilizado.

---

## 12. Créditos do cliente

Créditos poderão ser originados por:

- pagamento excedente;
- devolução de mercadoria;
- lançamento manual autorizado;
- outras origens futuras definidas pelo negócio.

Exemplo:

```text
Pedido: R$ 800
Pagamento recebido: R$ 1.000

Pedido = pago
Crédito gerado = R$ 200
```

O crédito deverá possuir histórico de origem, valor utilizado e saldo remanescente.

---

## 13. Crédito por devolução

Quando um cliente devolver mercadoria e a regra comercial determinar geração de crédito, o sistema poderá criar crédito na conta do cliente.

Exemplo:

```text
Valor da devolução: R$ 150
Crédito gerado: R$ 150
```

Esse crédito poderá ser utilizado posteriormente em outro pedido, respeitando as regras de compartilhamento entre filiais.

---

## 14. Crédito não elimina dívida automaticamente

Exemplo:

```text
Pedido #100
Débito: R$ 500

Crédito disponível: R$ 200
```

A situação continua sendo:

```text
Débito: R$ 500
Crédito: R$ 200
```

Somente após uma ação explícita:

```text
Aplicar R$ 200 de crédito no Pedido #100
```

o pedido passa a possuir:

```text
Saldo restante: R$ 300
```

---

## 15. Venda a prazo / "fiado"

Um cliente poderá comprar sem pagar integralmente no momento da venda.

Cada cliente poderá possuir limite configurável de compra a prazo.

Exemplo:

```text
Limite aprovado: R$ 5.000
Valor em aberto: R$ 2.000
Limite disponível: R$ 3.000
```

Quando uma nova compra ultrapassar o limite disponível, o sistema deverá bloquear ou solicitar autorização conforme regra futura.

Inicialmente, alteração de limite deverá ser restrita a gerente ou administrador.

---

## 16. Pagamentos

Um pedido poderá receber:

- pagamento integral;
- pagamento parcial;
- aplicação de crédito;
- combinação de formas autorizadas futuramente.

O sistema deve preservar qual pagamento foi destinado a qual pedido.

Exemplo:

```text
Pedido #1001 -> R$ 500 em aberto
Pedido #1002 -> R$ 300 em aberto

Cliente paga R$ 300 especificamente no Pedido #1002.

Resultado:
Pedido #1001 -> R$ 500 em aberto
Pedido #1002 -> pago
```

Não é permitido perder essa relação transformando tudo em um único saldo geral.

---

## 17. Produtos

Produtos deverão possuir informações globais dentro da organização, como:

- código;
- descrição;
- categoria;
- unidade;
- peso;
- demais atributos futuros.

Preço, disponibilidade e estoque poderão variar por filial.

Estrutura conceitual:

```text
Product
└── BranchProduct
```

Uma associação entre produto e filial poderá conter:

- filial;
- produto;
- preço;
- estoque;
- status ativo/inativo.

---

## 18. Estoque

Cada filial terá estoque próprio.

Exemplo:

```text
Produto: Vergalhão 10 mm

Filial A: 500 unidades
Filial B: 120 unidades
```

O sistema deverá manter histórico de movimentações.

Tipos iniciais de movimentação podem incluir:

- entrada;
- saída por venda;
- devolução;
- transferência enviada;
- transferência recebida;
- ajuste autorizado.

A quantidade atual não deve existir sem possibilidade de rastrear sua origem.

---

## 19. Transferências entre filiais

Uma filial poderá solicitar produtos de outra filial.

Fluxo inicial:

```text
SOLICITADA
↓
APROVADA
↓
RECEBIDA
```

Exemplo:

```text
Origem: Filial A
Destino: Filial B
Produto: Vergalhão 10 mm
Quantidade: 100
```

A regra exata sobre quando o estoque da filial de origem deve ser baixado será definida antes da implementação deste módulo.

Possível evolução futura:

```text
SOLICITADA
APROVADA
EM_TRANSITO
RECEBIDA
```

Não implementar o estado adicional sem revisão desta especificação.

---

## 20. Orçamentos

O vendedor poderá criar um orçamento.

Um orçamento poderá:

- permanecer como orçamento;
- ser alterado;
- expirar futuramente;
- ser convertido em pedido;
- não resultar em venda.

O vendedor responsável deverá permanecer registrado.

---

## 21. Conversão de orçamento em pedido

Quando a venda for confirmada, o caixa deverá poder:

- confirmar o pedido;
- registrar pagamento;
- registrar compra a prazo;
- aplicar crédito;
- definir atendimento;
- confirmar retirada, entrega ou combinação de ambos.

---

## 22. Formas de atendimento

Um pedido poderá possuir:

- retirada;
- entrega;
- retirada + entrega.

A forma de atendimento deverá ser controlada por item e quantidade, e não apenas por pedido inteiro.

---

## 23. Atendimento parcial

Exemplo:

```text
Pedido:
100 barras

20 -> retirada
80 -> entrega
```

As 80 unidades de entrega ainda poderão ser divididas:

```text
Carga #10 -> 50
Carga #15 -> 30
```

O sistema deverá conseguir responder:

```text
Comprado: 100
Retirado: 20
Entregue: 80
Pendente: 0
```

---

## 24. Pedido dividido entre múltiplas cargas

Um pedido poderá participar de várias cargas.

Portanto, um pedido não deverá possuir simplesmente um único identificador de carga.

As quantidades de cada item enviadas em cada carga devem ser registradas individualmente.

Essa regra é essencial para suportar entrega parcial.

---

## 25. Filial comercial e filial operacional

Um pedido poderá ser vendido por uma filial e atendido por outra.

Exemplo:

```text
Filial comercial: Filial A
Vendedor: Carlos

Filial operacional: Filial B
```

Mesmo quando a Filial B separar e entregar:

- a venda continua pertencendo à Filial A;
- o vendedor original permanece associado;
- a comissão permanece vinculada ao vendedor original;
- o histórico deve preservar ambas as filiais.

---

## 26. Comissão

Cada vendedor poderá possuir percentual de comissão configurável.

Inicialmente o sistema deverá permitir visualizar:

- valor bruto vendido;
- desconto total;
- valor líquido vendido;
- percentual de comissão;
- valor previsto de comissão.

A comissão somente será considerada adquirida quando o pedido estiver pago conforme a regra comercial.

Exemplo:

```text
Valor bruto: R$ 10.000
Desconto: R$ 500
Valor vendido: R$ 9.500
Comissão: 2%
Comissão prevista: R$ 190
```

A regra exata de cálculo deve ser validada antes da implementação.

---

## 27. Veículos

Cada veículo pertence inicialmente a uma filial específica.

Dados possíveis:

- placa;
- descrição;
- modelo;
- capacidade de carga;
- status ativo/inativo.

Uma carga deverá normalmente utilizar veículo pertencente à própria filial operacional.

Empréstimo de veículos entre filiais fica fora do escopo inicial.

---

## 28. Carga

Uma carga representa uma viagem programada de um veículo contendo itens de um ou mais pedidos destinados à entrega.

Uma carga deverá possuir, conceitualmente:

- organização;
- filial;
- veículo;
- motorista;
- ajudantes;
- data;
- itens;
- pedidos relacionados;
- peso total;
- capacidade do veículo;
- status;
- observações.

---

## 29. Motorista e ajudantes

Uma carga deverá possuir:

- exatamente um motorista;
- zero ou mais ajudantes.

Motorista e ajudantes devem permanecer registrados no histórico da carga.

---

## 30. Peso e capacidade

Produtos poderão possuir peso.

O sistema deverá permitir calcular:

```text
utilização da carga = peso total / capacidade do veículo
```

Exemplo:

```text
Capacidade: 8.000 kg
Peso da carga: 6.000 kg
Utilização: 75%
```

A regra para bloqueio ou aviso de excesso será definida antes da implementação do módulo.

---

## 31. Status de carga

Estados iniciais sugeridos:

```text
ABERTA
EM_CARREGAMENTO
AGUARDANDO_CONFERENCIA
LIBERADA
EM_ENTREGA
FINALIZADA
```

Os estados poderão ser refinados antes da implementação.

Nenhum estado deve ser adicionado ou removido silenciosamente por assistentes de IA.

---

## 32. Conferência

Antes de uma carga sair, um conferente poderá registrar sua conferência.

O sistema deverá poder armazenar:

- usuário conferente;
- data;
- horário;
- observações.

A conferência precisa fazer parte do histórico da carga.

---

## 33. Expedição

Após a conferência e liberação, uma carga poderá sair para entrega.

A saída deverá ser registrada como evento rastreável.

---

## 34. Tentativas de entrega

Caso uma entrega não possa ser concluída:

- o pedido não deve ser apagado;
- a tentativa anterior não deve ser apagada;
- o motivo deve ser registrado;
- o item ou pedido pendente deverá poder voltar para a fila de entrega;
- ele poderá participar de outra carga posteriormente.

Exemplo:

```text
Pedido #500
Carga #20

Resultado: NÃO ENTREGUE
Motivo: cliente ausente
```

Depois:

```text
Status operacional: AGUARDANDO_ENTREGA
```

---

## 35. Histórico de entregas

O histórico deverá preservar todas as tentativas.

Exemplo:

```text
Tentativa 1
23/09
Carga #20
Cliente ausente

Tentativa 2
24/09
Carga #25
Entregue
```

---

## 36. Dashboard

O administrador deverá futuramente poder visualizar uma visão consolidada da organização.

Exemplo:

```text
Filial A
Pedidos hoje: 120
Entregas pendentes: 25
Cargas abertas: 4

Filial B
Pedidos hoje: 80
Entregas pendentes: 15
Cargas abertas: 2

Total
Pedidos: 200
Entregas pendentes: 40
Cargas abertas: 6
```

---

## 37. Indicadores futuros

Possíveis indicadores:

- vendas por filial;
- vendas por vendedor;
- descontos concedidos;
- comissão prevista;
- comissão adquirida;
- pedidos pendentes;
- entregas pendentes;
- cargas abertas;
- peso transportado;
- estoque;
- clientes inadimplentes.

Esses indicadores não fazem parte das primeiras fases de implementação.

---

## 38. Escopo financeiro

O sistema deverá possuir apenas o financeiro diretamente ligado a cliente e pedido.

### Incluído

- pagamento;
- pagamento parcial;
- débito;
- crédito;
- devolução;
- limite de compra a prazo;
- aplicação de crédito;
- histórico comercial do cliente.

### Fora do escopo inicial

- contas a pagar da empresa;
- folha de pagamento;
- contabilidade;
- DRE;
- SPED;
- impostos;
- emissão fiscal completa;
- conciliação bancária;
- fluxo de caixa empresarial completo.

---

## 39. Escopo inicial do produto

O projeto é grande e deverá ser desenvolvido incrementalmente.

Não tentar construir todos os módulos simultaneamente.

A ordem de desenvolvimento está detalhada no arquivo `LEARNING_ROADMAP.md`.

---

## 40. Stack planejada

### Back-end
Python

### Framework
FastAPI

### Banco de dados
PostgreSQL

### Linguagem de consulta
SQL

### ORM
SQLAlchemy

### Migrações
Alembic

### Validação
Pydantic

### Testes
Pytest

### Versionamento
Git + GitHub

### Infraestrutura
Docker

O provedor de deploy será escolhido futuramente.

---

## 41. Front-end

Front-end não é o foco principal deste projeto.

Nas primeiras fases poderão ser usados:

- Swagger/OpenAPI;
- clientes HTTP;
- interfaces mínimas de teste.

Uma interface gráfica poderá ser criada futuramente para demonstração do produto.

A tecnologia de front-end não está definida.

---

## 42. Objetivo educacional

Este projeto será usado para estudar:

- fundamentos de Python;
- organização de projetos;
- FastAPI;
- HTTP;
- REST;
- JSON;
- SQL;
- PostgreSQL;
- modelagem relacional;
- SQLAlchemy;
- migrações;
- validação;
- autenticação;
- autorização;
- multi-tenancy;
- testes;
- Git;
- Docker;
- deploy;
- arquitetura de software.

A prioridade é compreender o que está sendo construído, e não apenas terminar o produto.

---

## 43. Instruções para assistentes de IA

Este projeto é também um projeto de aprendizagem.

Ao ajudar o desenvolvedor:

1. Explique o conceito antes de apresentar uma implementação.
2. Não implemente funcionalidades inteiras automaticamente sem solicitação explícita.
3. Sempre que possível, dê direção, perguntas ou pistas e permita que o desenvolvedor tente primeiro.
4. Revise o código escrito pelo desenvolvedor.
5. Explique os erros encontrados.
6. Explique por que uma correção funciona.
7. Não substitua automaticamente todo o código quando uma alteração pequena resolver o problema.
8. Introduza novos conceitos quando eles forem necessários para avançar no projeto.
9. Prefira soluções simples e legíveis.
10. Evite abstrações prematuras.
11. Não adicione bibliotecas sem explicar sua finalidade.
12. Explique comandos Git novos antes de pedir que o desenvolvedor os execute.
13. Recomende commits após marcos logicamente completos.
14. Não esconda lógica importante atrás de código gerado se o desenvolvedor deve aprendê-la.
15. Faça perguntas quando uma regra comercial estiver ausente ou ambígua.
16. Não invente requisitos para preencher lacunas.
17. Trate `PROJECT_SPEC.md` como a principal fonte de verdade sobre o produto.
18. Trate `LEARNING_ROADMAP.md` como guia da ordem pedagógica do desenvolvimento.

---

## 44. Fonte de verdade

O arquivo `PROJECT_SPEC.md` é a principal referência de requisitos.

Antes de implementar uma funcionalidade:

1. verificar esta especificação;
2. identificar a regra relevante;
3. discutir qualquer lacuna ou contradição;
4. atualizar a especificação quando uma decisão mudar;
5. somente então implementar.

---

## 45. Regra contra invenção de requisitos

Assistentes não devem assumir comportamento comercial sem confirmação.

Exemplos de perguntas que exigem decisão explícita:

- em qual momento o estoque deve baixar?
- quem pode cancelar pedidos?
- um crédito pode expirar?
- como uma comissão é arredondada?
- o que acontece quando uma carga excede a capacidade?
- quais campos são obrigatórios?
- quem pode aprovar uma transferência?
- o que acontece quando um pagamento é estornado?

Quando esta especificação não responder, perguntar ao desenvolvedor.

---

## 46. Desenvolvimento incremental

Cada funcionalidade deverá seguir, quando possível:

```text
entender o problema
↓
modelar
↓
implementar
↓
testar
↓
revisar
↓
commit
↓
avançar
```

---

## 47. Git

Git deverá ser utilizado desde o início do projeto.

Exemplos de commits futuros:

```text
chore: initialize project
docs: add project specification
feat: add organization model
feat: add branch model
feat: add customer creation endpoint
feat: add order model
test: add customer tests
fix: prevent automatic credit compensation
```

Commits devem representar mudanças pequenas e coerentes.

---

## 48. Princípio de arquitetura

O projeto deve crescer conforme o conhecimento e as necessidades reais crescem.

Prioridade:

```text
1. simples
2. correto
3. compreensível
4. testável
5. melhorado
6. refatorado
7. otimizado
```

Evitar desenhar uma arquitetura excessivamente complexa antes de existir uma necessidade concreta.
