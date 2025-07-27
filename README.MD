
### MODELS

| App name          | Model (em inglês)     |
| ----------------- | --------------------- |
| companies         | Company               |
| machines          | Machine               |
| sensors           | Sensor                |
| sensor\_readings  | SensorReading         |
| occurrences       | Occurrence            |
| profiles          | Profile               |
| user\_permissions | UserMachinePermission |
| users             | User                  |


### Os end-points

#### 🔗 Endpoint base da API Company:

```
GET     /api/companies/           → Lista todas as empresas
POST    /api/companies/           → Cria uma nova empresa
GET     /api/companies/<id>/      → Detalha uma empresa específica
PUT     /api/companies/<id>/      → Atualiza todos os campos da empresa
PATCH   /api/companies/<id>/      → Atualiza parcialmente a empresa
DELETE  /api/companies/<id>/      → Deleta uma empresa
```

---

### 📌 Exemplo prático:

#### ➕ Criar nova empresa (POST)

**URL:** `http://localhost:8000/api/companies/`

**JSON:**

```json
{
  "id": 1,
  "name": "Teiús Tecnologia",
  "cnpj": "12345678000199",
  "address": "Rua Exemplo, 1000 - Fortaleza",
  "email": "contato@teiustech.com",
  "contract_date": "2024-01-01",
  "active": "Y"
}
```

#### ✅ Buscar todas (GET)

**URL:** `http://localhost:8000/api/companies/`

#### 🔍 Buscar por ID (GET)

**URL:** `http://localhost:8000/api/companies/1/`

### Machines

* `GET /api/machines/` — lista máquinas
* `POST /api/machines/` — cria máquina
* `GET /api/machines/{id}/` — detalhes de máquina
* `PUT /api/machines/{id}/` — atualiza máquina
* `PATCH /api/machines/{id}/` — atualiza parcialmente
* `DELETE /api/machines/{id}/` — deleta máquina
