# MySystemDown

Este repositório contém uma **API REST** do projeto **MySystemDown**, um sistema centralizado para monitorar a saúde de múltiplos serviços locais.
O objetivo do sistema é permitir o acompanhamento do status, disponibilidade e integridade de serviços internos de forma unificada.

---

## 🚀 Tecnologias
- Python
- Django Rest Framework
- PostgreSQL

---

## ⚙️ Configuração do ambiente

### 1. Variáveis de ambiente
Crie um arquivo `.env` baseado no `.env.example`:

```bash
cp .env.example .env
```

### 2. Instale as dependências
Para o projeto funcionar sem nenhum problema é necessário baixar as dependências com as devidas versões listadas no `pyproject.toml`. Recomendo utilizar um ambiente virtualizado para evitar problemas.

``` shell
pip install .
```

### 3. Execute as migrations e as seeds
O sistema necessita de alguns registros previamente inseridos. Para isso é necessário rodar os seguintes script dentro da pasta `/src`.

``` shell
python manage.py migrate_schemas --shared
```

``` shell
python manage.py seed_tenants
```

``` shell
python manage.py seed_roles
```

``` shell
python manage.py seed_group_permissions
```


### 4. Execução
Para executar o projeto é necessário estar dentro da pasta `/src`. O padrão para execução da API Rest é a porta 8000.

``` shell
python manage.py runserver 8000
```