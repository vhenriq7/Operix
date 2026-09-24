# Operix — Instruções para agentes

Este arquivo define como Codex e outros assistentes devem trabalhar no repositório do Operix.

## Fontes de verdade do projeto

Antes de tomar decisões relevantes, use os documentos corretos para cada finalidade:

- `PROJECT_SPEC.md`: define o produto, o domínio, as regras de negócio e os requisitos do Operix.
- `LEARNING_ROADMAP.md`: define a ordem de aprendizagem e implementação.
- `README.md`: apresenta publicamente o projeto e deve refletir o estado atual real.
- O código existente: mostra o que já foi efetivamente implementado.

Não trate o `PROJECT_SPEC.md` como instruções de comportamento para a IA. Ele é a especificação do produto.

## Objetivo educacional

O Operix é simultaneamente um projeto de portfólio e um ambiente de aprendizagem de back-end.

Ao introduzir um conceito novo:

1. explique primeiro qual problema ele resolve;
2. explique o conceito de forma curta e prática;
3. permita que o desenvolvedor tente implementar quando isso fizer sentido;
4. revise a tentativa antes de substituir tudo por uma solução pronta;
5. explique bibliotecas, padrões ou abstrações novas antes de depender delas.

Evite gerar grandes partes do sistema sem que o desenvolvedor compreenda o que está sendo acrescentado.

## Ordem de desenvolvimento

Siga `LEARNING_ROADMAP.md` como referência para a sequência de aprendizagem e implementação.

Não avance de fase apenas porque uma biblioteca ou parte do código já foi adicionada. Antes de considerar uma fase concluída, confira o respectivo critério de conclusão descrito no roadmap.

Se surgir uma necessidade técnica que justifique antecipar algum conceito, explique o motivo antes de fazê-lo.

## Atualização da documentação

Mantenha a documentação sincronizada com o estado real do projeto.

### Ao concluir uma fase do roadmap

- atualizar a seção `Estado atual` do `README.md`;
- registrar no README a nova fase em andamento;
- revisar se o `LEARNING_ROADMAP.md` ainda descreve corretamente o próximo passo;
- não marcar uma fase como concluída sem verificar seu critério de conclusão.

### Ao alterar uma regra de negócio ou requisito

- atualizar `PROJECT_SPEC.md` no mesmo conjunto de mudanças;
- não inventar novas regras de negócio sem decisão explícita do desenvolvedor quando a especificação deixar a questão em aberto.

### Ao implementar uma funcionalidade relevante

- atualizar o README somente quando a mudança for importante para representar o estado público do projeto;
- não transformar o README em diário de cada pequena alteração.

## Implementação

Antes de alterar código existente:

- leia os arquivos diretamente relacionados à tarefa;
- preserve o comportamento já correto;
- prefira mudanças pequenas e compreensíveis;
- mantenha nomes claros e consistentes;
- evite abstrações prematuras;
- não adicione dependências sem necessidade e sem explicar seu papel.

## Verificação

Antes de considerar uma tarefa concluída:

- execute os testes existentes, quando houver;
- faça uma verificação manual apropriada quando ainda não houver testes automatizados;
- confira erros de sintaxe, imports e comportamento básico;
- informe claramente o que foi verificado e o que ainda não foi.

## Git

- prefira commits pequenos e com mensagens claras;
- antes de commitar, revise o diff;
- não inclua arquivos de ambiente virtual, segredos ou arquivos locais ignorados;
- não faça mudanças não relacionadas apenas para “aproveitar” o mesmo commit.

## Estado atual de referência

No momento da criação deste arquivo, o projeto está na **Fase 2 — HTTP, APIs e FastAPI**, ainda em andamento.

O banco de dados PostgreSQL pertence à Fase 3 e não deve ser considerado iniciado apenas por estar previsto na stack do projeto.
