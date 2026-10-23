# Operix — Roadmap de entregas

**Situação atual:** API inicial com persistência de organizações e filiais entregue; autenticação e os fluxos completos do ERP ainda não implementados. O roadmap registra marcos de produto, não aulas ou exercícios. Datas serão definidas apenas após estimativa.

## Marcos

| Marco | Entrega | Critério de aceite | Situação |
| --- | --- | --- | --- |
| D0 — requisitos | Consolidar regras, cenários e decisões pendentes | Especificação revisada e fluxos críticos validados com o responsável | Em levantamento |
| D1 — identidade | Contas, login, RBAC e permissão por filial | Usuário não acessa recursos não autorizados; administradores consultam somente escopo permitido | Não iniciado |
| D2 — cadastros | Clientes, produtos, categoria, preços e estoque por filial | CRUD persistente, cadastro central e saldo por filial com testes | Não iniciado |
| D3 — comercial | Orçamentos, descontos, pedidos abertos e impressão | Fluxo orçamento → pedido sem gerar pagamento ou entrega fictícios | Não iniciado |
| D4 — caixa | Abertura, sangria, suprimento, fechamento, pagamentos mistos, crédito e fiado | Pagamentos parciais são conciliados; crédito e débito não se compensam automaticamente; auditoria dos operadores | Não iniciado |
| D5 — cobrança | Vencimentos, contatos, contas de cliente, relatórios e painéis | Vencimento original é preservado; próxima cobrança é independente; consolidação por filial | Não iniciado |
| D6 — logística | Frota, romaneio, montagem de carga, entrega parcial, pendências e prestação de contas | Baixa por pedido; retorno sem data obrigatória; dinheiro do motorista só entra no caixa após conferência | Não iniciado |
| D7 — financeiro ampliado | Boletos integrados, condições configuráveis, cheques, bancos e contas a pagar | Parcelamento fecha nos centavos; cheque repassado vincula obrigação; banco e caixa não se confundem | Não iniciado |
| D8 — validação | Testes de ponta a ponta, dados sintéticos, relatório gerencial e demonstração | Jornada comercial-financeira-logística reproduzível, números conciliados, documentação fiel ao comportamento | Não iniciado |

Os marcos D1–D5 compõem a primeira demonstração funcional; D6–D8 ampliam os fluxos. O detalhamento e decisões em aberto estão na [SPEC](SPEC.md). Não anunciar como implementada qualquer linha ainda pendente.

## Gates de implantação

- **G1 — decisão comercial:** apresentar demonstração; obter aprovação explícita, definição de escopo, responsabilidades e condições de uso.
- **G2 — homologação:** revisar segurança, segregação de acessos, migração autorizada, testes financeiros/logísticos, operação com dados reais, integrações, backup/restauração, observabilidade e suporte.
- **G3 — produção:** implantar de forma controlada após G1 e G2, com rollback e acompanhamento; o repositório público de demonstração não se converte automaticamente em ambiente de produção.

## Regras de entrega

Cada mudança deve ter escopo rastreável, critério de aceite, implementação, verificação (automatizada quando disponível), revisão por PR e atualização pontual da documentação afetada. O status depende de evidência testável, não da existência de um arquivo ou interface.

**Próxima prioridade:** concluir decisões abertas de D0 relevantes a usuários e permissões, depois iniciar D1 preservando a API existente.
