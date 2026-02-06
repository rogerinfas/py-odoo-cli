# py-odoo-cli

A strictly decoupled, reusable Python library for Odoo XML-RPC interactions.  
Designed to work with environment variables (`.env`) for easy configuration in any project.

## Features

- **Decoupled**: Core logic is separated from configuration and usage.
- **Configurable**: Uses `.env` file for credentials.
- **Simple API**: Easy wrappers for `search_read`, `create`, `write`, `unlink`.
- **CLI Included**: Defines a `main.py` entry point for testing and quick actions.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-user/py-odoo-cli.git
   cd py-odoo-cli
   ```

2. Install [UV](https://docs.astral.sh/uv/) and dependencies:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   uv sync
   ```

3. Configure environment:
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your Odoo credentials:
   ```env
   ODOO_URL=https://your-instance.odoo.com
   ODOO_DB=your-db
   ODOO_USER=email@example.com
   ODOO_PASSWORD=your-api-key
   ```

## Usage

### As a Library

```python
from odoo_cli import OdooClient

# Automatically loads credentials from .env
client = OdooClient()

# Connect
uid = client.connect()

# Search records
partners = client.search_read('res.partner', [['customer_rank', '>', 0]], limit=5)
for p in partners:
    print(p['name'])
```

### via CLI

Check connection:
```bash
uv run python main.py test-connection
```

List records:
```bash
uv run python main.py list res.partner --limit 5 --fields name,email
```

List installed modules:
```bash
uv run python main.py list-modules
```

List system configurations:
```bash
uv run python main.py list-config
```

## Structure

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

### Base de Conocimiento (`knowledge/`)

La carpeta `knowledge/` contiene proyectos específicos y casos de uso que utilizan la biblioteca `odoo_cli`. Cada proyecto tiene su propia carpeta con:

- Scripts específicos del proyecto
- Documentación y guías
- Configuraciones particulares si es necesario

Esta estructura mantiene la raíz del proyecto limpia y organiza el conocimiento adquirido de cada implementación.
