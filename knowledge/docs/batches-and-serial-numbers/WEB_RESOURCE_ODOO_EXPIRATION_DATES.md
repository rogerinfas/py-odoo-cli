---
title: Fechas de vencimiento en Odoo saas‑18.4
source: https://www.odoo.com/documentation/saas-18.4/es/applications/inventory_and_mrp/inventory/product_management/product_tracking/expiration_dates.html
---

# Fechas de vencimiento

En Odoo se pueden usar **fechas de vencimiento (expiration dates)** para gestionar el ciclo de vida de productos **perecederos**:

- Reducen pérdidas por productos que caducan sin control.
- Evitan enviar productos caducados a los clientes.
- Permiten planificar mejor la rotación de inventario.

Las fechas de caducidad solo pueden usarse en productos que se gestionan con **lotes** o **números de serie**.  
Una vez que se asigna un lote o número de serie, se puede configurar su **información de caducidad**.

> Referencias relacionadas:
> - [Lot numbers — Odoo saas‑18.4](https://www.odoo.com/documentation/saas-18.4/es/applications/inventory_and_mrp/inventory/product_management/product_tracking/lots.html)
> - [Serial numbers — Odoo saas‑18.4](https://www.odoo.com/documentation/saas-18.4/es/applications/inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers.html)

---

## 1. Activar fechas de vencimiento

1. Ir a `Inventario ‣ Configuración ‣ Ajustes`.
2. En **Trazabilidad**:
   - Activar **Lotes y números de serie (Lots & Serial Numbers)**.
   - Activar **Fechas de vencimiento (Expiration Dates)**.
3. (Opcional) Activar:
   - **Mostrar lotes y números de serie en notas de entrega**.
4. Guardar.

Estas opciones ayudan a tener trazabilidad de principio a fin y facilitan la gestión de recalls y lotes defectuosos.

---

## 2. Configurar fechas de caducidad en productos

Una vez activadas **Expiration Dates** y **Lots & Serial Numbers**, se configura producto por producto.

1. Ir a `Inventario ‣ Productos ‣ Productos`.
2. Seleccionar un producto.
3. Pestaña **Información general**:
   - El **Tipo de producto** debe ser un producto almacenable (Goods).
   - Activar **Seguir inventario (Track Inventory)**.
4. En el campo de tracking, elegir **By Lots** o **By Unique Serial Number**.
5. Ir a la pestaña **Inventario**:
   - Sección **Trazabilidad (Traceability)** → marcar **Fecha de caducidad / Expiration Date**.
   - Aparecerá el bloque **Fechas (Dates)**.

### 2.1. Campos del bloque `Dates`

En saas‑18.4 hay cuatro campos clave:

- **Expiration Date**:
  - Número de días después de recibir/fabricar en los que el producto se considera inseguro para uso/consumo.
- **Best Before Date**:
  - Número de días **antes** de la expiración en que el producto empieza a deteriorarse, pero no es aún peligroso.
- **Removal Date**:
  - Número de días antes de la fecha de expiración en los que el producto debe retirarse del stock.
- **Alert Date**:
  - Número de días antes de la expiración en los que se genera una alerta para ese lote/número de serie.

Los valores de estos campos se usan para calcular automáticamente las fechas en cada entrada al stock (compras y fabricación).

> Nota: Si el producto ya tenía stock antes de activar tracking por lote/serie, puede ser necesario un ajuste de inventario o el flujo de reasignación para asignar lotes y fechas al stock existente.

---

## 3. Establecer fechas de caducidad al recibir productos

Se pueden generar fechas de caducidad para bienes **entrantes** directamente desde la **Recepción**.

1. Crear y confirmar una orden de compra en la app **Compras**.
2. Pulsar el botón inteligente **Recepción** para abrir el albarán.

> Importante: Validar sin asignar lote/número de serie provocará un error; primero hay que registrar el lote o número de serie.

Desde el albarán:

1. Pulsar **Detalles (Details)** en la línea del producto.
2. En el popup **Operaciones detalladas (Detailed Operations)**:
   - Asignar **Lote/Número de serie**.
   - Odoo calculará automáticamente la **Expiration Date**, **Best Before**, etc., según el bloque `Dates` del producto.
   - Si no se configuraron fechas en el producto, se pueden escribir manualmente.
3. Marcar la **Cantidad hecha**.
4. Guardar y luego **Validar**.

Tras validar:

- El botón **Trazabilidad (Traceability)** muestra un reporte donde se ve:
  - Documento de referencia.
  - Producto.
  - Lote/Número de serie.
  - Fechas asociadas.

---

## 4. Fechas de caducidad en productos fabricados

Para productos fabricados en Odoo:

1. Ir a `Fabricación ‣ Operaciones ‣ Órdenes de fabricación`.
2. Crear un **Manufacturing Order (MO)** y seleccionar:
   - **Producto**.
   - **Cantidad a producir**.
3. Confirmar el MO.
4. Asignar **Lote/Número de serie** a la producción (se pueden crear nuevos).

En el lote/número de serie resultante:

1. Abrir el formulario del lote (icono de enlace externo).
2. En la pestaña **Fechas (Dates)** se verán:
   - Expiration Date.
   - Best Before Date.
   - Removal Date.
   - Alert Date.

Estas fechas se calculan según el bloque `Dates` del producto, pero siempre pueden ajustarse manualmente.

---

## 5. Vender productos con fechas de caducidad

El flujo de venta es el estándar con algunas consideraciones:

1. Crear una **cotización** en la app **Ventas**.
2. Añadir:
   - Cliente.
   - Productos con expiración.
   - Cantidades.
3. Confirmar la orden.
4. Pulsar el botón inteligente **Entrega** y validar la salida.

Puntos clave:

- La ubicación donde se almacena el producto debe tener estrategia de remoción **FEFO** (First Expired, First Out).
- Si no hay cantidad suficiente en un lote, Odoo tomará el resto del siguiente lote con fecha de caducidad más próxima.
- Si la entrega se hace antes del **Alert Date**, no se muestran alertas.

---

## 6. Ver fechas de caducidad y alertas

### 6.1. Vista consolidada por fecha de expiración

1. Ir a `Inventario ‣ Productos ‣ Lotes/Números de serie`.
2. Quitar filtros por defecto.
3. Usar **Agrupar por → Agregar grupo personalizado → Expiration Date**.

Obtendrás un desglose de:

- Todos los lotes con expiración.
- Sus fechas.
- Productos y cantidades asociadas.

> Truco: en la vista de lista, habilita la columna **Expiration Date** desde el icono de ajustes de columnas.

### 6.2. Alertas y notificaciones de caducidad

Para ver **alertas de caducidad**:

1. Ir a `Inventario ‣ Productos ‣ Lotes/Números de serie`.
2. Abrir un lote/número de serie.
3. En la pestaña **Fechas**, revisar:
   - Expiration Date.
   - Alert Date.

Si la Expiration Date ya pasó, verás un mensaje de **alerta de caducidad** en la parte superior del formulario.

Para listar solo lotes con alerta:

1. Volver al tablero de `Lotes/Números de serie`.
2. Quitar filtros.
3. Usar **Filtros → Expiration Alerts**.

Odoo también permite enviar notificaciones a un **Responsible** configurado en el producto, cuando se superan estas fechas (según la doc saas‑18.4).

---

## 7. Referencia de imágenes (saas‑18.4)

La doc de Odoo saas‑18.4 sobre **Expiration dates** incluye capturas para:

- Activar **Lots & Serial Numbers** y **Expiration Dates**.
- Configurar el bloque `Dates` en el formulario de producto.
- Ver las fechas en el formulario de lote/número de serie.
- Agrupar por fecha de expiración y ver alertas.

Para tenerlas en local:

1. Abrir  
   `https://www.odoo.com/documentation/saas-18.4/es/applications/inventory_and_mrp/inventory/product_management/product_tracking/expiration_dates.html`
2. Inspeccionar cada imagen y copiar su URL (`/documentation/saas-18.4/_images/...`).
3. Descargar a `knowledge/docs/batches-and-serial-numbers/imgs/`, por ejemplo:

```bash
cd knowledge/docs/batches-and-serial-numbers
mkdir -p imgs
curl -o imgs/expiration-dates-setting.png "https://www.odoo.com/documentation/saas-18.4/_images/expiration-dates-setting.png"
```

4. Usar rutas relativas en este MD:

```markdown
![Configuración de fechas de vencimiento](imgs/expiration-dates-setting.png)
```

Así mantienes la documentación alineada con **Odoo saas‑18.4** y el mismo patrón de imágenes que en `WEB_RESOURCE_CERTIFICADO_DIGITAL_SUNAT.md`.

