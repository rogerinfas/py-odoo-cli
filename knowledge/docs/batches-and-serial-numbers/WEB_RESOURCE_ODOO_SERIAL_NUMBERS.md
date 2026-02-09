---
title: Números de serie en Odoo saas‑18.4
source: https://www.odoo.com/documentation/saas-18.4/es/applications/inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers.html
---

# Números de serie

Los **números de serie** son una de las dos formas de identificar y rastrear productos en Odoo (junto con los **lotes**).  
Un número de serie es un identificador **único** asignado a cada unidad para distinguirla de las demás.

En Odoo saas‑18.4:

- Los números de serie pueden contener números, letras y otros caracteres.
- Permiten rastrear:
  - **Ubicación actual** del producto.
  - **Historial de movimientos**.
  - **Fechas de vencimiento** asociadas.
- Son clave para:
  - Servicio posventa (garantías, reparaciones, devoluciones).
  - Retiros de producto.
  - Auditorías y trazabilidad regulatoria.

> Referencias relacionadas:
> - [Lot numbers — Odoo saas‑18.4](https://www.odoo.com/documentation/saas-18.4/es/applications/inventory_and_mrp/inventory/product_management/product_tracking/lots.html)
> - [Expiration dates — Odoo saas‑18.4](https://www.odoo.com/documentation/saas-18.4/es/applications/inventory_and_mrp/inventory/product_management/product_tracking/expiration_dates.html)

---

## 1. Habilitar lotes y números de serie

### 1.1. Ajuste global de trazabilidad

1. Ir a `Inventario ‣ Configuración ‣ Ajustes`.
2. Sección **Trazabilidad**.
3. Activar **Lotes y números de serie (Lots & Serial Numbers)**.
4. Guardar cambios.

Esto permite que el inventario se gestione con lotes y/o números de serie.

### 1.2. Por tipo de operación

Para controlar dónde se **crean** o solo se **usan** números de serie:

1. Ir a `Inventario ‣ Configuración ‣ Tipos de operación`.
2. Abrir un tipo (por ejemplo, **Recepciones**, **Órdenes de entrega**, **Fabricación**).
3. En la sección **Lotes/Números de serie**:
   - **Crear nuevos (Create New)**: permite generar números de serie nuevos en esa operación (típico en Recepciones).
   - **Usar existentes (Use Existing)**: fuerza a usar solo números ya existentes (típico en Entregas).
4. Guardar.

---

## 2. Configurar seguimiento por número de serie en productos

1. Ir a `Inventario ‣ Productos ‣ Productos`.
2. Seleccionar el producto.
3. En la pestaña **Información general**:
   - Activar **Seguir inventario (Track Inventory)**.
   - En el campo de seguimiento, elegir **Por número de serie único (By Unique Serial Number)**.
4. Guardar.

Con esto:

- Cada unidad de ese producto tendrá **un número de serie único**.
- Podrás asignar números de serie en recepciones, entregas, fabricación y ajustes.

---

## 3. Asignar números de serie

Los números de serie se pueden asignar en varios puntos del flujo:

- A productos **ya en stock** sin número asignado.
- En **recepciones** (entradas).
- En **órdenes de entrega** (salidas).
- En **órdenes de fabricación**.
- En **ajustes de inventario**.

### 3.1. Crear números de serie para productos ya en stock

1. Ir a `Inventario ‣ Productos ‣ Lotes/Números de serie`.
2. Hacer clic en **Nuevo**.
3. Odoo genera un **Lote/Número de serie** de forma automática (editable).
4. En **Producto**, seleccionar el producto.
5. Opcionalmente:
   - Ajustar **Cantidad en mano (On Hand Quantity)**.
   - Definir **Referencia interna** (SKU alternativo).
   - Seleccionar **Compañía**.
   - Añadir **Descripción** en la pestaña correspondiente.
6. Guardar.

Después:

- Ir a `Inventario ‣ Productos ‣ Productos`, abrir el producto y usar el botón inteligente **Lotes/Números de serie** para ver los números asociados.

---

### 3.2. Crear/asignar números de serie en recepciones y entregas

En **Recepciones** (`Inventario ‣ Operaciones ‣ Recepciones`) y **Órdenes de entrega** (`Inventario ‣ Operaciones ‣ Entregas`) se usan dos interfaces:

#### A) Campo directo de número de serie

- Mostrar la columna **Números de serie** desde el icono de ajustes de columnas.
- Escribir o seleccionar el número de serie directamente en la línea de producto.

#### B) Ventana de **Operaciones detalladas**

1. En la línea de producto, hacer clic en **Detalles (Details)**.
2. Se abre el popup **Operaciones detalladas** con columnas para:
   - **Lote/Número de serie**.
   - Ubicaciones.
   - Cantidades.

Desde aquí hay tres formas principales:

##### 3.2.1. Añadir una línea (Add a line)

- Pulsar **Add a line**.
- Escribir el valor de **Lote/Número de serie**.
- Ajustar la **Cantidad** (normalmente 1 en números de serie).

##### 3.2.2. Generate Serials/Lots

- Pulsar **Generate Serials/Lots**.
- Indicar:
  - **First Serial Number** (primer número de la secuencia).
  - **Number of SN** (cuántos números generar).
  - **Keep current lines** para conservar o no las líneas ya existentes.
- Pulsar **Generate**.

Odoo:

- Crea en bloque los números de serie.
- Ajusta la **Cantidad** en función de la cantidad generada (puede superar la demanda si así se configura).

##### 3.2.3. Import Serials/Lots

- Pulsar **Import Serials/Lots**.
- En el popup **Import Serials**, pegar la lista de números (uno por línea) en **Lots/Serial numbers**.
- (Opcional) Marcar **Keep current lines** para añadir, o desmarcar para reemplazar.
- Pulsar **Generate**.

Esto es ideal cuando se copian números desde una hoja de cálculo.

---

### 3.3. Operaciones detalladas / Moves

Además del popup de detalles:

1. En una recepción o entrega, pulsar el botón inteligente **Moves (Movimientos)**.
2. En la vista de movimientos, usar la columna **Lote/Número de serie** para:
   - Revisar los números asignados.
   - Modificarlos manualmente si es necesario.

Esta vista da un resumen de los números de serie usados en todos los movimientos relacionados.

---

## 4. Mostrar números de serie en notas de entrega

Para que los números de serie aparezcan en el PDF de la nota de entrega:

1. Ir a `Inventario ‣ Configuración ‣ Ajustes`.
2. En **Trazabilidad**, activar **Mostrar lotes y números de serie en las notas de entrega (Display Lots & Serial Numbers on Delivery Slips)**.
3. Guardar.

Después:

1. En una orden de entrega validada, pulsar **Acciones ‣ Imprimir ‣ Nota de entrega**.
2. En el documento PDF, la columna **Lote/Número de serie** listará los números asociados a cada producto.

---

## 5. Trazabilidad y reporting

### 5.1. Tablero de Lotes/Números de serie

1. Ir a `Inventario ‣ Productos ‣ Lotes/Números de serie`.
2. Verás el **tablero de Lotes/Números de serie**, donde:
   - Cada fila representa un lote o número de serie.
   - Se puede expandir para ver cantidades, ubicaciones y producto.

Acciones útiles:

- **Group By / Agrupar por**:
  - Producto.
  - Lote/Número de serie.
  - Fecha de caducidad (si se usa expiración).
- Hacer clic en una línea para abrir el formulario del número de serie.
- Desde el formulario:
  - Botón **Ubicación (Location)** → stock actual.
  - Botón **Trazabilidad (Traceability)** → todos los movimientos donde aparece ese número.

### 5.2. Otros reportes que usan números de serie

En `Inventario ‣ Reportes` hay informes que permiten filtrar/agrupuar por **Lote/Número de serie**:

- **Ubicaciones**.
- **Historial de movimientos (Moves history)**.
- **Análisis de movimientos (Moves analysis)**.

Esto permite, por ejemplo:

- Ver todos los movimientos de un número de serie concreto.
- Analizar salidas/entradas por rangos de números de serie.

---

## 6. Referencia de imágenes (saas‑18.4)

La documentación de Odoo saas‑18.4 incluye capturas para:

- Activar **Lots & Serial Numbers**.
- Configurar el producto con **By Unique Serial Number**.
- Usar el campo **Serial Numbers** en recepciones/entregas.
- El popup **Detailed Operations** (Add a line / Generate Serials / Import Serials).
- El tablero de **Lots/Serial Numbers** y los reportes.

Para replicar el estilo de `WEB_RESOURCE_CERTIFICADO_DIGITAL_SUNAT.md`:

1. Abre la página oficial:  
   `https://www.odoo.com/documentation/saas-18.4/es/applications/inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers.html`
2. Inspecciona cada captura con las herramientas de desarrollador.
3. Copia las URLs de las imágenes (normalmente bajo `/documentation/saas-18.4/_images/...`).
4. Descarga los archivos a `knowledge/docs/batches-and-serial-numbers/imgs/`, por ejemplo:

```bash
cd knowledge/docs/batches-and-serial-numbers
mkdir -p imgs
curl -o imgs/serial-numbers-setting.png "https://www.odoo.com/documentation/saas-18.4/_images/serial-numbers-setting.png"
```

5. En este mismo MD, referencia las imágenes con rutas relativas:

```markdown
![Ajuste de trazabilidad por números de serie](imgs/serial-numbers-setting.png)
```

De esta manera tendrás la **documentación actualizada a saas‑18.4** y las imágenes disponibles en local, con un patrón idéntico al recurso de SUNAT.


