
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

#### 🔗 Endpoint base da API Machine:

```
GET     /api/machines/           → Lista todas as máquinas  
POST    /api/machines/           → Cria uma nova máquina  
GET     /api/machines/<id>/      → Detalha uma máquina específica  
PUT     /api/machines/<id>/      → Atualiza todos os campos da máquina  
PATCH   /api/machines/<id>/      → Atualiza parcialmente a máquina  
DELETE  /api/machines/<id>/      → Deleta uma máquina  
```

---

### 📌 Exemplo prático:

#### ➕ Criar nova máquina (POST)

**URL:** `http://localhost:8000/api/machines/`

**JSON:**

```json
{
  "id": 1,
  "name": "Compressor de Ar 500L",
  "serial_number": "ABC123456789",
  "model": "Model X500",
  "manufacturer": "AirTech",
  "location": "Setor 1 - Galpão A",
  "installation_date": "2023-07-15",
  "status": "Operando",
  "last_maintenance": "2024-01-10",
  "next_maintenance": "2024-07-10"
}
```

---

#### ✅ Buscar todas (GET)

**URL:** `http://localhost:8000/api/machines/`

---

#### 🔍 Buscar por ID (GET)

**URL:** `http://localhost:8000/api/machines/1/`

---

#### 🔁 Atualizar máquina (PUT)

**URL:** `http://localhost:8000/api/machines/1/`

**JSON:**

```json
{
  "id": 1,
  "name": "Compressor de Ar 500L",
  "serial_number": "ABC123456789",
  "model": "Model X600",
  "manufacturer": "AirTech",
  "location": "Setor 2 - Galpão B",
  "installation_date": "2023-07-15",
  "status": "Parado",
  "last_maintenance": "2024-01-10",
  "next_maintenance": "2024-12-10"
}
```

---

#### 🛠 Atualizar parcialmente (PATCH)

**URL:** `http://localhost:8000/api/machines/1/`

**JSON:**

```json
{
  "status": "Em manutenção"
}
```

---

#### ❌ Deletar (DELETE)

**URL:** `http://localhost:8000/api/machines/1/`
