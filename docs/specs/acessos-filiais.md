# Operix — identidade, usuários e filiais

**Estado:** requisitos planejados; autenticação e permissões ainda não implementadas. Ver também [TECHNICAL.md](../TECHNICAL.md) e [ROADMAP.md](../ROADMAP.md).

### 1. Identidade, filiais e equipe
- Administrador principal cadastra/gerencia filiais, usuários, funções e permissões de ação.
- Usuário vinculado à organização e a uma ou mais filiais conforme função. Dono e financeiro podem consultar consolidação das três filiais quando autorizados.
- Perfis de referência: dono, administrador, financeiro, gerente, vendedor, caixa, estoque, conferente e logística. Permissões específicas são configuráveis e devem ser validadas no servidor.
- Abrir, movimentar e fechar caixa registra o usuário real em cada evento; **uma pessoa pode abrir e outra fechar**.
- Configurações comuns, como modelos de parcelamento de boletos, ficam disponíveis para todas as filiais da mesma organização.

#### Filiais e conta do cliente

- A organização tem três filiais, com administração central. A matriz não representa uma quarta loja.
- O cliente pertence à organização e possui filial de origem; seu cadastro pode ser compartilhado ou restrito. Se não compartilhado, outras filiais não consultam sua conta comercial, histórico, créditos ou débitos. Se compartilhado, somente filiais e usuários autorizados podem consultá-los ou realizar operações.
- O identificador de login planejado é e-mail; uma conta pertence a uma organização. O mesmo e-mail não identifica usuários distintos dentro dessa organização. Regra de repetição entre organizações e papel próprio de Dono seguem pendentes.
- Administração e financeiro podem ter visão consolidada; vendedor e caixa se limitam às filiais atribuídas. Alcance de filial não equivale a permissão para executar toda operação.

### Validações de negócio para D1

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
