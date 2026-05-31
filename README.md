# Engenharia de Dados Pipeline

Projeto de estudos em Engenharia de Dados simulando uma arquitetura moderna de dados com ingestão, transformação, armazenamento analítico e visualização.

## Tecnologias

* Apache Airflow
* PostgreSQL (Neon)
* Python
* Docker
* BigQuery
* Power BI

## Arquitetura

Neon PostgreSQL
↓
Airflow
↓
Raw
↓
Silver
↓
Gold
↓
BigQuery
↓
Power BI

## Objetivos

* Construir pipelines ETL e ELT
* Aplicar arquitetura Medallion
* Orquestrar processos com Airflow
* Armazenar dados analíticos no BigQuery
* Criar dashboards no Power BI

## Status do Projeto

* [x] Docker configurado
* [x] Airflow configurado
* [x] Primeira DAG criada
* [ ] Integração com Neon PostgreSQL
* [ ] Camada Raw
* [ ] Camada Silver
* [ ] Camada Gold
* [ ] BigQuery
* [ ] Dashboard Power BI

## Estrutura

```text
engenharia-dados/
│
├── airflow/
├── scripts/
├── data/
│   ├── raw/
│   ├── silver/
│   └── gold/
│
└── docker-compose.yml
```
