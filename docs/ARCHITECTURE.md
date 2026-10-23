# Operix — Arquitetura e stack

**Estado:** documento técnico evolutivo. Requisitos em [SPEC.md](SPEC.md); prioridades em [ROADMAP.md](ROADMAP.md).

## Estratégia

**Monólito modular** com API HTTP/JSON e PostgreSQL. Os limites internos evoluirão pelos domínios do produto, sem microserviços ou camadas artificiais no estágio atual. A separação arquitetural deve preservar transações consistentes entre pedidos, pagamentos, estoque e expedição.

## Stack e maturidade

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

## Componentes existentes

- `app/main.py`: API inicial com saúde, clientes, organizações e filiais.
- `app/database.py`: conexão e sessões SQLAlchemy via `DATABASE_URL`.
- `app/models.py`: entidades `Organizacao` e `Filial`, com relacionamento.
- `alembic/`: controle versionado da estrutura de banco.
- `app/main.py` ainda utiliza **lista em memória para clientes**; apenas organizações e filiais usam persistência no PostgreSQL.

**Ainda inexistentes:** autenticação, RBAC, isolamento efetivo entre organizações, persistência real de clientes, testes automatizados, módulos transacionais completos, interface de negócio, integrações bancárias e implantação.

## Domínios previstos

Identidade e filiais; clientes; produtos e estoque; comercial (orçamentos/pedidos); conta do cliente e recebimentos; caixa; cobranças; logística/cargas; financeiro central; relatórios. A estrutura física de pastas será adaptada conforme funcionalidades forem implementadas.

## Regras técnicas transversais

- **Autorização:** identidade autenticada e escopo por organização/filial em cada consulta e comando; o front-end não substitui controles de API. Testar acessos cruzados antes de disponibilizar dados reais.
- **Integridade:** operações financeiras e de estoque devem manter transações, vínculos e histórico; definir representação exata para valores monetários (Decimal/NUMERIC ou centavos inteiros) antes do módulo financeiro; evitar `float`.
- **Idempotência:** impedir cobrança, recebimento, reserva ou baixa duplicados por requisições repetidas ou concorrentes.
- **Auditoria:** identificar usuário, data, contexto e motivo de eventos relevantes; estornos e correções não apagam o histórico operacional.
- **Fronteiras de domínio:** venda não equivale a recebimento; recebimento não equivale a entrega; dinheiro com motorista não é dinheiro conferido no caixa; cheque recebido não é compensado; parcela prevista não é boleto bancário registrado.
- **Estoque/logística:** quantidades são controladas por item e localização, incluindo retirada, caminhão, retorno e entregas parciais. Um pedido pode estar em múltiplas cargas.
- **Qualidade:** testes unitários, integração e autorização devem acompanhar os módulos críticos; automação CI pode ser introduzida com a suíte de testes, sem alegar que já existe.

## Ambientes e entrada em produção

Etapa atual: desenvolvimento local e demonstração com dados sintéticos. Produção exige aprovação formal, revisão de segurança e LGPD, integração bancária homologada, testes de carga e concorrência, backup e restauração, monitoramento, plano de rollback e suporte. Nenhum desses controles é considerado concluído por estar documentado.
