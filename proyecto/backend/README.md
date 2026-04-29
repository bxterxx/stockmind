# StockMind API

API REST modular para gestión de inventario y stock.

## Estructura del Proyecto

```
StockMind/
├── entities/              # Modelos de base de datos (SQLAlchemy)
│   ├── __init__.py       # Export de todos los schemas (DTOs)
│   ├── usuario.py
│   ├── producto.py
│   ├── movimiento.py
│   ├── proveedor.py
│   └── categoria.py
├── services/              # Lógica de negocio
│   ├── usuario_service.py
│   ├── producto_service.py
│   ├── movimiento_service.py
│   ├── proveedor_service.py
│   └── categoria_service.py
├── controllers/          # Endpoints FastAPI
│   ├── usuario_controller.py
│   ├── producto_controller.py
│   ├── movimiento_controller.py
│   ├── proveedor_controller.py
│   └── categoria_controller.py
├── schemas/               # DTOs con Pydantic
│   └── __init__.py
├── database.py            # Configuración de BD
├── main.py                # Punto de entrada
├── .env                   # Variables de entorno
└── requirements.txt      # Dependencias
```

## Tecnologías

- **Python** 3.10+
- **FastAPI** - Framework web
- **SQLAlchemy** - ORM
- **PostgreSQL** - Base de datos
- **Pydantic** - Validación de datos
- **Uvicorn** - Servidor ASGI

## Configuración

1. **Crear y configurar `.env`:**

```env
PORT=3000
DEBUG=True
DB_ENGINE=postgres
DB_HOST=localhost
DB_PORT=5432
DB_NAME=stockmind
DB_USER=postgres
DB_PASSWORD=tu_password
SECRET_KEY=tu_secret_key
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
CORS_ORIGINS=*
```

2. **Instalar dependencias:**

```bash
pip install -r requirements.txt
```

3. **Crear la base de datos:**

```sql
CREATE DATABASE stockmind;
```

4. **Iniciar el servidor:**

```bash
python main.py
```

O con Uvicorn directamente:

```bash
uvicorn main:app --reload --port 3000
```

## Endpoints

### Usuarios
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/usuarios` | Listar todos |
| GET | `/usuarios/{id}` | Obtener por ID |
| POST | `/usuarios` | Crear |
| PUT | `/usuarios/{id}` | Actualizar |
| DELETE | `/usuarios/{id}` | Eliminar |

### Productos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/productos` | Listar todos |
| GET | `/productos/{id}` | Obtener por ID |
| POST | `/productos` | Crear |
| PUT | `/productos/{id}` | Actualizar |
| DELETE | `/productos/{id}` | Eliminar |

### Movimientos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/movimientos` | Listar todos |
| GET | `/movimientos/{id}` | Obtener por ID |
| POST | `/movimientos` | Crear |
| PUT | `/movimientos/{id}` | Actualizar |
| DELETE | `/movimientos/{id}` | Eliminar |

### Proveedores
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/proveedores` | Listar todos |
| GET | `/proveedores/{id}` | Obtener por ID |
| POST | `/proveedores` | Crear |
| PUT | `/proveedores/{id}` | Actualizar |
| DELETE | `/proveedores/{id}` | Eliminar |

### Categorías
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/categorias` | Listar todos |
| GET | `/categorias/{id}` | Obtener por ID |
| POST | `/categorias` | Crear |
| PUT | `/categorias/{id}` | Actualizar |
| DELETE | `/categorias/{id}` | Eliminar |

## Ejemplo de uso

```bash
# Crear un usuario
curl -X POST "http://localhost:3000/usuarios" \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Juan Pérez", "email": "juan@email.com", "password": "123456"}'

# Listar usuarios
curl "http://localhost:3000/usuarios"
```

## Documentación interactiva

FastAPI genera documentación automática en:
- **Swagger UI**: `http://localhost:3000/docs`
- **ReDoc**: `http://localhost:3000/redoc`
```

## Scripts

| Comando | Descripción |
|---------|-------------|
| `npm run dev` | Iniciar en modo desarrollo |
| `npm run build` | Compilar TypeScript |
| `npm start` | Iniciar producción |

## Endpoints

### Usuarios
- `GET /api/usuarios` - Listar todos
- `GET /api/usuarios/:id` - Obtener uno
- `POST /api/usuarios` - Crear
- `PUT /api/usuarios/:id` - Actualizar
- `DELETE /api/usuarios/:id` - Eliminar

### Productos
- `GET /api/productos`
- `GET /api/productos/:id`
- `POST /api/productos`
- `PUT /api/productos/:id`
- `DELETE /api/productos/:id`

### Movimientos
- `GET /api/movimientos`
- `GET /api/movimientos/:id`
- `POST /api/movimientos`
- `PUT /api/movimientos/:id`
- `DELETE /api/movimientos/:id`

### Proveedores
- `GET /api/proveedores`
- `GET /api/proveedores/:id`
- `POST /api/proveedores`
- `PUT /api/proveedores/:id`
- `DELETE /api/proveedores/:id`

### Categorías
- `GET /api/categorias`
- `GET /api/categorias/:id`
- `POST /api/categorias`
- `PUT /api/categorias/:id`
- `DELETE /api/categorias/:id`

## Siguientes Pasos

1. **Instalar dependencias**: `npm install`
2. **Configurar base de datos**: Crear la base de datos en PostgreSQL/MySQL
3. **Conectar TypeORM**: Actualizar `src/config/index.ts` con la lógica de conexión
4. **Iniciar**: `npm run dev`