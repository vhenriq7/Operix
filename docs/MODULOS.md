# Operix — catálogo de módulos comerciais

**Status:** planejamento de produto, não funcionalidades prontas nem planos à venda. **Módulo = funcionalidade que um cliente pode contratar.** Os nomes abaixo representam áreas de negócio, não pastas de código.

| Módulo | O que entrega ao cliente | Escopo e referência |
| --- | --- | --- |
| **Vendas** | Orçamentos, pedidos, descontos, vendas de balcão e PDV simples. | Primeira fase. [Regras atuais](specs/vendas-caixa.md). |
| **Estoque** | Produtos, saldo por filial, entradas, saídas, transferências e compras (a detalhar). | Primeira fase. [Regras atuais](specs/clientes-produtos-estoque.md). |
| **CRM** | Relacionamento comercial com o cliente, histórico, contatos, negociação e acompanhamento de oportunidades. | Evolução; cadastros compartilhados não dependem da contratação de CRM. [Base existente](specs/clientes-produtos-estoque.md). |
| **Caixa** | Abertura e fechamento, sangria, suprimento, conferência e recebimentos por diferentes meios. | Primeira fase, integrado a Vendas. [Regras atuais](specs/vendas-caixa.md). |
| **Financeiro** | Contas a pagar e receber, cobrança, crédito, cheques, boletos, bancos e fluxo de caixa. | Implantação gradual; bancos e boletos precisam de integração/homologação. [Regras atuais](specs/financeiro-cobranca.md). |
| **Fiscal** | Emissão e controle de documentos fiscais e regras tributárias aplicáveis. | A especificar e homologar com especialistas; não está implementado. |
| **Contábil** | Integração/exportação de informações para a contabilidade; eventual automação contábil deve ter escopo próprio. | Futuro, dependente de validação contábil; não prometer escrituração completa. |
| **Frota** | Veículos, motoristas, ajudantes e controle operacional da frota. | Planejado. [Regras atuais](specs/frota-transporte.md). |
| **Transportes** | Cargas, romaneios, separação, entregas, ocorrências e prestação de contas. Roteirização avançada ainda será avaliada. | Planejado. [Regras atuais](specs/frota-transporte.md). |
| **BI** | Dashboards, indicadores e relatórios por filial ou consolidados. | Evolução progressiva. [Regras atuais](specs/bi-relatorios.md). |
| **Mobile** | Funcionalidades operacionais móveis, por exemplo para vendedores externos, se houver demanda. | Oferta e escopo por definir. **É diferente dos canais web/desktop** e não implica licença separada para todo acesso por celular. |

## Regras para oferta e implantação

- **Cada empresa contrata o necessário**, respeitando dependências funcionais a validar. Não exigir Financeiro, BI, Frota ou CRM para um pequeno comércio usar PDV/Estoque/Caixa.
- **Base técnica comum:** organização, filiais, cadastro compartilhado de clientes, identidade, permissões, segurança e auditoria. Esses recursos dão sustentação aos módulos e não são, por si, produtos comerciais obrigatórios.
- **Habilitação comercial ≠ permissão do funcionário ≠ parametrização operacional**. Um módulo ativo não significa acesso liberado para todo usuário.
- **Implantação consultiva:** mapear processos, parametrizar regras por cliente/filial e treinar os usuários. [Requisitos de parametrização](specs/parametrizacao.md).
- Os módulos compartilham dados, mas **venda, recebimento, emissão fiscal e entrega são eventos distintos**. Não duplicar lançamentos nem presumir quitações.
- **Não priorizar** e-commerce, marketplaces ou ferramentas de envios neste primeiro recorte. Funcionalidades ainda não especificadas devem ser discutidas antes da IA implementá-las.

## Onde estão os detalhes para desenvolver

A pasta [`specs/`](specs/) guarda **regras já levantadas**, algumas agrupando mais de um módulo comercial. Não é o catálogo de contratação nem uma ordem para implementar tudo. [`ROADMAP.md`](ROADMAP.md) guarda etapas e critérios detalhados; [`TECHNICAL.md`](TECHNICAL.md) guarda arquitetura e segurança. O desenvolvedor/IA lê apenas o recorte em trabalho.
