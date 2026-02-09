---
title: Reasignar lotes y números de serie en Odoo saas‑18.4
source: https://www.odoo.com/documentation/saas-18.4/es/applications/inventory_and_mrp/inventory/product_management/product_tracking/reassign.html
---

# Reasignar lotes y números de serie

Cambiar la configuración de seguimiento de un producto (**sin tracking → por lotes / por número de serie**) cuando ya existe stock puede generar registros inconsistentes si no se hace correctamente.

Odoo saas‑18.4 propone un flujo seguro basado en **ajustes de inventario** para:

- Eliminar los movimientos antiguos **sin** lotes/series.
- Volver a introducir el stock **con** los lotes/números de serie correctos.

> Referencias:
> - [Serial numbers — Odoo saas‑18.4](https://www.odoo.com/documentation/saas-18.4/es/applications/inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers.html)
> - [Lot numbers — Odoo saas‑18.4](https://www.odoo.com/documentation/saas-18.4/es/applications/inventory_and_mrp/inventory/product_management/product_tracking/lots.html)

---

## 1. Cambiar el tracking del producto

1. Ir a `Inventario ‣ Productos ‣ Productos`.
2. Seleccionar el producto.
3. En **Información general**:
   - Activar **Seguir inventario (Track Inventory)**.
   - Elegir **By Lots** o **By Unique Serial Number**, según corresponda.

Al guardar, Odoo muestra un mensaje indicando que se requiere un **ajuste de inventario** para asignar lotes/números de serie al stock ya existente.

---

## 2. Primer ajuste: poner el stock a cero (sin tracking)

1. En el formulario del producto, pasar el ratón sobre **Cantidad disponible (Quantity On Hand)**.
2. Hacer clic en el enlace **Update** / **Actualizar** que aparece.
3. En la pantalla de ajuste de inventario:
   - Establecer **On Hand Quantity** a `0` en todas las ubicaciones para ese producto.
4. Guardar.

Con esto:

- Se corrige el stock teórico a 0.
- Los movimientos anteriores sin tracking quedan “cerrados” desde el punto de vista de existencias actuales.

> Nota: Si el producto está en varias ubicaciones, asegúrate de dejar la suma total en 0 (puede requerir varias líneas).

---

## 3. Segundo ajuste: volver a introducir el stock con lotes/series

Ahora se vuelve a introducir el stock real, pero esta vez **con** la información de lotes o números de serie correcta.

1. Desde la misma pantalla de **Update Quantity**:
   - Pulsar **Nuevo (New)** para crear nuevas líneas de stock.
2. Para cada combinación:
   - Elegir **Ubicación**.
   - Indicar la **Cantidad** real.
   - En **Lote/Número de serie (Lot/Serial Number)**:
     - Crear un nuevo valor, o
     - Elegir uno existente.
3. Guardar.

Repite hasta cubrir todo el stock real del producto con los lotes/números de serie deseados.

> Truco: el botón **History** en la línea de ajuste ayuda a ver el historial y las cantidades originales antes de ponerlas a 0.

---

## 4. Resultado y buenas prácticas

Después de estos dos ajustes:

- El inventario actual refleja:
  - Cantidades correctas.
  - Lotes/números de serie correctos.
- Toda la trazabilidad futura (recepciones, entregas, fabricación) se hará ya **con** tracking activado.

Recomendaciones:

- Hacer esta operación en momentos de poca actividad (ej. fuera del horario punta).
- Anotar en el ajuste (campo **Descripción / Reason**) que se trata de un proceso de “Reasignación de lotes/números de serie”.
- Revisar los reportes de:
  - **Moves history**.
  - Tablero de **Lots/Serial Numbers**.

---

## 5. Referencia de imágenes (saas‑18.4)

La doc oficial de Odoo saas‑18.4 (`Reassign lot/serial numbers`) incluye capturas para:

- El formulario de producto al cambiar el tipo de tracking.
- La pantalla de **Update Quantity** poniendo el stock en 0.
- El nuevo ajuste con **Lot/Serial Number** rellenado.
- El uso del botón **History**.

Para integrarlas como en otros recursos:

1. Abrir  
   `https://www.odoo.com/documentation/saas-18.4/es/applications/inventory_and_mrp/inventory/product_management/product_tracking/reassign.html`
2. Inspeccionar cada imagen y copiar su URL (`/documentation/saas-18.4/_images/...`).
3. Descargar a `knowledge/docs/batches-and-serial-numbers/imgs/`, por ejemplo:

```bash
cd knowledge/docs/batches-and-serial-numbers
mkdir -p imgs
curl -o imgs/reassign-update-quantity.png "https://www.odoo.com/documentation/saas-18.4/_images/reassign-update-quantity.png"
```

4. Referenciar en este MD:

```markdown
![Ajuste de inventario para reasignar lotes](imgs/reassign-update-quantity.png)
```

Con esto tendrás una guía clara y actualizada para realizar la **migración de stock sin tracking → con lotes/series** en Odoo saas‑18.4.

