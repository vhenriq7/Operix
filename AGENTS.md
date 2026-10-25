# AGENTS.md — desenvolvimento do Operix com IA

## Ler só o necessário

1. [`docs/PROJECT.md`](docs/PROJECT.md): visão curta e situação real.
2. [`docs/MODULOS.md`](docs/MODULOS.md): **módulos comerciais** (Vendas, Estoque, CRM, Caixa, Financeiro, Fiscal, Contábil, Frota, Transportes, BI, Mobile), não módulos internos do código.
3. [`docs/specs/`](docs/specs/): regras previamente discutidas; consultar somente as pertinentes à tarefa. Os arquivos podem agrupar mais de um módulo comercial e não significam que algo esteja implementado.
4. [`docs/ROADMAP.md`](docs/ROADMAP.md) e [`docs/TECHNICAL.md`](docs/TECHNICAL.md): consultar só o incremento e os requisitos técnicos relevantes.

## Executar um incremento de cada vez

- Confirmar o **módulo comercial**, o comportamento esperado, dependências e critérios de aceite. Não implementar todo o catálogo.
- Verificar o código atual e preservar contratos e migrações. Não confundir requisitos futuros com funcionalidades prontas.
- Implementar a menor mudança testável. Explicar ao responsável as decisões centrais e propor um desafio curto para aprendizado ativo, sem comprometer segurança.
- Criar/executar testes (inclusive erros, repetição de requisições, concorrência quando aplicável) e informar o que não foi possível verificar.
- Atualizar a especificação pertinente se o comportamento mudar; atualizar PROJECT só para decisões gerais, MODULOS para escopo comercial, ROADMAP para status e TECHNICAL para arquitetura. Não duplicar textos.

## Invariantes obrigatórias

- Separar **contratação de módulo**, **permissões de usuários** e **parametrização**. Controlar autorização no backend, por organização e filial.
- Preservar diferenças entre venda, recebimento, dívida, crédito livre, caixa físico, banco, faturamento fiscal e entrega.
- Usar dinheiro em representação exata, transações, rastreabilidade e proteção contra lançamentos duplicados; controlar estoque por filial e localização.
- Não incluir dados reais ou segredos no repositório público. Não marcar algo como pronto sem testes. Fiscal, bancário e contábil exigem validações especializadas antes de operação real.
- Web e desktop são canais da mesma plataforma; Mobile exige definição de escopo e não equivale automaticamente a licença cobrada. Offline ainda não decidido.
- Desenvolvimento/demonstração com dados sintéticos **não significa produção**.

## GitHub

Commits pequenos e claros, revisão por branch/PR quando conveniente. Não fazer deploy nem modificações destrutivas sem autorização. Informar os arquivos alterados e as verificações.
