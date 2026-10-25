# Operix — arquitetura e decisões técnicas

**Estado:** referência técnica; propostas não aprovadas estão sinalizadas no texto original. Veja a [visão resumida](PROJECT.md).

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
