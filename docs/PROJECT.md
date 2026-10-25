# Operix — projeto e ordem de desenvolvimento

**Situação:** desenvolvimento inicial. A demonstração utilizará dados sintéticos. O Operix não está homologado nem pronto para empresas reais. Este é o guia curto; os detalhes ficam nos arquivos de cada módulo.

## 1. Visão

O Operix será um ERP operacional e financeiro para comércio físico, com **múltiplas empresas/filiais**, PDV simples no balcão e gestão administrativa mais abrangente. O primeiro cenário de referência tem **três filiais com administração central**, sem criar uma quarta unidade artificial.

O cliente poderá **contratar apenas os módulos necessários** e parametrizar regras operacionais por organização/filial. São controles distintos: módulos habilitados no contrato, permissões dos funcionários e regras de negócio. O atendimento poderá incluir diagnóstico, parametrização e treinamento. Preço, pacotes e suporte ainda precisam de definição.

**Sites de inspiração:** [Domtec/Yzidro](https://domtec.com.br/distribuidoras) (parametrização e gestão) e [Nex/Nextar](https://www.nextar.com.br/) (experiência de balcão) como referências principais; [Bling](https://www.bling.com.br/) e [Distribuidora Eficaz](https://www.distribuidoraeficaz.com.br/) como referências complementares. Não presumir integração entre esses sistemas. E-commerce, marketplaces e envios não são prioridades iniciais.

## 2. Tecnologias e interfaces

- **Backend:** Python, FastAPI e Pydantic.
- **Persistência:** PostgreSQL, SQLAlchemy, psycopg e Alembic.
- **Arquitetura:** monólito modular com API HTTP/JSON e isolamento por organização e filial.
- **Acesso planejado:** versão **web**, pelo navegador, e versão **instalada no computador** do cliente. O mesmo backend e as regras devem servir às duas. Tecnologia de interface, periféricos e operação offline continuam em avaliação.
- **Implementação atual:** persistência inicial de organizações e filiais. Clientes ainda estão em memória; autenticação, permissões e os fluxos principais ainda não estão implementados.

Mais detalhes: [Arquitetura e decisões técnicas](TECHNICAL.md).

## 3. Módulos e comportamentos

| Módulo | Comportamento principal |
| --- | --- |
| [Configuração e contratação](modules/00-configuracao.md) | Módulos opcionais, parametrização e implantação consultiva. |
| [Identidade e filiais](modules/01-identidade.md) | Organizações, filiais, usuários, login e permissões. |
| [Cadastros e estoque](modules/02-cadastros-estoque.md) | Clientes PF/PJ, produtos, preços e estoques por filial. |
| [Vendas e caixa](modules/03-comercial-caixa.md) | Orçamentos, pedidos, descontos, PDV, recebimentos e caixa. |
| [Financeiro e cobrança](modules/04-financeiro-cobranca.md) | Contas a pagar e receber, cobrança, boletos, cheques e bancos. |
| [Logística](modules/05-logistica.md) | Cargas, frota, romaneios, entregas parciais e prestação de contas. |
| [Relatórios](modules/06-relatorios.md) | Painéis operacionais e gerenciais por filial ou consolidados. |

**Situação dos módulos:** planejados, não concluídos. Emissão fiscal é etapa posterior sujeita a avaliação especializada e homologação.

## 4. Sequência de desenvolvimento

1. **D0 — Requisitos mínimos e decisões do incremento:** em levantamento.
2. **D1 — Identidade, login e controle de acesso:** não iniciado.
3. **D2 — Clientes, produtos e estoque:** não iniciado.
4. **D3 — Orçamentos e pedidos:** não iniciado.
5. **D4 — Caixa e recebimentos:** não iniciado.
6. **D5 — Contas de cliente e cobrança:** não iniciado.
7. **D6 — Logística e cargas:** não iniciado.
8. **D7 — Financeiro ampliado e boletos:** não iniciado.
9. **D8 — Demonstração integrada e validações:** não iniciado.

Os marcos D1–D5 constituem a primeira demonstração; D6–D8 ampliam o produto. A ordem e os critérios detalhados estão no [Roadmap](ROADMAP.md).

## 5. Como desenvolver e saber se concluiu

- Consultar o **módulo atual**, o recorte do [Roadmap](ROADMAP.md) e as partes relevantes de [TECHNICAL.md](TECHNICAL.md), não todos os documentos em toda tarefa.
- IA pode implementar e testar; o responsável descreve o comportamento, revisa resultados e resolve desafios pequenos para aprender ativamente.
- Uma etapa só termina após critérios de aceite e testes positivos/negativos, proteção dos acessos, consistência de dados e atualização da documentação.
- Nunca considerar uma tela ou código gerado como produto pronto. Uso com dados reais exige revisão de segurança, LGPD, testes, backups, homologação e autorização empresarial.
- Regras já discutidas permanecem nos arquivos específicos; decisões pendentes **não** devem virar comportamento presumido.

Diretrizes de contribuição: [AGENTS.md](../AGENTS.md).
