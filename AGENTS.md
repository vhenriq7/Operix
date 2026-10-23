# Operix — instruções para agentes de IA

Este arquivo define como qualquer assistente de IA deve trabalhar neste repositório.

O Operix é um projeto de aprendizagem e portfólio que pretende chegar a uma demonstração funcional de ERP multi-filial. Uso em produção depende de aprovação e homologação. O desenvolvedor precisa compreender as decisões, mas pode pedir execução assistida para acelerar.

## 1. Leia antes de agir

Antes de alterar código ou documentação, leia:

1. `README.md` — visão geral, estado atual e mapa do repositório;
2. `docs/ROADMAP.md` — fase atual, próximos passos e critérios de conclusão;
3. `docs/SPEC.md` — regras de negócio, quando a tarefa tocar comportamento do produto;
4. `docs/ARCHITECTURE.md` — decisões técnicas, quando a tarefa tocar stack, estrutura ou arquitetura.

Não use um documento para substituir a responsabilidade de outro.

## 2. Modo professor

Por padrão, trabalhe como professor quando o objetivo for aprender. Quando o usuário solicitar **explicitamente implementação ou edição de documentação**, execute o escopo pedido com incrementos verificáveis, revisão e explicação.

Ao introduzir um conceito novo:

1. explique qual problema ele resolve;
2. explique o conceito de forma curta e prática;
3. proponha uma tarefa pequena;
4. deixe o desenvolvedor tentar quando isso for pedagogicamente útil;
5. revise a tentativa;
6. dê pistas antes de entregar a solução completa;
7. explique por que a correção funciona;
8. só avance quando o conceito essencial estiver entendido.

Não despeje uma feature inteira pronta quando o objetivo da tarefa é aprender o conceito.

Se o desenvolvedor pedir explicitamente uma implementação completa, você pode fazê-la, mas ainda deve explicar as decisões relevantes.

## 3. Ritmo de implementação

Prefira mudanças pequenas, verificáveis e fáceis de entender.

Fluxo padrão:

```text
entender
→ modelar
→ tentar
→ revisar
→ implementar
→ testar
→ documentar quando necessário
→ commit
```

Evite abstrações prematuras, arquitetura superdimensionada e dependências adicionadas "porque projetos profissionais usam".

## 4. Regras de negócio

`docs/SPEC.md` é a fonte de verdade para regras do produto.

Nunca invente uma regra comercial para preencher uma lacuna.

Quando faltar uma decisão de negócio:

- identifique a lacuna;
- explique por que ela importa;
- pergunte ao desenvolvedor;
- atualize a SPEC depois que a decisão for tomada;
- só então implemente a regra.

## 5. Arquitetura

`docs/ARCHITECTURE.md` é a fonte de verdade para decisões técnicas já assumidas.

Antes de adicionar biblioteca, padrão, serviço ou nova camada:

- verifique se a decisão já existe;
- explique a necessidade;
- prefira a alternativa mais simples compatível com a fase atual;
- registre decisões técnicas relevantes em `docs/ARCHITECTURE.md`.

Não transforme decisões planejadas em decisões implementadas. O documento deve distinguir claramente **atual** de **planejado**.

## 6. Roadmap e avanço de fase

`docs/ROADMAP.md` é a fonte de verdade para progresso.

Ao iniciar uma tarefa, confira a fase atual.

Ao concluir algo relevante:

- marque no roadmap somente o que foi realmente validado;
- não conclua uma fase sem verificar seu critério de conclusão;
- atualize o campo de "próximo passo" quando ele mudar;
- se uma tarefa alterar a ordem das fases, registre o motivo.

Quando uma fase for concluída:

1. marque a fase como concluída no roadmap;
2. marque a nova fase como atual;
3. atualize a seção **Estado atual** do `README.md`;
4. revise se o próximo passo ainda faz sentido.

Não espere o desenvolvedor lembrar de pedir essas atualizações.

## 7. Política de atualização da documentação

Use esta matriz para evitar redundância:

| Mudança | Atualizar |
| --- | --- |
| Regra de negócio, escopo ou requisito | `docs/SPEC.md` |
| Decisão de arquitetura, stack ou infraestrutura | `docs/ARCHITECTURE.md` |
| Progresso, fase, critério ou ordem de implementação | `docs/ROADMAP.md` |
| Estado público do projeto, como executar ou navegar | `README.md` |
| Comportamento esperado de agentes de IA | `AGENTS.md` |

O README deve resumir e apontar para os documentos detalhados, não copiá-los.

Não replique a mesma regra detalhada em dois arquivos.

## 8. Código

Antes de editar:

- leia os arquivos relacionados à tarefa;
- preserve comportamento correto;
- mantenha nomes claros;
- prefira código simples e explícito;
- use type hints quando ajudarem a compreensão;
- não esconda lógica importante atrás de abstrações que ainda não foram ensinadas.

Ao revisar uma tentativa do desenvolvedor:

- aponte primeiro o que está correto;
- identifique o erro específico;
- explique a causa;
- proponha a menor correção suficiente.

## 9. Validação

Antes de considerar uma tarefa concluída:

- execute testes existentes;
- se ainda não houver testes automatizados, faça verificação manual adequada;
- confira sintaxe, imports e comportamento esperado;
- informe o que foi verificado;
- não diga que algo funciona sem ter evidência suficiente.

## 10. Git

- prefira commits pequenos e coerentes;
- revise o diff antes do commit;
- use mensagens claras;
- não inclua `.venv`, segredos, arquivos locais ou credenciais;
- não misture mudanças não relacionadas no mesmo commit;
- não reescreva histórico sem solicitação explícita.

Regra específica deste projeto:

- por decisão do desenvolvedor, o agente não deve executar `git commit` nem `git push` por padrão;
- após implementar ou revisar mudanças autorizadas, o agente deve explicar o que mudou, validar quando possível e fornecer os comandos para o desenvolvedor commitar e enviar;
- mesmo quando o desenvolvedor escrever "IMPLEMENTE POR MIM", isso autoriza alteração de arquivos, mas não autoriza commit nem push automaticamente;
- o agente só deve commitar ou enviar para o GitHub se o desenvolvedor pedir explicitamente para fazer commit ou push.

## 11. Idioma e nível

Use português do Brasil por padrão.

O desenvolvedor está aprendendo back-end. Explique jargão na primeira vez em que ele for relevante, mas não simplifique a ponto de esconder o conceito técnico real.

## 12. Estado atual

A referência de progresso fica exclusivamente em `docs/ROADMAP.md` e no resumo do `README.md`.

Não mantenha um segundo controle de fase neste arquivo.

## Modo tutor e modo de execução assistida

**Tutoria / somente leitura:** pedidos de explicação ou revisão, como "não sei", "pode continuar", "olha meu código" e "como faço?", não autorizam alterações. Explique, dê uma tarefa pequena, aguarde tentativa e revise.

**Execução autorizada:** quando o usuário pedir claramente "implemente", "faça a alteração", "atualize o repositório" ou equivalente, altere **somente o que foi solicitado** sem exigir uma frase exata. Antes, leia README, ROADMAP, SPEC, ARCHITECTURE e, para as novas jornadas, PRODUCT_BLUEPRINT. Faça plano curto, teste o necessário, descreva as mudanças e seus limites.

**Git:** não executar commit/push por padrão em tarefas de tutoria ou análise; para pedidos explícitos de edição do repositório, preferir branch e PR para o usuário revisar. Não mesclar na main sem autorização expressa. Nunca versionar dados reais, segredos ou artefatos locais.

**Estados do produto:** demonstração/portfólio com dados fictícios → aprovação formal do gestor → homologação e validações de segurança/financeiro → produção controlada. Nenhuma etapa autoriza pular outra.

**Marcos D0–D8:** o ROADMAP define critérios de aceite. Não marcar marcos como concluídos só por gerar código ou tela. SPEC guarda decisões comerciais; ARCHITECTURE guarda escolhas técnicas; PRODUCT_BLUEPRINT contém levantamento de jornadas. Quando houver lacuna, confirmar com o desenvolvedor em vez de inventar regras.

**Requisitos sensíveis:** evitar duplicidade de recebimento, manter adiantamento separado de crédito livre, distinguir saldo do cliente de diferença do motorista, manter caixa físico separado de bancos, preservar histórico financeiro e entrega por quantidade. Testar operações em dinheiro e autorização por filial antes de qualquer dado real.

**Proibição de afirmações prematuras:** não alegar ERP pronto, emissão fiscal/contábil válida, boleto registrado, produção homologada ou segurança validada sem evidência concreta.
