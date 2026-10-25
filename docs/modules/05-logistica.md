# Operix — cargas, frota e entregas

**Estado:** requisitos planejados; entrega, separação e recebimento são operações distintas.

### 12. Cargas, frota e entrega parcial
- Cadastrar frota, caminhões/veículos, motorista e ajudantes, com filial responsável e gestão central conforme autorização.
- Montador cria carga do dia identificada como "Carga 1", "Carga 2" etc., escolhe caminhão, motorista, ajudantes e pedidos por código ou nome; visualiza valor total de pedidos da carga.
- Selecionar **quais produtos e quais quantidades** vão embarcar; o que cliente retirou ou solicitou para depois não entra na carga atual.
- Imprimir **romaneio** com itens, quantidades, clientes, pedidos e endereços; origem da carga e conferência ficam auditáveis.
- Na volta, fechar resultado **pedido por pedido**: entregue, parcial, não entregue com motivo; pendência gera nova folha a imprimir e volta para mesa do montador, **sem data obrigatória**.
- Mercadoria não entregue pode voltar ao depósito **ou permanecer no caminhão**. Preservar onde ela está; não duplicar quantidades em cargas/estoques.
- Uma compra pode estar em várias cargas e uma carga pode conter várias compras; controle é por item/quantidade, não apenas por pedido.

### 13. Recebimentos com motorista
- Motorista pode cobrar na entrega, mas deve **entregar integralmente ao caixa** o dinheiro recebido, sem usar parte para combustível/despesas.
- Caixa confere **pedido por pedido** o que cliente pagou, o que motorista informou e o que entregou efetivamente.
- O dinheiro em poder do motorista não entra automaticamente no caixa até a prestação de contas.
- Se cliente pagou menos, o restante é dívida do cliente. Se cliente pagou tudo mas motorista devolveu menos, a diferença é de **prestação de contas**, não inadimplência do cliente.
- Lançar somente o valor efetivamente recebido/confirmado, preservando a divergência para a administração resolver pessoalmente.
