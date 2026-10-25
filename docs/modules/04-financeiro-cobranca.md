# Operix — financeiro e cobrança

**Estado:** requisitos planejados; operação bancária/fiscal exige validação e homologação.

### 8. Fiados e cobrança recorrente
- Fiado exige **vencimento original obrigatório** no pedido/obrigação. Relatório diário imprimível com código do cliente, nome, telefone, pedido, valor, vencimento; listar apenas quando vencer ou já estiver vencido.
- Atendimento de cobrança: quem ligou, data, resultado, observação e **próxima data de cobrança** agendada.
- Caso WP: vencimento original 23/10, contato em 23/10, nova cobrança combinada para 28/10. A dívida permanece **vencida desde 23/10**; sai apenas da fila de contatos até 28/10.
- Relatórios separados de inadimplência e produtividade da cobrança; promessa de pagamento não é recebimento.

### 9. Boleto e parcelamento
- O operador autorizado cria modelos de vencimento **livres e reutilizáveis** para toda a organização: por exemplo, 15/30, 30/60, 15/30/45/60, 15/40/65; não limitar a lista a presets fixos.
- Seleção calcula vencimentos a partir de data-base configurada, número de parcelas e valores, ajustando centavos na última parcela para a soma fechar.
- Permitir mudar vencimentos em um pedido sem reescrever o modelo global, conforme permissões.
- Imprimir boleto associado ao pedido/entrega quando já houver boleto **real emitido**. Gerar apenas cronograma não equivale a emissão bancária.
- Controlar vencido, a vencer, emitido, compensado, cancelado e falhas. Emissão bancária exige provedor/conta autorizada, regras de dias úteis, homologação e confirmação confiável antes de baixa.

### 10. Cheques e custódia
- Registrar cliente/código, pedido, filial, banco, número do cheque, favorecido, valor, data de emissão declarada, data de recebimento, data prevista de depósito/pré-datado, depósito efetivo, compensação, conta bancária destino, funcionário lançador, observações e ocorrências.
- Acompanhar em carteira, a depositar, depositado, compensado, devolvido, **repassado a terceiros**; quem está com cheque, data de cada evento e dias faltantes.
- Relatório de cheques para depositar hoje/próximos dias, vencidos, repassados, depositados, devolvidos e compensados, por filial e consolidado.
- Cheque repassado a fornecedor mantém elo com o contas a pagar; repassar cheque e compensá-lo não são a mesma coisa.
- Cheque ainda em carteira ou não compensado não pode ser tratado como dinheiro bancário disponível sem critério.

### 11. Financeiro central e contas a pagar
- Cadastrar conta de fornecedor: fornecedor, documento, descrição, categoria, filial responsável, valor, vencimento, parcelas, valor pago, data de pagamento e saldo.
- Previsão do que vence hoje, na semana e no mês, e valores atrasados; relatórios por filial e consolidados.
- Pagamento não precisa passar pelo **caixa físico**: selecionar **conta bancária cadastrada** da empresa, forma Pix/transferência etc. ou **cheque de terceiro recebido anteriormente**, ou combinar fontes.
- A conta bancária que pagou pode ser central, embora a despesa seja de uma filial. Separar conta pagadora, obrigação e comprovante.
- Projeção de fluxo de caixa diferencia entradas/saídas esperadas e disponibilidades já confirmadas. Não considerar programado = pago.
