# Operix — Projeto

**Situação:** em desenvolvimento, com demonstração planejada utilizando dados sintéticos. O sistema não está homologado nem disponível para produção.

Referência central de engenharia do Operix. Reúne requisitos, arquitetura, stack, marcos de entrega e decisões pendentes. O `README.md` apresenta o repositório; o `AGENTS.md` define as instruções para agentes de IA.

## 1. Requisitos de produto

**Estado:** requisitos em validação. As funcionalidades descritas não estão necessariamente implementadas; consultar o README e o roadmap.
**Primeiro destinatário:** uma empresa de três filiais, controladas por uma administração central. Uma filial pode ser a matriz; não criar uma quarta unidade artificial.
**Fase atual:** construção de demonstração funcional com dados sintéticos, em repositório público.
**Entrada em produção:** condicionada a aprovação empresarial, homologação e planejamento operacional.

Esta seção centraliza requisitos de produto, regras funcionais e pendências. A arquitetura e as entregas estão nas seções seguintes.

### 1. Identidade, filiais e equipe
- Administrador principal cadastra/gerencia filiais, usuários, funções e permissões de ação.
- Usuário vinculado à organização e a uma ou mais filiais conforme função. Dono e financeiro podem consultar consolidação das três filiais quando autorizados.
- Perfis de referência: dono, administrador, financeiro, gerente, vendedor, caixa, estoque, conferente e logística. Permissões específicas são configuráveis e devem ser validadas no servidor.
- Abrir, movimentar e fechar caixa registra o usuário real em cada evento; **uma pessoa pode abrir e outra fechar**.
- Configurações comuns, como modelos de parcelamento de boletos, ficam disponíveis para todas as filiais da mesma organização.

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

### 14. BI, gerência e documentos
- Painel da patroa/patrão: todas as três filiais juntas ou uma por vez, conforme permissão e período.
- Valores de vendas, recebidos, caixa físico, fiado a vencer/vencido, créditos livres, adiantamentos vinculados, boleto, cheques e contas a pagar **em blocos separados**.
- Relatório por **cada carga**: dia, número da carga, caminhão, motorista, ajudantes, pedidos, quais foram entregues/parciais/não entregues, motivo, pendências, situação financeira e montante recebido pelo motorista.
- Resumo diário de cargas e relatórios de cobrança, conta do cliente e cheques, com impressão.
- Evitar somar faturamento, previsão de cobrança e recebimento real como se fossem a mesma métrica.

### Diretriz de produto — módulos contratáveis e parametrização (planejada)

**Decisão de direcionamento:** o Operix deve poder atender desde um comércio com operação simples de balcão até uma empresa com rotinas administrativas e de distribuição mais completas, sem exigir que cada cliente contrate todos os recursos. Trata-se de **requisito de produto em planejamento**, não de funcionalidade implementada, plano comercial lançado ou preço aprovado.

- **Catálogo de módulos:** desenhar ofertas opcionais, coerentes com os domínios já especificados neste documento: (1) comercial/PDV e orçamentos/pedidos; (2) estoque e compras; (3) caixa e recebimentos; (4) financeiro, contas a pagar/receber e cobrança/boletos; (5) documentos fiscais, sujeito a validação e homologação próprias; (6) cargas, frota e logística; (7) relatórios, painéis gerenciais e BI. O núcleo técnico de organização, filiais, identidade e cadastros compartilhados sustenta os módulos e não precisa aparecer como contratação separada.
- **Contratação por necessidade:** o escopo e o orçamento de cada empresa devem refletir os módulos que ela efetivamente utilizará. Pacotes, preços, dependências e condições de contratação serão definidos em etapa comercial posterior. Não condicionar o uso do PDV simples à aquisição de módulos administrativos desnecessários.
- **Três camadas distintas de controle:** (a) **habilitação contratual** dos módulos para a organização, eventualmente com escopo por filial; (b) **permissões** de usuários/funções e filiais, sempre verificadas no servidor; (c) **parametrização** das regras operacionais da organização/filial. Ter um módulo contratado não concede automaticamente acesso a todos os funcionários.
- **Parametrização consultiva:** permitir configurar, conforme módulo e regras já validadas, fluxos de trabalho, etapas de pedidos, limites e alertas, condições comerciais, formas de recebimento, visibilidade e particularidades por filial, evitando código customizado para cada cliente. Configurações devem ser versionáveis/auditáveis e não podem contrariar regras financeiras, fiscais ou de segurança.
- **Implantação orientada à operação:** inspirar-se em três etapas: (1) mapeamento de processos do cliente; (2) parametrização dos módulos e regras aprovados; (3) treinamento da equipe e suporte de entrada em operação. Escopo, tempo, serviços e níveis de suporte ainda precisam ser definidos.
- **Integração interna sem retrabalho:** módulos ativos compartilham entidades e processos com consistência, de modo que um registro originado em vendas possa alimentar caixa, estoque, financeiro ou fiscal quando o fluxo contratado e autorizado exigir. Evitar relançamentos e integrações frágeis entre cópias dos mesmos dados; operações financeiras, fiscais e logísticas permanecem conceitualmente distintas, conforme as invariantes já registradas.
- **Priorização:** começar pela experiência de comércio físico (PDV, vendas, caixa, estoque e financeiro) e evoluir conforme os marcos existentes. E-commerce, marketplaces e automação de envios **não são prioridade inicial**. Funções especializadas de distribuição, como Kanban de pedidos, validação financeira/estoque, separação e faturamento em lote, ficam como **referências para avaliação posterior**, não como requisitos fechados nem implementações iniciadas.

**Questões abertas para especificação:** granularidade de licenças e filiais, medição de uso, cobrança, dependências entre módulos, provisionamento/desativação sem perda de dados, compatibilidade de parametrizações, migração entre planos e responsabilidades de implantação/suporte. Não implementar suposições sobre esses pontos.

### Sites de inspiração (referências externas)

Referências de **experiência do produto**, não dependências de tecnologia, integrações confirmadas, autorização de copiar interfaces ou comprovação do uso específico em outra empresa:

- **Principal — [Domtec / Yzidro ERP](https://domtec.com.br/distribuidoras):** implantação consultiva, parametrização por regras de negócio e amplitude da retaguarda de gestão.
- **Principal — [Nex / Nextar](https://www.nextar.com.br/):** simplicidade visual e operacional do PDV, atendimento ágil em balcão e experiência do aplicativo para computador.
- **Complementar — [Bling](https://www.bling.com.br/):** integração de vendas, estoque, financeiro e documentos fiscais em ERP para loja física; não tomar e-commerce como prioridade automática do Operix.
- **Complementar — [Distribuidora Eficaz](https://www.distribuidoraeficaz.com.br/):** visualização por etapas de pedidos, conferência de estoque/crédito e operações de distribuidora como ideias para análise futura. **Não está confirmado** por qual razão uma empresa observada utiliza essa plataforma.

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

#### Validações de negócio para D1

As regras de identidade e alcance já registradas em **Identidade, filiais e equipe** e **Filiais e conta do cliente** permanecem requisitos, ainda sem implementação. Os pontos abaixo detalham as decisões necessárias ao planejamento de D1; não representam respostas aprovadas.

| Referência | Decisão pendente | Impacto no D1 |
| --- | --- | --- |
| B1 | Representação do Dono, quantidade de proprietários, seus poderes e transferência de responsabilidade | Definir os papéis iniciais e sua relação com a administração principal |
| B2 | Matriz de ações por função, acúmulo de papéis e exercício de funções diferentes entre filiais | Aprovar concessões, restrições e alcance das atribuições |
| B3 | Quem cria/desativa contas, configura papéis, concede exceções e delega poderes; procedimento de substituição do último administrador | Delimitar a administração de acessos sem permitir elevação indevida de privilégios |
| B4 | Dados mínimos das contas e necessidade imediata de cadastrar funcionários sem login | Delimitar identidade de acesso e cadastro operacional, sem antecipar um módulo de RH |
| B5 | Filiais autorizadas por perfil e inclusão automática ou explícita de novas filiais | Definir alcance operacional e consultas consolidadas |
| B6 | Adequação dos prazos de sessão propostos em T4, sessões simultâneas e entrega, troca e recuperação da credencial inicial | Aprovar o ciclo de acesso e recuperação das contas |
| B7 | Destino das rotas de clientes em memória durante D1 | Aprovar a compatibilidade da API; autenticar uma lista global não implementa isolamento |

A repetição do e-mail entre organizações continua pendente para a ampliação do uso. O desenho técnico deve identificar a organização no login sem presumir uma política global de unicidade. As decisões sobre estoque, cobrança e integrações permanecem nos módulos correspondentes e não precisam ser encerradas para iniciar D1.


### Regras complementares consolidadas

#### Filiais e conta do cliente

- A organização tem três filiais, com administração central. A matriz não representa uma quarta loja.
- O cliente pertence à organização e possui filial de origem; seu cadastro pode ser compartilhado ou restrito. Se não compartilhado, outras filiais não consultam sua conta comercial, histórico, créditos ou débitos. Se compartilhado, somente filiais e usuários autorizados podem consultá-los ou realizar operações.
- O identificador de login planejado é e-mail; uma conta pertence a uma organização. O mesmo e-mail não identifica usuários distintos dentro dessa organização. Regra de repetição entre organizações e papel próprio de Dono seguem pendentes.
- Administração e financeiro podem ter visão consolidada; vendedor e caixa se limitam às filiais atribuídas. Alcance de filial não equivale a permissão para executar toda operação.

#### Crédito e comissão

- Cada obrigação do cliente é vinculada a pedido e valor. Crédito livre não quita débito automaticamente; a aplicação exige evento explícito e rastreável.
- Compra a prazo pode observar limite por cliente; a decisão sobre bloqueio ou aprovação ao exceder o limite permanece aberta.
- Comissão de venda mantém vínculo com vendedor e filial comercial, mesmo quando outra filial atende o pedido. Comissão prevista e adquirida são distintas; a comissão adquirida pressupõe pedido pago. Fórmula final e arredondamento dependem de validação.

#### Transferências e estoques

- Uma transferência entre filiais tem fluxo inicialmente previsto `SOLICITADA → APROVADA → RECEBIDA`; ainda precisa definir quando o estoque sai da origem e entra no destino.
- Estoque por filial deve ser rastreável por movimentações e nunca aumentar em retorno de mercadoria antes de registrar a localização física real.

#### Volume de referência

Operação inicial de referência: cerca de 200 pedidos diários, em canais presenciais, telefone e WhatsApp. É parâmetro para descoberta e testes futuros, não meta de desempenho já comprovada.


**Decisões abertas não devem ser implementadas como suposições.**

## 2. Arquitetura e tecnologias

**Estado:** arquitetura evolutiva; informações implementadas e planejadas são diferenciadas.

### Estratégia

**Monólito modular** com API HTTP/JSON e PostgreSQL. Os limites internos evoluirão pelos domínios do produto, sem microserviços ou camadas artificiais no estágio atual. A separação arquitetural deve preservar transações consistentes entre pedidos, pagamentos, estoque e expedição.

### Canais de acesso previstos: web e aplicativo para computador

**Requisito de produto planejado:** oferecer o Operix de duas formas complementares: **interface web acessível pelo navegador** e **aplicativo instalado no computador do cliente**, com foco especial em uso cotidiano de PDV/caixa. Ambas devem representar a mesma organização, filiais, permissões, dados e regras de negócio; não constituem ERPs separados nem bases comerciais independentes.

- Priorizar navegação rápida, interface intuitiva e fluxos adequados ao balcão, sem comprometer recursos administrativos mais completos.
- Reutilizar a API e as regras de domínio, respeitando autenticação, autorização, auditoria e isolamento de organização/filial em qualquer cliente.
- **A definir:** tecnologia e sistemas operacionais do aplicativo instalado; distribuição, atualização e suporte; impressoras, leitores e demais periféricos; comportamento com conexão instável; necessidade de operação offline e estratégia de sincronização/reconciliação segura. A oferta de um aplicativo instalado **não significa** que a operação offline já esteja definida ou implementada.
- A emissão fiscal e qualquer funcionalidade bancária em modo offline, se um dia propostas, exigem avaliação legal/técnica e homologação específica. Não prometer paridade de funcionalidades antes dessa análise.

### Stack e maturidade

| Área | Tecnologia | Estado |
| --- | --- | --- |
| Linguagem e API | Python, FastAPI, Uvicorn | Implementados |
| Validação e contrato HTTP | Pydantic, OpenAPI | Implementados |
| Banco de dados | PostgreSQL | Integrado parcialmente |
| Persistência | SQLAlchemy, psycopg | Em uso em organizações/filiais |
| Migrações | Alembic | Configurado, migração inicial versionada |
| Versionamento | Git e GitHub | Em uso |
| Testes automatizados | Pytest (previsto) | Não implementado |
| Contêineres | Docker (previsto) | Não implementado |
| Interface operacional | Stack a definir | Não implementada |
| Deploy e observabilidade | Infraestrutura a definir | Não implementados |

Dependências existentes são especificadas em `requirements.txt`. Novas tecnologias só devem ser adotadas mediante necessidade e revisão da decisão.

### Componentes existentes

- `app/main.py`: API inicial com saúde, clientes, organizações e filiais.
- `app/database.py`: conexão e sessões SQLAlchemy via `DATABASE_URL`.
- `app/models.py`: entidades `Organizacao` e `Filial`, com relacionamento.
- `alembic/`: controle versionado da estrutura de banco.
- `app/main.py` ainda utiliza **lista em memória para clientes**; apenas organizações e filiais usam persistência no PostgreSQL.

**Ainda inexistentes:** autenticação, RBAC, isolamento efetivo entre organizações, persistência real de clientes, testes automatizados, módulos transacionais completos, interface de negócio, integrações bancárias e implantação.

### Domínios previstos

Identidade e filiais; clientes; produtos e estoque; comercial (orçamentos/pedidos); conta do cliente e recebimentos; caixa; cobranças; logística/cargas; financeiro central; relatórios. A estrutura física de pastas será adaptada conforme funcionalidades forem implementadas.

### Regras técnicas transversais

- **Autorização:** identidade autenticada e escopo por organização/filial em cada consulta e comando; o front-end não substitui controles de API. Testar acessos cruzados antes de disponibilizar dados reais.
- **Integridade:** operações financeiras e de estoque devem manter transações, vínculos e histórico; definir representação exata para valores monetários (Decimal/NUMERIC ou centavos inteiros) antes do módulo financeiro; evitar `float`.
- **Idempotência:** impedir cobrança, recebimento, reserva ou baixa duplicados por requisições repetidas ou concorrentes.
- **Auditoria:** identificar usuário, data, contexto e motivo de eventos relevantes; estornos e correções não apagam o histórico operacional.
- **Fronteiras de domínio:** venda não equivale a recebimento; recebimento não equivale a entrega; dinheiro com motorista não é dinheiro conferido no caixa; cheque recebido não é compensado; parcela prevista não é boleto bancário registrado.
- **Estoque/logística:** quantidades são controladas por item e localização, incluindo retirada, caminhão, retorno e entregas parciais. Um pedido pode estar em múltiplas cargas.
- **Qualidade:** testes unitários, integração e autorização devem acompanhar os módulos críticos; automação CI pode ser introduzida com a suíte de testes, sem alegar que já existe.

### Planejamento técnico de D1

**Estado:** proposta registrada para revisão; implementação não iniciada. A inclusão deste planejamento não aprova bibliotecas, modelos, políticas ou alterações de contrato. Os incrementos estão na seção **Entregas incrementais de D1**.

#### Base técnica já adotada

Aplicam-se a D1 a stack e o monólito modular descritos em **Estratégia** e **Stack e maturidade**, a persistência e as migrações existentes e os controles exigidos em **Regras técnicas transversais**. Essa base deve ser preservada; autenticação, autorização e isolamento efetivo continuam inexistentes no código.

Conta vinculada à organização, e-mail único dentro dela, alcance por filial e permissões configuráveis são requisitos já registrados na seção de produto, não modelos implementados ou prova de homologação empresarial.

#### Recomendações técnicas ainda não aprovadas

Todos os itens T1–T7 abaixo aguardam validação técnica e, quando indicado, as decisões de negócio B1–B7. As estruturas são conceituais; o schema definitivo dependerá do recorte aprovado.

##### T1 — Identidade e vínculos

| Estrutura proposta | Responsabilidade |
| --- | --- |
| `Usuario` | Identidade individual de acesso: organização, nome, e-mail normalizado, hash de senha, situação ativa e datas de controle |
| `UsuarioFilial` | Vínculos explícitos entre conta e filiais autorizadas |
| `Papel` e suas permissões | Agrupamento configurável de ações, pertencente à organização |
| Atribuição de papel | Associação de usuário e papel com escopo explícito de organização ou filial |
| Exceção individual | Concessão ou negação de uma ação ao usuário em um escopo determinado |

Recomenda-se garantir no banco a unicidade do e-mail normalizado por organização. A regra de normalização e as cardinalidades de papéis serão definidas no contrato de identidade, considerando B2 e B4.

Funcionários, administradores e proprietários com acesso usariam a mesma entidade `Usuario`; seus poderes decorreriam das atribuições. A recomendação é um papel próprio para proprietário, condicionado a B1 e sem atalho de autorização irrestrita. Cadastro operacional de colaborador sem login, se necessário, seria separado da conta; sua inclusão em D1 depende de B4.

##### T2 — Papéis, ações e exceções

Recomenda-se RBAC, controle de acesso por papéis, complementado por exceções individuais. O catálogo de ações seria conhecido pelo servidor, por exemplo `usuarios.criar`, `usuarios.desativar` e `filiais.consultar`. A administração poderia agrupar ações existentes em papéis; cadastrar um nome de permissão não criaria uma funcionalidade.

A proposta distingue permissões administrativas de organização e atribuições operacionais por filial. Um valor ausente de filial não significaria acesso irrestrito. Para uma ação no escopo avaliado, a precedência proposta é:

1. exigir conta ativa e contexto organizacional válido;
2. exigir vínculo com a filial, quando aplicável;
3. verificar concessão por papel ou por exceção individual;
4. fazer uma negação explícita aplicável prevalecer sobre concessões;
5. negar na ausência de concessão.

Exceções não ampliariam organização ou filiais autorizadas. A matriz, a composição de papéis, a configuração individual e os poderes de delegação dependem de B2, B3 e B5. Alterações de acesso seriam auditadas e consideradas na próxima requisição, sem depender de permissões antigas incorporadas a uma credencial.

##### T3 — Proteção de senhas

Recomenda-se Argon2id por `pwdlib[argon2]`, com geração e verificação feitas pela biblioteca e armazenamento apenas de `senha_hash`. A dependência ainda não integra as dependências declaradas nem foi adotada pelo projeto. Senhas, hashes e tokens não seriam expostos em respostas operacionais ou logs; a credencial de sessão seria entregue apenas no fluxo autorizado de autenticação.

O primeiro incremento proposto é um componente isolado de senha, com testes de senha correta/incorreta, hashes distintos e verificáveis para a mesma senha e rejeição segura de hash inválido. A compatibilidade da biblioteca com o Python do projeto e o contrato de entrada devem ser verificados antes da integração. O ciclo de credenciais iniciais e recuperação depende de B6.

##### T4 — Login e sessões revogáveis

Recomenda-se login por e-mail e senha no contexto de uma organização. Esse contexto poderia estar pré-selecionado na demonstração de uma empresa; sua apresentação não autorizaria acesso. Após autenticar, a organização ficaria vinculada à sessão e seria validada pelo servidor.

A proposta é uma sessão persistida no PostgreSQL, com token opaco aleatório de 32 bytes de entropia. Somente seu digest SHA-256 seria armazenado, acompanhado de usuário, criação, última atividade, expiração e revogação. Identidade, situação da conta e autorizações atuais seriam verificadas em cada requisição.

Para a API e o Swagger iniciais, recomenda-se `Authorization: Bearer` com os recursos do FastAPI. Não se propõe JWT, Redis ou serviço externo neste recorte. O transporte por cookie `HttpOnly` e `Secure`, acompanhado de proteção CSRF, dependeria da definição da interface web futura e não alteraria o modelo de sessão.

**Política sugerida, não aprovada:** 30 minutos de inatividade e oito horas de duração máxima, configuráveis e verificadas no servidor. Atividade não prorrogaria o prazo absoluto. Recomenda-se logout da sessão atual e revogação de todas as sessões após desativação ou redefinição de senha; a adequação operacional e as sessões simultâneas dependem de B6.

O login incluiria resposta genérica para credenciais inválidas e limitação de tentativas. Parâmetros, persistência desse controle e contrato de expiração seriam definidos na revisão técnica, sem tratar memória de um único processo como controle compartilhado entre instâncias.

##### T5 — Primeira conta e administração

Recomenda-se provisionar a primeira conta administrativa por comando local controlado, na organização existente, solicitando a senha sem exibi-la. Não haveria cadastro administrativo público, senha padrão ou segredo passado em argumento de comando.

O provisionamento recusaria recriação e seria transacional, com proteção contra duas inicializações concorrentes. A API administrativa posterior permitiria gerenciar contas, filiais autorizadas, papéis, exceções e revogação de sessões, sempre dentro da autoridade de delegação aprovada em B3.

Recomenda-se proteger o último acesso administrativo efetivo contra desativação ou retirada de poderes, inclusive em operações concorrentes. A auditoria registraria responsável, momento e alteração. Destinatário inicial, limites de delegação, substituição administrativa e entrega de credenciais dependem de B3 e B6.

##### T6 — Isolamento no servidor e no banco

Para atender às regras de autorização já registradas, recomenda-se obter o contexto organizacional da sessão válida e aplicar escopo nas consultas e comandos antes de retornar ou alterar recursos. Identificadores recebidos por URL ou corpo seriam apenas seletores, sujeitos à autorização.

Restrições relacionais, inclusive chaves estrangeiras compostas quando necessárias, impediriam associar conta, filial ou papel de organizações diferentes. Consultas consolidadas agregariam somente filiais autorizadas para a ação consultada. Esses controles complementariam, sem substituir, os testes de acesso cruzado.

##### T7 — Integração com a base existente

Recomenda-se preservar `Organizacao`, `Filial`, `get_db` e o histórico do Alembic, acrescentando apenas os módulos e migrações necessários. A separação de autenticação e autorização seria gradual, sem nova infraestrutura ou camadas genéricas antecipadas.

O rascunho local de login em `app/main.py` não implementa D1 e deve permanecer preservado até uma tarefa de integração expressamente autorizada. As rotas persistentes receberiam identidade, permissão e escopo. Para `/customers`, recomenda-se indisponibilidade na API operacional até a persistência de D2; essa mudança de contrato depende de B7 e não é uma decisão adotada.

### Ambientes e entrada em produção

Etapa atual: desenvolvimento local e demonstração com dados sintéticos. Produção exige aprovação formal, revisão de segurança e LGPD, integração bancária homologada, testes de carga e concorrência, backup e restauração, monitoramento, plano de rollback e suporte. Nenhum desses controles é considerado concluído por estar documentado.

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
