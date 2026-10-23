# AGENTS.md — Operix

Instruções de execução para agentes de IA que colaboram no desenvolvimento do Operix. Este arquivo não é um tutorial.

## Referências

- `docs/PROJECT.md`: requisitos, regras de negócio, arquitetura, tecnologias, decisões pendentes, marcos e critérios de aceite.
- `README.md`: apresentação e execução local.

Antes de agir, consulte os documentos pertinentes à alteração; não replique conteúdo entre arquivos.

## Fluxo de trabalho

1. Compreenda a solicitação, os arquivos envolvidos e a compatibilidade com os contratos existentes.
2. Implemente a menor mudança coesa e verificável, sem introduzir bibliotecas, camadas ou diretórios sem justificativa.
3. Não presuma regra de negócio ausente: sinalize a decisão pendente antes de implementar comportamento irreversível.
4. Inclua ou ajuste testes relevantes quando houver ambiente para isso; execute as verificações disponíveis e relate limitações.
5. Atualize a seção pertinente de `docs/PROJECT.md` quando mudar uma regra de negócio, decisão técnica ou estado de entrega.
6. Documente claramente mudanças incompatíveis, migrações e impactos em segurança/dados.

## Invariantes

- Nunca exponha segredos nem inclua dados reais de clientes, funcionários ou empresas no repositório público.
- Verifique autorização por organização, filial e permissão no servidor; não trate apenas filtros da interface como segurança.
- Para dinheiro e estoque, use registros rastreáveis, tipos numéricos exatos, transações e proteção contra lançamentos repetidos.
- Separe: venda e recebimento; caixa físico e conta bancária; dívida do cliente e divergência do motorista; crédito livre e adiantamento; emissão de boleto e confirmação de pagamento; separação de carga e entrega.
- Não marque funcionalidade como pronta sem evidência de implementação e teste. Não afirme que o sistema foi homologado para produção.

## Controle de mudanças

Use commits de escopo claro, uma branch de trabalho e pull requests para revisão. Quando o responsável solicitar alterações no GitHub, é permitido enviá-las para branch/PR; não fazer merge, deploy ou alteração destrutiva sem solicitação específica. Informe o que foi alterado e o que foi efetivamente verificado.

## Ambientes

**Desenvolvimento e demonstração com dados sintéticos** → aprovação do responsável → **homologação** → **produção, se autorizada**. Cada transição exige validação própria; publicação do código não implica prontidão operacional.
