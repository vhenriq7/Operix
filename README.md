# Operix

> SaaS de gestão operacional para empresas com múltiplas filiais.

O **Operix** é um projeto de estudo e portfólio focado em desenvolvimento back-end com **Python, FastAPI, PostgreSQL e SQL**.

A proposta é modelar um problema empresarial real: integrar vendas, clientes, conta do cliente, estoque, transferências entre filiais, montagem de cargas, expedição e entregas em uma única plataforma.

## Objetivos do projeto

- Aprender back-end construindo um sistema realista.
- Praticar Python e SQL em contexto de negócio.
- Aprender modelagem relacional e PostgreSQL.
- Construir APIs REST com FastAPI.
- Aplicar autenticação, autorização e multi-tenancy.
- Trabalhar com testes, Git, Docker e deploy.
- Criar um projeto de portfólio com evolução documentada.

## Stack planejada

- **Python**
- **FastAPI**
- **PostgreSQL**
- **SQL**
- **SQLAlchemy**
- **Alembic**
- **Pydantic**
- **Pytest**
- **Git & GitHub**
- **Docker**

## Módulos planejados

- Administração de organizações e filiais
- Usuários, papéis e permissões
- Clientes e conta comercial
- Produtos, preços e estoque por filial
- Orçamentos e pedidos
- Pagamentos, créditos, débitos e devoluções
- Comissões
- Transferências entre filiais
- Veículos, cargas e expedição
- Tentativas de entrega
- Dashboards gerenciais

## Estado atual

**Fase 2 — HTTP, APIs e FastAPI (em andamento).**

A estrutura inicial do back-end já está funcionando com FastAPI. O projeto está praticando os fundamentos de HTTP e APIs antes de conectar um banco de dados.

Atualmente já existem endpoints para:

- verificar se a API está em execução;
- realizar health check;
- listar clientes em memória;
- consultar cliente por `customer_id`;
- criar cliente com validação de dados usando Pydantic.

Os dados de clientes ainda são temporários e armazenados apenas em memória. A persistência com PostgreSQL será introduzida em uma fase posterior do roadmap.

## Documentação

- [Especificação do projeto](PROJECT_SPEC.md) — define o produto, as regras de negócio e os requisitos do Operix.
- [Roadmap de aprendizagem](LEARNING_ROADMAP.md) — define a ordem de estudo e implementação do projeto.
- [Instruções para agentes](AGENTS.md) — define como Codex e outros assistentes devem trabalhar neste repositório.

## Princípio do projeto

> Primeiro simples, correto e compreensível. Depois melhorado, refatorado e otimizado.

---

Projeto desenvolvido para estudo e portfólio.
