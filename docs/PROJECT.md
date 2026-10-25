# Operix — visão do produto

**Objetivo:** ERP modular para comércio físico, do balcão à gestão empresarial. Cada empresa contrata o que usa, com regras parametrizadas para sua operação. Projeto em desenvolvimento; **não está pronto para produção**.

## O que será vendido

**Módulos comerciais:** **Vendas, Estoque, CRM, Caixa, Financeiro, Fiscal, Contábil, Frota, Transportes, BI e Mobile**. Veja [o que cada módulo faz e seu estágio](MODULOS.md).

- **Base compartilhada (não vendida como módulo separado):** organizações, filiais, cadastros comuns, usuários, login, permissões, segurança e integrações internas.
- **Contratação modular:** habilitar somente os módulos escolhidos. Contratação, autorização de funcionários e parametrização são coisas distintas. Pacotes, dependências e valores ainda não foram definidos.
- **Implantação:** entender o processo da empresa, configurar as regras pertinentes e treinar a equipe.

**Referências:** [Domtec/Yzidro](https://domtec.com.br/distribuidoras) (gestão e parametrização), [Nex/Nextar](https://www.nextar.com.br/) (PDV intuitivo), [Bling](https://www.bling.com.br/) e [Distribuidora Eficaz](https://www.distribuidoraeficaz.com.br/) (ideias complementares). Não pressupor integração ou uso específico entre elas.

## Como o cliente acessará

- **Web:** navegador.
- **Desktop:** aplicativo instalado no computador; mesma plataforma e dados da versão web.
- **Mobile:** acesso/aplicações para celular a definir; poderá ter funcionalidades comerciais próprias, especialmente para uso externo. Acesso pelo celular não é automaticamente um módulo cobrado.
- **Offline:** necessidade e comportamento ainda não definidos.

## Tecnologia

Python, FastAPI, Pydantic, PostgreSQL, SQLAlchemy e Alembic. Arquitetura: **monólito modular com API compartilhada**. Interfaces web/desktop ainda não escolhidas. Detalhes reservados para a IA: [TECHNICAL.md](TECHNICAL.md).

## Ordem de construção

| Etapa | Foco |
| --- | --- |
| **D0–D1** | Validar o recorte; organizações, filiais, usuários e segurança (base). |
| **D2** | Clientes, produtos e estoque. |
| **D3** | Vendas: orçamentos, pedidos e base do PDV. |
| **D4** | Caixa, recebimentos e pagamentos mistos. |
| **D5** | Contas de clientes e cobrança; começar a ampliar Financeiro/CRM. |
| **D6–D7** | Frota/Transportes e Financeiro avançado conforme demanda. |
| **D8** | Testar a demonstração integrada. |
| **Depois, por validação** | Evoluir BI e Mobile; especificar Fiscal e Contábil com especialistas. |

**Situação real:** API inicial de organizações/filiais com persistência; clientes ainda em memória. Login, controle de acesso, módulos comerciais completos, telas e aplicativos não foram implementados.

**Próximo passo:** finalizar as decisões mínimas de D1 e desenvolver/testar uma entrega pequena de identidade. [Roadmap técnico detalhado](ROADMAP.md).

## Como trabalharemos com IA

Você define e testa o comportamento; a IA implementa incrementos pequenos, explica pontos centrais e cria testes. Você resolve um desafio curto relacionado ao incremento para aprender. A IA consulta **apenas** o módulo comercial pertinente, as [especificações existentes](specs/) e os detalhes técnicos necessários. **Não considerar concluído sem testes e revisão.** Uso real exige segurança, LGPD, backups, homologação e, onde aplicável, validação fiscal/contábil.
