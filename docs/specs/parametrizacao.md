# Operix — módulos contratáveis e parametrização

**Estado:** planejamento; não implementado.

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
