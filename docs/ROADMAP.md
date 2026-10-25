# Operix — planejamento, decisões e entregas

**Estado:** planejamento. Nenhum marco novo foi implementado por esta reorganização.

## 3. Entregas e critérios de aceite

**Situação atual:** API inicial com persistência de organizações e filiais entregue; autenticação e os fluxos completos do ERP ainda não implementados. O roadmap registra marcos de produto, não aulas ou exercícios. Datas serão definidas apenas após estimativa.

### Marcos

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

Os marcos D1–D5 compõem a primeira demonstração funcional; D6–D8 ampliam os fluxos. O detalhamento e decisões em aberto estão na seção de requisitos deste documento. Não anunciar como implementada qualquer linha ainda pendente.

### Entregas incrementais de D1

**Planejamento:** documentado como proposta pendente de validação. **Implementação de D1:** não iniciada; o status do marco permanece inalterado. Os critérios abaixo são propostos e só devem ser usados para concluir entregas após aprovação do respectivo escopo e verificação do código.

As referências B1–B7 identificam as validações de negócio; T1–T7 identificam as recomendações técnicas. A sequência permite aprovações por incremento: decisões futuras de outros módulos não bloqueiam o componente isolado de senhas.

| Incremento | Entrega proposta | Dependências | Critério de aceite proposto | Status |
| --- | --- | --- | --- | --- |
| D1.0 | Validar o recorte e os contratos de identidade | Revisão de B1–B7 e T1–T7 conforme o incremento | Registrar neste documento decisões aprovadas, responsáveis pela validação e pendências que bloqueiam cada entrega | Planejamento registrado; validações pendentes |
| D1.1 | Componente de senha e testes isolados | Aprovação de T3 e contrato de entrada; adoção controlada das dependências de hash e testes | Casos de T3 passam; biblioteca compatível com o ambiente; nenhum segredo exposto; rascunho de `app/main.py` preservado | Não iniciado |
| D1.2 | Persistência das contas e vínculos | D1.1; contrato de identidade aprovado em D1.0, incluindo T1 e T6 | Migração reproduzível em PostgreSQL de teste; unicidade por organização; vínculos de outra organização rejeitados; dados existentes preservados | Não iniciado |
| D1.3 | Persistência e avaliação de papéis e exceções | D1.2; matriz, escopos e precedência aprovados em D1.0 | Testes demonstram concessão, negação, ausência de permissão e composição aprovada, sem ampliar organização ou filial | Não iniciado |
| D1.4 | Provisionamento da primeira administração | D1.3; autoridade inicial e fluxo T5 aprovados | Conta inicial criada pelo fluxo controlado; repetição e execução concorrente não recriam administração nem expõem credenciais | Não iniciado |
| D1.5 | Login, identificação, sessão e logout | D1.4; T4 e política B6 aprovados | Credenciais válidas autenticam; inválidas, expiradas ou revogadas falham; limites de tentativa verificados; logout invalida a sessão | Não iniciado |
| D1.6 | Administração de contas e acessos | D1.3 e D1.5; delegação, recuperação e proteção administrativa aprovadas | Gestão respeita poderes delegáveis; mudanças são auditadas e efetivas na próxima requisição; revogação e proteção do último administrador resistem à concorrência | Não iniciado |
| D1.7 | Integração de autorização na API existente | D1.6; T7 e destino de `/customers` aprovados | Identificadores adulterados não ultrapassam escopos; consultas consolidadas e ações respeitam permissões; rotas públicas e protegidas têm contrato explícito | Não iniciado |
| D1.8 | Verificação integrada e revisão do marco | D1.1–D1.7 | Suíte com dados sintéticos e PostgreSQL de teste comprova os contratos, acessos cruzados e regressões; documentação reflete somente resultados validados | Não iniciado |

A primeira tarefa de implementação proposta é **D1.1**, após aprovação de sua decisão técnica e autorização para alterar arquivos. Concluir esse componente não conclui o marco D1. O fechamento do marco depende do critério geral e das evidências integradas de D1.8; D0 permanece aberto para requisitos ainda não validados.

### Gates de implantação

- **G1 — decisão comercial:** apresentar demonstração; obter aprovação explícita, definição de escopo, responsabilidades e condições de uso.
- **G2 — homologação:** revisar segurança, segregação de acessos, migração autorizada, testes financeiros/logísticos, operação com dados reais, integrações, backup/restauração, observabilidade e suporte.
- **G3 — produção:** implantar de forma controlada após G1 e G2, com rollback e acompanhamento; o repositório público de demonstração não se converte automaticamente em ambiente de produção.

### Regras de entrega

Cada mudança deve ter escopo rastreável, critério de aceite, implementação, verificação (automatizada quando disponível), revisão por PR e atualização pontual da documentação afetada. O status depende de evidência testável, não da existência de um arquivo ou interface.

**Próxima prioridade:** validar as decisões de D0 e as recomendações técnicas necessárias ao próximo incremento de D1; após aprovação e autorização, iniciar D1.1, preservando a API existente e o rascunho local. A documentação deste plano não inicia a implementação.

### 15. Questões pendentes — não supor respostas
- Quem pode cancelar/estornar, editar dados, reabrir caixa, aprovar divergências e repassar cheques?
- Regras de duplicidade de CPF/CNPJ, acesso a dados pessoais e compartilhamento de clientes entre filiais.
- Fórmula exata para alerta de desconto efetivo; preço de custo versus preço negociado.
- Quando ocorre reserva/baixa de estoque, em especial devolução, expedição e mercadoria que continua em caminhão.
- Integração bancária e emissão de boletos, contagem de dias corridos/úteis, feriados e encargos.
- Forma de confirmação e comprovação de Pix, cartão, cheques e recebimentos do motorista.
- Definições de relatórios e responsáveis por pagamentos de contas bancárias e centralização entre filiais.
- Emissão fiscal/contábil é uma frente posterior que exige validação especializada.
- Antes do piloto real: direitos de uso, contrato, preço, suporte, disponibilidade, backups, migração, LGPD e segurança.

#### Volume de referência

Operação inicial de referência: cerca de 200 pedidos diários, em canais presenciais, telefone e WhatsApp. É parâmetro para descoberta e testes futuros, não meta de desempenho já comprovada.


**Decisões abertas não devem ser implementadas como suposições.**
