
# API Documentation

## Models

| App name          | Model (in English)     |
| ----------------- | --------------------- |
| companies         | Company               |
| machines          | Machine               |
| sensors           | Sensor                |
| sensor_readings   | SensorReading         |
| occurrences       | Occurrence            |
| profiles          | Profile               |
| user_permissions  | UserMachinePermission |
| users             | User                  |

---

## API Endpoints

### Company API

| Method | Endpoint                  | Description                     |
|--------|---------------------------|---------------------------------|
| GET    | `/api/companies/`          | List all companies              |
| POST   | `/api/companies/`          | Create a new company            |
| GET    | `/api/companies/<id>/`     | Get details of a specific company |
| PUT    | `/api/companies/<id>/`     | Update all fields of a company  |
| PATCH  | `/api/companies/<id>/`     | Partial update of a company     |
| DELETE | `/api/companies/<id>/`     | Delete a company                |

#### Example: Create a Company (POST)

**URL:** `http://localhost:8000/api/companies/`

**Body:**
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
````

#### Example: List Companies (GET)

**URL:** `http://localhost:8000/api/companies/`

#### Example: Get Company by ID (GET)

**URL:** `http://localhost:8000/api/companies/1/`

---

### Machine API

| Method | Endpoint              | Description                    |
| ------ | --------------------- | ------------------------------ |
| GET    | `/api/machines/`      | List all machines              |
| POST   | `/api/machines/`      | Create a new machine           |
| GET    | `/api/machines/<id>/` | Get details of a machine       |
| PUT    | `/api/machines/<id>/` | Update all fields of a machine |
| PATCH  | `/api/machines/<id>/` | Partial update of a machine    |
| DELETE | `/api/machines/<id>/` | Delete a machine               |

#### Example: Create a Machine (POST)

**URL:** `http://localhost:8000/api/machines/`

**Body:**

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

### Occurrence API

| Method | Endpoint                 | Description                        |
| ------ | ------------------------ | ---------------------------------- |
| GET    | `/api/occurrences/`      | List all occurrences               |
| POST   | `/api/occurrences/`      | Create a new occurrence            |
| GET    | `/api/occurrences/<id>/` | Get details of an occurrence       |
| PUT    | `/api/occurrences/<id>/` | Update all fields of an occurrence |
| PATCH  | `/api/occurrences/<id>/` | Partial update of an occurrence    |
| DELETE | `/api/occurrences/<id>/` | Delete an occurrence               |

> **Note:** The `sensor_reading` field must reference an existing SensorReading ID.

#### Example: Create an Occurrence (POST)

**URL:** `http://localhost:8000/api/occurrences/`

**Body:**

```json
{
  "id": 1,
  "sensor_reading": 101,
  "sensor_id": 5,
  "occurrence_number": 3,
  "anomaly_type": "High Vibration",
  "severity": "High",
  "description": "Vibration levels above normal detected",
  "status": "Open"
}
```

---

## API Root Response Example

Request: `GET /api/`

Response:

```json
{
  "companies": "http://127.0.0.1:8000/api/companies/",
  "machines": "http://127.0.0.1:8000/api/machines/",
  "occurrences": "http://127.0.0.1:8000/api/occurrences/",
  "sensor-readings": "http://127.0.0.1:8000/api/sensor-readings/",
  "sensors": "http://127.0.0.1:8000/api/sensors/"
}
```

# API Endpoints Completos

---

## Companies (Empresas)

| Método | Endpoint               | Descrição                           |
| ------ | ---------------------- | ----------------------------------- |
| GET    | `/api/companies/`      | Lista todas as empresas             |
| POST   | `/api/companies/`      | Cria uma nova empresa               |
| GET    | `/api/companies/<id>/` | Detalha empresa específica          |
| PUT    | `/api/companies/<id>/` | Atualiza todos os campos da empresa |
| PATCH  | `/api/companies/<id>/` | Atualização parcial da empresa      |
| DELETE | `/api/companies/<id>/` | Deleta uma empresa                  |

---

## Machines (Máquinas)

| Método | Endpoint              | Descrição                           |
| ------ | --------------------- | ----------------------------------- |
| GET    | `/api/machines/`      | Lista todas as máquinas             |
| POST   | `/api/machines/`      | Cria uma nova máquina               |
| GET    | `/api/machines/<id>/` | Detalha máquina específica          |
| PUT    | `/api/machines/<id>/` | Atualiza todos os campos da máquina |
| PATCH  | `/api/machines/<id>/` | Atualização parcial da máquina      |
| DELETE | `/api/machines/<id>/` | Deleta uma máquina                  |

---

## Sensors (Sensores)

| Método | Endpoint             | Descrição                          |
| ------ | -------------------- | ---------------------------------- |
| GET    | `/api/sensors/`      | Lista todos os sensores            |
| POST   | `/api/sensors/`      | Cria um novo sensor                |
| GET    | `/api/sensors/<id>/` | Detalha sensor específico          |
| PUT    | `/api/sensors/<id>/` | Atualiza todos os campos do sensor |
| PATCH  | `/api/sensors/<id>/` | Atualização parcial do sensor      |
| DELETE | `/api/sensors/<id>/` | Deleta um sensor                   |

---

## Sensor Readings (Leituras de Sensores)

| Método | Endpoint                     | Descrição                           |
| ------ | ---------------------------- | ----------------------------------- |
| GET    | `/api/sensor-readings/`      | Lista todas as leituras             |
| POST   | `/api/sensor-readings/`      | Cria uma nova leitura               |
| GET    | `/api/sensor-readings/<id>/` | Detalha leitura específica          |
| PUT    | `/api/sensor-readings/<id>/` | Atualiza todos os campos da leitura |
| PATCH  | `/api/sensor-readings/<id>/` | Atualização parcial da leitura      |
| DELETE | `/api/sensor-readings/<id>/` | Deleta uma leitura                  |

---

## Occurrences (Ocorrências)

| Método | Endpoint                 | Descrição                              |
| ------ | ------------------------ | -------------------------------------- |
| GET    | `/api/occurrences/`      | Lista todas as ocorrências             |
| POST   | `/api/occurrences/`      | Cria uma nova ocorrência               |
| GET    | `/api/occurrences/<id>/` | Detalha ocorrência específica          |
| PUT    | `/api/occurrences/<id>/` | Atualiza todos os campos da ocorrência |
| PATCH  | `/api/occurrences/<id>/` | Atualização parcial da ocorrência      |
| DELETE | `/api/occurrences/<id>/` | Deleta uma ocorrência                  |

---

## Profiles (Perfis)

| Método | Endpoint              | Descrição                          |
| ------ | --------------------- | ---------------------------------- |
| GET    | `/api/profiles/`      | Lista todos os perfis              |
| POST   | `/api/profiles/`      | Cria um novo perfil                |
| GET    | `/api/profiles/<id>/` | Detalha perfil específico          |
| PUT    | `/api/profiles/<id>/` | Atualiza todos os campos do perfil |
| PATCH  | `/api/profiles/<id>/` | Atualização parcial do perfil      |
| DELETE | `/api/profiles/<id>/` | Deleta um perfil                   |

---

## User Machine Permissions (Permissões de Máquina por Usuário)

| Método | Endpoint                              | Descrição                             |
| ------ | ------------------------------------- | ------------------------------------- |
| GET    | `/api/user-machine-permissions/`      | Lista todas as permissões             |
| POST   | `/api/user-machine-permissions/`      | Cria uma nova permissão               |
| GET    | `/api/user-machine-permissions/<id>/` | Detalha permissão específica          |
| PUT    | `/api/user-machine-permissions/<id>/` | Atualiza todos os campos da permissão |
| PATCH  | `/api/user-machine-permissions/<id>/` | Atualização parcial da permissão      |
| DELETE | `/api/user-machine-permissions/<id>/` | Deleta uma permissão                  |

---

## Users (Usuários)

| Método | Endpoint           | Descrição                           |
| ------ | ------------------ | ----------------------------------- |
| GET    | `/api/users/`      | Lista todos os usuários             |
| POST   | `/api/users/`      | Cria um novo usuário                |
| GET    | `/api/users/<id>/` | Detalha usuário específico          |
| PUT    | `/api/users/<id>/` | Atualiza todos os campos do usuário |
| PATCH  | `/api/users/<id>/` | Atualização parcial do usuário      |
| DELETE | `/api/users/<id>/` | Deleta um usuário                   |

