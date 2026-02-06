# py-odoo-cli

Biblioteca Python desacoplada y reutilizable para interactuar con Odoo vía XML-RPC.  
Pensada para usar variables de entorno (`.env`) y configurarse fácilmente en cualquier proyecto.

## Características

- **Desacoplada**: La lógica principal está separada de la configuración y del uso.
- **Configurable**: Usa archivo `.env` para credenciales.
- **API sencilla**: Wrappers para `search_read`, `create`, `write`, `unlink`.
- **CLI incluido**: Punto de entrada `main.py` para pruebas y acciones rápidas.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/your-user/py-odoo-cli.git
   cd py-odoo-cli
   ```

2. Instala [UV](https://docs.astral.sh/uv/) y las dependencias:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   uv sync
   ```

3. Configura el entorno:
   Copia `.env.example` a `.env`:
   ```bash
   cp .env.example .env
   ```
   Edita `.env` con tus credenciales de Odoo:
   ```env
   ODOO_URL=https://tu-instancia.odoo.com
   ODOO_DB=tu-base-de-datos
   ODOO_USER=email@ejemplo.com
   ODOO_PASSWORD=tu-api-key
   ```

## Uso

### Como biblioteca

```python
from odoo_cli import OdooClient

# Carga credenciales desde .env automáticamente
client = OdooClient()

# Conectar
uid = client.connect()

# Buscar registros
partners = client.search_read('res.partner', [['customer_rank', '>', 0]], limit=5)
for p in partners:
    print(p['name'])
```

### Desde la CLI

Probar conexión:
```bash
uv run python main.py test-connection
```

Listar registros:
```bash
uv run python main.py list res.partner --limit 5 --fields name,email
```

Listar módulos instalados:
```bash
uv run python main.py list-modules
```

Listar parámetros del sistema:
```bash
uv run python main.py list-config
```

## Estructura

```
py-odoo-cli/
├── odoo_cli/          # Biblioteca core (reutilizable)
│   ├── client.py      # Cliente principal con wrappers
│   └── config.py      # Carga y validación de configuración
├── main.py            # CLI general para pruebas rápidas
├── knowledge/         # Base de conocimiento: proyectos y casos de uso específicos
│   └── hotel-trip-agency/  # Proyecto específico de ejemplo
│       ├── setup_timezone.py
│       └── debug_planning.py
└── tests/             # Tests unitarios
```

### Base de conocimiento (`knowledge/`)

La carpeta `knowledge/` contiene proyectos concretos y casos de uso que usan la biblioteca `odoo_cli`. Cada proyecto tiene su propia carpeta con:

- Scripts propios del proyecto
- Documentación y guías
- Configuraciones particulares si hace falta

Así la raíz del proyecto se mantiene ordenada y se organiza el conocimiento de cada implementación.
