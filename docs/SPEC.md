# Operix — Especificação do produto

**Versão:** 0.2  
**Status:** requisitos iniciais em evolução  
**Tipo:** SaaS de gestão operacional multi-filial

Este documento contém **regras de negócio e requisitos do produto**. Stack e decisões técnicas ficam em [ARCHITECTURE.md](ARCHITECTURE.md). Ordem de implementação fica em [ROADMAP.md](ROADMAP.md).

## 1. Visão do produto

O Operix é um SaaS para empresas com uma ou mais filiais que precisam integrar:

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

O sistema é inspirado em uma operação real de venda e distribuição de ferro, aço, telhas e materiais relacionados, mas deve permanecer genérico o suficiente para outros segmentos.

Referência operacional inicial: aproximadamente **200 pedidos por dia**, incluindo pedidos originados presencialmente, por WhatsApp e por telefone. Isso é uma referência de escala, não um SLA.

## 2. Limite do produto

O Operix não pretende inicialmente substituir um ERP fiscal/contábil completo.

O foco é a operação comercial, conta do cliente, estoque e logística.

### Incluído

- cadastro de organização e filiais;
- usuários e permissões;
- clientes;
- produtos e preço/estoque por filial;
- orçamento e pedido;
- atendimento por retirada/entrega;
- pagamentos ligados a pedidos;
- crédito e débito do cliente;
- venda a prazo;
- devolução;
- comissão;
- transferências de estoque;
- veículos, cargas, conferência e entregas;
- dashboards operacionais.

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

## 3. Organização e filiais

O SaaS suporta múltiplas organizações.

Uma organização pode possuir várias filiais.

Exemplo conceitual:

```text
Organization
├── Branch A
├── Branch B
└── Branch C
```

O administrador da organização pode ter visão consolidada das filiais autorizadas.

Dados de uma organização nunca devem ser visíveis para outra organização.

## 4. Papéis de usuário

Papéis iniciais:

- Administrador;
- Gerente;
- Vendedor;
- Caixa;
- Estoque;
- Conferente.

As permissões exatas serão refinadas conforme os módulos forem implementados.

### Administrador

Deve poder, de acordo com permissões:

- administrar filiais;
- administrar usuários;
- visualizar várias filiais;
- consultar indicadores consolidados;
- consultar vendas, pedidos, estoque e cargas;
- configurar parâmetros da organização.

### Gerente

Deve poder, conforme permissão:

- acompanhar operação da filial;
- consultar vendas, pedidos, estoque e cargas;
- visualizar indicadores;
- alterar limite de compra a prazo;
- acompanhar vendedores;
- aprovar operações específicas quando a regra exigir.

## 5. Clientes e compartilhamento entre filiais

O cliente pertence à organização e tem uma filial de origem.

Cada cadastro possui uma opção de compartilhamento entre filiais.

### Cliente não compartilhado

Quando o compartilhamento estiver desativado:

- outras filiais não acessam sua conta comercial;
- crédito não pode ser usado em outra filial;
- débito não pode ser recebido em outra filial;
- histórico comercial fica restrito à filial de origem.

### Cliente compartilhado

Quando o compartilhamento estiver ativado, filiais autorizadas da mesma organização podem consultar, conforme permissão:

- cadastro;
- crédito;
- débito;
- histórico financeiro/comercial;
- pedidos.

**Regra:** créditos, débitos e histórico comercial só circulam entre filiais quando o cliente estiver compartilhado.

## 6. Conta comercial do cliente

O sistema não deve representar tudo em um único campo `saldo`.

Débitos e créditos são rastreados separadamente.

Exemplo:

```text
Débitos: R$ 1.000
Crédito disponível: R$ 300
```

Isso não vira automaticamente uma dívida líquida de R$ 700.

Um crédito só reduz uma obrigação quando for explicitamente aplicado.

### Pedido específico

Se o cliente deve:

```text
Pedido #1001: R$ 500
Pedido #1002: R$ 300
```

e paga R$ 300 especificamente no pedido #1002:

```text
Pedido #1001: R$ 500 em aberto
Pedido #1002: pago
```

A relação entre pagamento e pedido deve ser preservada.

## 7. Créditos

Crédito pode ser originado por:

- pagamento excedente;
- devolução;
- lançamento manual autorizado;
- outras origens futuras definidas explicitamente.

Exemplo:

```text
Pedido: R$ 800
Pagamento: R$ 1.000

Pedido: pago
Crédito gerado: R$ 200
```

O sistema deve preservar origem, valor utilizado e saldo remanescente do crédito.

Crédito não elimina dívida automaticamente.

## 8. Venda a prazo

Clientes podem comprar sem pagamento integral imediato.

Cada cliente pode possuir limite configurável de compra a prazo.

Exemplo:

```text
Limite aprovado: R$ 5.000
Em aberto: R$ 2.000
Disponível: R$ 3.000
```

Quando a compra ultrapassar o limite, o sistema deverá bloquear ou exigir autorização conforme regra a ser refinada.

Inicialmente, alteração de limite é responsabilidade de gerente ou administrador.

## 9. Pagamentos

Um pedido pode receber:

- pagamento integral;
- pagamento parcial;
- aplicação de crédito;
- combinação de formas autorizadas futuramente.

O pagamento deve permanecer vinculado aos pedidos/obrigações aos quais foi destinado.

## 10. Devoluções

Uma devolução pode, conforme a regra do caso:

- devolver mercadoria ao estoque;
- gerar crédito na conta do cliente;
- registrar histórico.

As regras detalhadas de devolução deverão ser validadas antes da implementação do módulo.

## 11. Produtos, preço e estoque

Produto possui dados gerais da organização, como:

- código;
- descrição;
- categoria;
- unidade;
- peso;
- demais atributos futuros.

Preço e estoque podem variar por filial.

Conceito:

```text
Product
└── configuração por Branch
    ├── preço
    ├── estoque
    └── ativo/inativo
```

O mesmo produto não precisa ser duplicado apenas porque possui preços diferentes em filiais diferentes.

## 12. Movimentação de estoque

Cada filial possui estoque próprio.

O sistema deve manter histórico de movimentações, incluindo futuramente:

- entrada;
- saída;
- devolução;
- transferência enviada;
- transferência recebida;
- ajuste autorizado.

A quantidade atual deve ser rastreável a partir de eventos/movimentações consistentes.

## 13. Transferências entre filiais

Uma filial pode solicitar produtos de outra.

Fluxo inicial definido:

```text
SOLICITADA
→ APROVADA
→ RECEBIDA
```

Exemplo:

```text
Origem: Filial A
Destino: Filial B
Produto: Vergalhão 10 mm
Quantidade: 100
```

**Decisão ainda aberta:** em qual estado o estoque sai da origem e em qual momento entra no destino.

Um estado futuro `EM_TRANSITO` pode ser considerado, mas não deve ser implementado sem revisão desta especificação.

## 14. Orçamentos

O vendedor cria o orçamento.

Um orçamento pode:

- permanecer apenas como orçamento;
- ser alterado;
- não virar venda;
- ser convertido em pedido.

O vendedor responsável deve permanecer registrado.

## 15. Confirmação de pedido

O caixa confirma a venda e deve poder registrar:

- se o atendimento será retirada, entrega ou ambos;
- pagamento;
- compra a prazo;
- aplicação de crédito;
- demais operações financeiras ligadas ao cliente dentro do escopo definido.

## 16. Forma de atendimento

Um pedido pode ser:

- retirada;
- entrega;
- retirada + entrega.

A forma de atendimento é controlada por **item e quantidade**, não apenas por pedido inteiro.

Exemplo:

```text
Pedido: 100 barras

20 retiradas pelo cliente
80 destinadas à entrega
```

## 17. Atendimento e entrega parcial

Um item pode ser atendido em múltiplos momentos.

Exemplo:

```text
100 barras compradas
20 retiradas
50 entregues na carga #10
30 entregues na carga #15
```

O sistema deve conseguir informar:

- quantidade comprada;
- retirada;
- entregue;
- pendente.

Nenhuma quantidade atendida pode ultrapassar a quantidade vendida.

## 18. Pedido em múltiplas cargas

Um pedido pode participar de várias cargas.

Logo, um pedido não pode ser modelado simplesmente com um único `load_id`.

A carga precisa registrar quais itens e quais quantidades de cada pedido estão naquela viagem.

## 19. Filial comercial e filial operacional

Um pedido pode ser vendido por uma filial e atendido por outra.

Exemplo:

```text
Filial comercial: Santa Margarida
Vendedor: Carlos
Filial operacional/entrega: Divino
```

Mesmo que outra filial separe ou entregue:

- a venda continua pertencendo à filial comercial;
- o vendedor original continua vinculado;
- a comissão continua vinculada ao vendedor original;
- o histórico preserva ambas as filiais.

## 20. Comissão

Cada vendedor pode possuir percentual configurável de comissão.

O sistema deve permitir visualizar:

- valor bruto vendido;
- desconto total;
- valor líquido vendido;
- percentual de comissão;
- comissão prevista.

A comissão só é considerada adquirida quando o pedido estiver pago.

A fórmula exata e regras de arredondamento deverão ser validadas antes da implementação.

## 21. Veículos

Cada veículo pertence inicialmente a uma filial específica.

Dados previstos:

- placa;
- descrição/modelo;
- capacidade;
- ativo/inativo.

Empréstimo de veículo entre filiais está fora do escopo inicial.

## 22. Cargas

Uma carga representa **uma viagem de um veículo contendo itens de um ou mais pedidos destinados à entrega**.

Uma carga deverá registrar, conceitualmente:

- filial;
- veículo;
- motorista;
- ajudantes;
- data;
- itens e quantidades;
- pedidos relacionados;
- peso;
- capacidade;
- status;
- observações.

Uma carga possui um motorista e zero ou mais ajudantes.

## 23. Peso e capacidade

Produtos podem possuir peso.

O sistema deve conseguir calcular:

```text
utilização = peso da carga / capacidade do veículo
```

A política de bloqueio ou aviso quando houver excesso ainda será definida.

## 24. Status da carga

Estados iniciais sugeridos:

```text
ABERTA
EM_CARREGAMENTO
AGUARDANDO_CONFERENCIA
LIBERADA
EM_ENTREGA
FINALIZADA
```

Esses estados podem ser refinados antes da implementação.

Nenhum agente deve adicionar/remover estado silenciosamente.

## 25. Conferência e expedição

Antes da saída, um conferente deve poder registrar a conferência.

Registrar:

- usuário;
- data/hora;
- observações quando aplicável.

Após conferência/liberação, a saída para entrega deve ficar registrada no histórico.

## 26. Tentativas de entrega

Se a entrega falhar:

- não apagar a tentativa;
- registrar motivo;
- manter o que ficou pendente;
- permitir inclusão em carga futura.

Exemplo:

```text
Carga #20
Pedido #500
Resultado: não entregue
Motivo: cliente ausente
```

Depois o pedido/quantidade pendente pode voltar para `AGUARDANDO_ENTREGA` e entrar em nova carga.

O histórico deve preservar todas as tentativas.

## 27. Dashboards

O administrador deve poder visualizar visão por filial e consolidada.

Indicadores possíveis:

- vendas;
- vendas por vendedor;
- descontos;
- comissão prevista/adquirida;
- pedidos;
- entregas pendentes;
- cargas;
- peso transportado;
- estoque;
- inadimplência.

Os indicadores exatos serão priorizados quando o módulo for iniciado.

## 28. Regras transversais

- operações relevantes devem ser rastreáveis;
- alterações de dinheiro, crédito, estoque e entrega não devem apagar histórico necessário;
- a origem comercial de um pedido deve ser preservada;
- nenhuma organização pode acessar dados de outra;
- regras em aberto não devem ser preenchidas por suposição.

## 29. Questões de negócio ainda abertas

Antes dos módulos correspondentes, decidir explicitamente:

- momento exato da movimentação de estoque em transferências;
- quem pode cancelar pedido e quais efeitos isso gera;
- se crédito expira;
- regras completas de estorno;
- fórmula/arredondamento definitivo de comissão;
- comportamento quando uma carga excede capacidade;
- detalhes finais do fluxo de devolução;
- autorização quando compra ultrapassa limite.

Quando uma decisão for tomada, atualizar este documento antes ou junto da implementação.
