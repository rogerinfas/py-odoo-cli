<!--
  py-odoo-cli · Cliente XML-RPC para Odoo
  Diseño sobrio y profesional. Sin emojis.
-->

<div align="center">

# py-odoo-cli

**Cliente Python desacoplado para Odoo vía XML-RPC**

---

</div>

Biblioteca reutilizable que centraliza la interacción con Odoo usando variables de entorno (`.env`) y una API mínima y predecible.

---

## Características

| Aspecto        | Descripción |
|----------------|-------------|
| **Desacoplada** | Lógica core separada de configuración y casos de uso. |
| **Configurable** | Credenciales y opciones vía `.env`. |
| **API sencilla** | Wrappers para `search_read`, `create`, `write`, `unlink`. |
| **CLI incluido** | Punto de entrada `main.py` para pruebas y tareas rápidas. |

---

## Instalación

**1. Clonar el repositorio**

```bash
git clone https://github.com/your-user/py-odoo-cli.git
cd py-odoo-cli
```

**2. Instalar [UV](https://docs.astral.sh/uv/) y dependencias**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
```

**3. Configurar entorno**

Copia `.env.example` a `.env` y ajusta credenciales:

```bash
cp .env.example .env
```

Contenido mínimo de `.env`:

```env
ODOO_URL=https://tu-instancia.odoo.com
ODOO_DB=tu-base-de-datos
ODOO_USER=email@ejemplo.com
ODOO_PASSWORD=tu-api-key
```

---

## Uso

### Como biblioteca

```python
from odoo_cli import OdooClient

client = OdooClient()
uid = client.connect()

partners = client.search_read(
    'res.partner',
    [['customer_rank', '>', 0]],
    limit=5
)
for p in partners:
    print(p['name'])
```

### Desde la CLI

| Acción              | Comando |
|---------------------|---------|
| Probar conexión     | `uv run python main.py test-connection` |
| Listar registros    | `uv run python main.py list res.partner --limit 5 --fields name,email` |
| Módulos instalados  | `uv run python main.py list-modules` |
| Parámetros sistema  | `uv run python main.py list-config` |

---

## Estructura del proyecto

```
py-odoo-cli/
├── odoo_cli/              # Biblioteca core
│   ├── client.py          # Cliente y wrappers
│   └── config.py          # Carga y validación
├── main.py                # CLI general
├── knowledge/             # Base de conocimiento (proyectos y casos de uso)
│   └── hotel-trip-agency/
│       ├── setup_timezone.py
│       └── debug_planning.py
└── tests/
```

### Carpeta `knowledge/`

Contiene proyectos concretos y casos de uso que usan `odoo_cli`. Cada proyecto vive en su propia carpeta con scripts, documentación y, si aplica, configuraciones propias. La raíz del repo se mantiene limpia y el conocimiento queda organizado por implementación.

Más detalles en [knowledge/README.md](knowledge/README.md).

---

<div align="center">

*py-odoo-cli — Servicio del CLI.*

</div>
