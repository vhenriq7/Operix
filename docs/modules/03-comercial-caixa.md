# Operix — vendas, pedidos e caixa

**Estado:** requisitos planejados; os fluxos comerciais/financeiros completos não estão implementados.

### 4. Orçamento, negociação e pedido em aberto
- Vendedor escolhe cliente e produtos, edita quantidade, unidade, preço unitário e observação de cada linha; desconto por item em reais ou percentual; desconto geral sobre o pedido.
- Preservar preço de tabela, preço efetivamente negociado, descontos por item e desconto geral, além de quem alterou e quando. Definir base da porcentagem efetiva para impedir que reduzir preço manualmente esconda um desconto.
- Limiar de **alerta** configurável por administração (16% é exemplo). Ao ultrapassar, exibir aviso, permitir clicar OK e salvar, registrar ocorrência e notificar gestor pelo próprio sistema. Não impor bloqueio ou senha: a regra discutida é alerta sem impedir orçamento.
- Consultar/aprovar conforme fluxo, **clonar orçamento** em novo identificador sem copiar pagamentos, converter em pedido aberto. Pedido aberto não é comprovante de pagamento.
- Definir por item/quantidade retirada imediata, entrega, retirada posterior ou parte para depois.
- **Imprimir após conversão:** documento com código/número, data, cliente, telefone, endereço de entrega, itens/códigos/unidades/quantidades/valores unitários/totais, descontos, forma e estado de pagamento, instruções, observações e campo para assinatura do cliente. A impressão pode ir para a mesa do montador de carga, sem liquidar nem entregar o pedido.

### 5. Pedido, valores recebidos e crédito do cliente
- O mesmo pedido pode ser recebido parcialmente, por **vários meios** (ex.: R$ 300 Pix + R$ 200 cartão + R$ 500 fiado), mantendo saldos por obrigação e evento de recebimento.
- Meios previstos: dinheiro, cartão crédito, cartão débito, Pix QR, Pix comprovante sujeito a conferência, cheque, boleto, crédito livre aplicado explicitamente e outros configuráveis.
- **Três grandezas independentes:** valor vendido, dinheiro efetivamente recebido e situação logística/entrega. Uma venda paga pode permanecer sem entrega e uma entrega concluída pode continuar fiada.
- **Crédito livre:** cliente depositou previamente dinheiro sem vincular a pedido; permanece separado de dívida até aplicação manual e autorizada.
- **Adiantamento vinculado:** pagamento antecipado associado exclusivamente a pedido ainda a entregar/retirar; não usar automaticamente em outras vendas.
- Exemplo obrigatório para testes: cliente com R$ 2.000 de crédito livre, R$ 500 já pagos em pedido separado e R$ 90 de nova dívida; nenhuma compensação automática.
- Registrar trilha de toda aplicação, estorno e repasse para outra obrigação. Crédito aplicado não vira nova entrada física no caixa.

### 6. Cancelamentos, devoluções e ajustes
- Cancelamento total ou **parcial por item/quantidade**: se seis unidades foram entregues e quatro canceladas, conservar seis e cancelar somente quatro.
- Para parcela elegível à devolução financeira, o cliente pode optar por reembolso via Pix/dinheiro/cartão conforme meios permitidos, ou conversão em crédito livre futuro.
- Diferenciar cancelamento do pedido, estorno do recebimento, devolução de mercadoria e operação fiscal. Preservar histórico, autorização e efeito no estoque.
- Se pedido já foi parcialmente entregue, não fingir que houve retorno automático de estoque; seguir processo de devolução.

### 7. Caixa operacional
- Abertura por funcionário e filial, com **valor inicial em dinheiro** e histórico da sessão.
- Tela de valores por meio: dinheiro, cartão crédito/débito, cheque (quantidade e valor), Pix QR, Pix comprovante, boleto, outros. Separar lançado, confirmado e a compensar quando aplicável.
- Consultas por hoje, ontem, 7 dias, intervalo, funcionário, filial e pedido; possibilidade de consultar/reabrir caixas anteriores com autorização e trilha de auditoria.
- Movimentações próprias: **sangria** (retirada de dinheiro físico) e **suprimento** (entrada de troco/dinheiro), com justificativa; não lançar como venda.
- Contagem de moedas R$ 0,05, 0,10, 0,25, 0,50 e 1,00; cédulas R$ 2, 5, 10, 20, 50, 100 e 200; quantidade × denominação; diferença entre contado e esperado.
- Fechamento por pessoa que pode ser diferente de quem abriu, incluindo horário, conferência por modalidade, sobra/falta e responsável.
- **Caixa da loja não é conta bancária da empresa.** Operações do financeiro não devem manipular automaticamente o saldo físico da loja.

#### Crédito e comissão

- Cada obrigação do cliente é vinculada a pedido e valor. Crédito livre não quita débito automaticamente; a aplicação exige evento explícito e rastreável.
- Compra a prazo pode observar limite por cliente; a decisão sobre bloqueio ou aprovação ao exceder o limite permanece aberta.
- Comissão de venda mantém vínculo com vendedor e filial comercial, mesmo quando outra filial atende o pedido. Comissão prevista e adquirida são distintas; a comissão adquirida pressupõe pedido pago. Fórmula final e arredondamento dependem de validação.
