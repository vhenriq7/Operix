# Operix — Mapa de módulos e jornadas de negócio

**Estado:** levantamento de requisitos, ainda não implementados salvo indicação no README/ROADMAP.
**Primeiro destinatário:** uma empresa de três filiais, controladas por uma administração central. Uma filial pode ser a matriz; não criar uma quarta unidade artificial.
**Meta atual:** portfólio com demonstração funcional operando em base de dados fictícios, sem substituir os sistemas da empresa.
**Meta condicionada:** somente se a direção aprovar, passar por homologação técnica, comercial, segurança, fiscalização pertinente, implantação e suporte até produção.

Este documento detalha as jornadas que nasceram de relatos da operação real. A SPEC mantém as regras de produto e deve ser atualizada sempre que alguma dúvida for resolvida; o ROADMAP define o que implementar primeiro. O texto abaixo expressa principalmente **requisitos planejados** e não funcionalidades existentes.

## 1. Identidade, filiais e equipe
- Administrador principal cadastra/gerencia filiais, usuários, funções e permissões de ação.
- Usuário vinculado à organização e a uma ou mais filiais conforme função. Dono e financeiro podem consultar consolidação das três filiais quando autorizados.
- Perfis de referência: dono, administrador, financeiro, gerente, vendedor, caixa, estoque, conferente e logística. Permissões específicas são configuráveis e devem ser validadas no servidor.
- Abrir, movimentar e fechar caixa registra o usuário real em cada evento; **uma pessoa pode abrir e outra fechar**.
- Configurações comuns, como modelos de parcelamento de boletos, ficam disponíveis para todas as filiais da mesma organização.

## 2. Cliente PF/PJ e ficha completa
- Tipo PF ou PJ; CPF ou CNPJ inicialmente obrigatórios conforme tipo; nome/razão social, nome fantasia se PJ e pessoa de contato quando houver.
- Código de cadastro, e-mail, múltiplos telefones com etiquetas (WhatsApp, celular, comercial, residencial), principal e observações.
- País, CEP, UF, cidade, bairro, logradouro, número, complemento e referência. Endereços de cobrança e entrega podem ser diferentes. Consulta automática do CEP é opcional e editável.
- Visão resumida: valores em aberto, atrasados, crédito livre, adiantamentos para pedidos específicos, limite de fiado, data da dívida mais antiga, último pagamento e próximo contato.
- Abas/histórico de orçamentos, pedidos, pagamentos, créditos, estornos, entregas, cobranças e transações, filtráveis por data e filial respeitando regras de compartilhamento.
- Confirmar posteriormente política de duplicidade, privacidade, CPF/CNPJ e dados mínimos quando o cliente não tem documento.

## 3. Cadastro de produtos e estoque
- Produto central: código interno único, nome, descrição, categoria, marca, unidade (unidade, kg etc.), código de barras quando houver, peso líquido, peso bruto, custo de referência e dados tributários pertinentes.
- Por filial: preço de venda, estoque, estoque mínimo e histórico de entradas, saídas, transferências, ajustes, devoluções e reservas.
- A mesma mercadoria pode ter **preços e saldos distintos por filial** sem duplicar o cadastro geral.
- Não atribuir ao produto a situação de pagamento/entrega de uma venda: esses são dados do pedido.

## 4. Orçamento, negociação e pedido em aberto
- Vendedor escolhe cliente e produtos, edita quantidade, unidade, preço unitário e observação de cada linha; desconto por item em reais ou percentual; desconto geral sobre o pedido.
- Preservar preço de tabela, preço efetivamente negociado, descontos por item e desconto geral, além de quem alterou e quando. Definir base da porcentagem efetiva para impedir que reduzir preço manualmente esconda um desconto.
- Limiar de **alerta** configurável por administração (16% é exemplo). Ao ultrapassar, exibir aviso, permitir clicar OK e salvar, registrar ocorrência e notificar gestor pelo próprio sistema. Não impor bloqueio ou senha: a regra discutida é alerta sem impedir orçamento.
- Consultar/aprovar conforme fluxo, **clonar orçamento** em novo identificador sem copiar pagamentos, converter em pedido aberto. Pedido aberto não é comprovante de pagamento.
- Definir por item/quantidade retirada imediata, entrega, retirada posterior ou parte para depois.
- **Imprimir após conversão:** documento com código/número, data, cliente, telefone, endereço de entrega, itens/códigos/unidades/quantidades/valores unitários/totais, descontos, forma e estado de pagamento, instruções, observações e campo para assinatura do cliente. A impressão pode ir para a mesa do montador de carga, sem liquidar nem entregar o pedido.

## 5. Pedido, valores recebidos e crédito do cliente
- O mesmo pedido pode ser recebido parcialmente, por **vários meios** (ex.: R$ 300 Pix + R$ 200 cartão + R$ 500 fiado), mantendo saldos por obrigação e evento de recebimento.
- Meios previstos: dinheiro, cartão crédito, cartão débito, Pix QR, Pix comprovante sujeito a conferência, cheque, boleto, crédito livre aplicado explicitamente e outros configuráveis.
- **Três grandezas independentes:** valor vendido, dinheiro efetivamente recebido e situação logística/entrega. Uma venda paga pode permanecer sem entrega e uma entrega concluída pode continuar fiada.
- **Crédito livre:** cliente depositou previamente dinheiro sem vincular a pedido; permanece separado de dívida até aplicação manual e autorizada.
- **Adiantamento vinculado:** pagamento antecipado associado exclusivamente a pedido ainda a entregar/retirar; não usar automaticamente em outras vendas.
- Exemplo obrigatório para testes: cliente com R$ 2.000 de crédito livre, R$ 500 já pagos em pedido separado e R$ 90 de nova dívida; nenhuma compensação automática.
- Registrar trilha de toda aplicação, estorno e repasse para outra obrigação. Crédito aplicado não vira nova entrada física no caixa.

## 6. Cancelamentos, devoluções e ajustes
- Cancelamento total ou **parcial por item/quantidade**: se seis unidades foram entregues e quatro canceladas, conservar seis e cancelar somente quatro.
- Para parcela elegível à devolução financeira, o cliente pode optar por reembolso via Pix/dinheiro/cartão conforme meios permitidos, ou conversão em crédito livre futuro.
- Diferenciar cancelamento do pedido, estorno do recebimento, devolução de mercadoria e operação fiscal. Preservar histórico, autorização e efeito no estoque.
- Se pedido já foi parcialmente entregue, não fingir que houve retorno automático de estoque; seguir processo de devolução.

## 7. Caixa operacional
- Abertura por funcionário e filial, com **valor inicial em dinheiro** e histórico da sessão.
- Tela de valores por meio: dinheiro, cartão crédito/débito, cheque (quantidade e valor), Pix QR, Pix comprovante, boleto, outros. Separar lançado, confirmado e a compensar quando aplicável.
- Consultas por hoje, ontem, 7 dias, intervalo, funcionário, filial e pedido; possibilidade de consultar/reabrir caixas anteriores com autorização e trilha de auditoria.
- Movimentações próprias: **sangria** (retirada de dinheiro físico) e **suprimento** (entrada de troco/dinheiro), com justificativa; não lançar como venda.
- Contagem de moedas R$ 0,05, 0,10, 0,25, 0,50 e 1,00; cédulas R$ 2, 5, 10, 20, 50, 100 e 200; quantidade × denominação; diferença entre contado e esperado.
- Fechamento por pessoa que pode ser diferente de quem abriu, incluindo horário, conferência por modalidade, sobra/falta e responsável.
- **Caixa da loja não é conta bancária da empresa.** Operações do financeiro não devem manipular automaticamente o saldo físico da loja.

## 8. Fiados e cobrança recorrente
- Fiado exige **vencimento original obrigatório** no pedido/obrigação. Relatório diário imprimível com código do cliente, nome, telefone, pedido, valor, vencimento; listar apenas quando vencer ou já estiver vencido.
- Atendimento de cobrança: quem ligou, data, resultado, observação e **próxima data de cobrança** agendada.
- Caso WP: vencimento original 23/10, contato em 23/10, nova cobrança combinada para 28/10. A dívida permanece **vencida desde 23/10**; sai apenas da fila de contatos até 28/10.
- Relatórios separados de inadimplência e produtividade da cobrança; promessa de pagamento não é recebimento.

## 9. Boleto e parcelamento
- O operador autorizado cria modelos de vencimento **livres e reutilizáveis** para toda a organização: por exemplo, 15/30, 30/60, 15/30/45/60, 15/40/65; não limitar a lista a presets fixos.
- Seleção calcula vencimentos a partir de data-base configurada, número de parcelas e valores, ajustando centavos na última parcela para a soma fechar.
- Permitir mudar vencimentos em um pedido sem reescrever o modelo global, conforme permissões.
- Imprimir boleto associado ao pedido/entrega quando já houver boleto **real emitido**. Gerar apenas cronograma não equivale a emissão bancária.
- Controlar vencido, a vencer, emitido, compensado, cancelado e falhas. Emissão bancária exige provedor/conta autorizada, regras de dias úteis, homologação e confirmação confiável antes de baixa.

## 10. Cheques e custódia
- Registrar cliente/código, pedido, filial, banco, número do cheque, favorecido, valor, data de emissão declarada, data de recebimento, data prevista de depósito/pré-datado, depósito efetivo, compensação, conta bancária destino, funcionário lançador, observações e ocorrências.
- Acompanhar em carteira, a depositar, depositado, compensado, devolvido, **repassado a terceiros**; quem está com cheque, data de cada evento e dias faltantes.
- Relatório de cheques para depositar hoje/próximos dias, vencidos, repassados, depositados, devolvidos e compensados, por filial e consolidado.
- Cheque repassado a fornecedor mantém elo com o contas a pagar; repassar cheque e compensá-lo não são a mesma coisa.
- Cheque ainda em carteira ou não compensado não pode ser tratado como dinheiro bancário disponível sem critério.

## 11. Financeiro central e contas a pagar
- Cadastrar conta de fornecedor: fornecedor, documento, descrição, categoria, filial responsável, valor, vencimento, parcelas, valor pago, data de pagamento e saldo.
- Previsão do que vence hoje, na semana e no mês, e valores atrasados; relatórios por filial e consolidados.
- Pagamento não precisa passar pelo **caixa físico**: selecionar **conta bancária cadastrada** da empresa, forma Pix/transferência etc. ou **cheque de terceiro recebido anteriormente**, ou combinar fontes.
- A conta bancária que pagou pode ser central, embora a despesa seja de uma filial. Separar conta pagadora, obrigação e comprovante.
- Projeção de fluxo de caixa diferencia entradas/saídas esperadas e disponibilidades já confirmadas. Não considerar programado = pago.

## 12. Cargas, frota e entrega parcial
- Cadastrar frota, caminhões/veículos, motorista e ajudantes, com filial responsável e gestão central conforme autorização.
- Montador cria carga do dia identificada como "Carga 1", "Carga 2" etc., escolhe caminhão, motorista, ajudantes e pedidos por código ou nome; visualiza valor total de pedidos da carga.
- Selecionar **quais produtos e quais quantidades** vão embarcar; o que cliente retirou ou solicitou para depois não entra na carga atual.
- Imprimir **romaneio** com itens, quantidades, clientes, pedidos e endereços; origem da carga e conferência ficam auditáveis.
- Na volta, fechar resultado **pedido por pedido**: entregue, parcial, não entregue com motivo; pendência gera nova folha a imprimir e volta para mesa do montador, **sem data obrigatória**.
- Mercadoria não entregue pode voltar ao depósito **ou permanecer no caminhão**. Preservar onde ela está; não duplicar quantidades em cargas/estoques.
- Uma compra pode estar em várias cargas e uma carga pode conter várias compras; controle é por item/quantidade, não apenas por pedido.

## 13. Recebimentos com motorista
- Motorista pode cobrar na entrega, mas deve **entregar integralmente ao caixa** o dinheiro recebido, sem usar parte para combustível/despesas.
- Caixa confere **pedido por pedido** o que cliente pagou, o que motorista informou e o que entregou efetivamente.
- O dinheiro em poder do motorista não entra automaticamente no caixa até a prestação de contas.
- Se cliente pagou menos, o restante é dívida do cliente. Se cliente pagou tudo mas motorista devolveu menos, a diferença é de **prestação de contas**, não inadimplência do cliente.
- Lançar somente o valor efetivamente recebido/confirmado, preservando a divergência para a administração resolver pessoalmente.

## 14. BI, gerência e documentos
- Painel da patroa/patrão: todas as três filiais juntas ou uma por vez, conforme permissão e período.
- Valores de vendas, recebidos, caixa físico, fiado a vencer/vencido, créditos livres, adiantamentos vinculados, boleto, cheques e contas a pagar **em blocos separados**.
- Relatório por **cada carga**: dia, número da carga, caminhão, motorista, ajudantes, pedidos, quais foram entregues/parciais/não entregues, motivo, pendências, situação financeira e montante recebido pelo motorista.
- Resumo diário de cargas e relatórios de cobrança, conta do cliente e cheques, com impressão.
- Evitar somar faturamento, previsão de cobrança e recebimento real como se fossem a mesma métrica.

## 15. Questões pendentes — não supor respostas
- Quem pode cancelar/estornar, editar dados, reabrir caixa, aprovar divergências e repassar cheques?
- Regras de duplicidade de CPF/CNPJ, acesso a dados pessoais e compartilhamento de clientes entre filiais.
- Fórmula exata para alerta de desconto efetivo; preço de custo versus preço negociado.
- Quando ocorre reserva/baixa de estoque, em especial devolução, expedição e mercadoria que continua em caminhão.
- Integração bancária e emissão de boletos, contagem de dias corridos/úteis, feriados e encargos.
- Forma de confirmação e comprovação de Pix, cartão, cheques e recebimentos do motorista.
- Definições de relatórios e responsáveis por pagamentos de contas bancárias e centralização entre filiais.
- Emissão fiscal/contábil é uma frente posterior que exige validação especializada.
- Antes do piloto real: direitos de uso, contrato, preço, suporte, disponibilidade, backups, migração, LGPD e segurança.

**Não implementar decisões em aberto por suposição.**