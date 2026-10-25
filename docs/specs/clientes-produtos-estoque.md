# Operix — cadastros, produtos e estoque

**Estado:** requisitos planejados; clientes ainda usam memória na API atual.

### 2. Cliente PF/PJ e ficha completa
- Tipo PF ou PJ; CPF ou CNPJ inicialmente obrigatórios conforme tipo; nome/razão social, nome fantasia se PJ e pessoa de contato quando houver.
- Código de cadastro, e-mail, múltiplos telefones com etiquetas (WhatsApp, celular, comercial, residencial), principal e observações.
- País, CEP, UF, cidade, bairro, logradouro, número, complemento e referência. Endereços de cobrança e entrega podem ser diferentes. Consulta automática do CEP é opcional e editável.
- Visão resumida: valores em aberto, atrasados, crédito livre, adiantamentos para pedidos específicos, limite de fiado, data da dívida mais antiga, último pagamento e próximo contato.
- Abas/histórico de orçamentos, pedidos, pagamentos, créditos, estornos, entregas, cobranças e transações, filtráveis por data e filial respeitando regras de compartilhamento.
- Confirmar posteriormente política de duplicidade, privacidade, CPF/CNPJ e dados mínimos quando o cliente não tem documento.

### 3. Cadastro de produtos e estoque
- Produto central: código interno único, nome, descrição, categoria, marca, unidade (unidade, kg etc.), código de barras quando houver, peso líquido, peso bruto, custo de referência e dados tributários pertinentes.
- Por filial: preço de venda, estoque, estoque mínimo e histórico de entradas, saídas, transferências, ajustes, devoluções e reservas.
- A mesma mercadoria pode ter **preços e saldos distintos por filial** sem duplicar o cadastro geral.
- Não atribuir ao produto a situação de pagamento/entrega de uma venda: esses são dados do pedido.

#### Transferências e estoques

- Uma transferência entre filiais tem fluxo inicialmente previsto `SOLICITADA → APROVADA → RECEBIDA`; ainda precisa definir quando o estoque sai da origem e entra no destino.
- Estoque por filial deve ser rastreável por movimentações e nunca aumentar em retorno de mercadoria antes de registrar a localização física real.
