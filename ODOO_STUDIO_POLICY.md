# Política estricta sobre Odoo Studio

Este documento establece, de forma inequívoca, la **prohibición absoluta** del uso de **Odoo Studio** en el contexto de este repositorio y de cualquier trabajo derivado del mismo.

---

## 1. Alcance

Esta política aplica a:

- Cualquier instancia de Odoo (producción, preproducción, QA, desarrollo, pruebas, sandbox, etc.) que se gestione, administre o automatice con ayuda de este repositorio (`py-odoo-cli`) o de scripts ubicados en la carpeta `knowledge/`.
- Cualquier persona (usuarios funcionales, técnicos, consultores internos o externos) que utilice este código, directa o indirectamente.

---

## 2. Prohibición explícita

Queda **terminantemente prohibido**:

- Instalar, activar o configurar el módulo **Odoo Studio** (`web_studio`) en las bases de datos gestionadas con este proyecto.
- Utilizar Odoo Studio para:
  - Crear o modificar modelos, campos, vistas, acciones, flujos, reportes o cualquier otro artefacto.
  - Ajustar o sobreescribir lógica de negocio existente.
- Ejecutar scripts, automatizaciones o procedimientos que, directa o indirectamente, instalen o reactiven `web_studio`.

Esta prohibición es **una orden directa de la dirección funcional/técnica** responsable del uso de Odoo en la organización.

---

## 3. Responsabilidades

- **Usuarios funcionales**: No deben, bajo ninguna circunstancia, activar Odoo Studio desde la interfaz web ni solicitar a terceros que lo hagan.
- **Desarrolladores y administradores técnicos**:
  - No deben incluir en sus desarrollos nada que requiera Odoo Studio.
  - Deben revisar que las instancias sobre las que trabajen **no tengan `web_studio` instalado y en estado `installed` o equivalente**.
  - Deben informar inmediatamente si detectan que Odoo Studio se ha instalado o utilizado en alguna base de datos bajo su responsabilidad.

---

## 4. Actuación en caso de incumplimiento

Si se detecta que Odoo Studio ha sido instalado o utilizado en una instancia cubierta por esta política:

1. Se debe **notificar de inmediato** al responsable técnico/funcional designado.
2. Se evaluará el impacto de las personalizaciones creadas con Odoo Studio.
3. Se definirán las acciones para:
   - Desinstalar Odoo Studio o
   - Reconducir las personalizaciones a código estándar/controlado fuera de Studio,
   según las políticas internas de la organización.

---

## 5. Referencia en la documentación

Esta política está referenciada también en `README.md` para que cualquier persona que use `py-odoo-cli` conozca de antemano:

- Que **Odoo Studio está totalmente vetado** en este proyecto.
- Que cualquier solicitud de activación/uso de Odoo Studio contraviene explícitamente esta política.

---

## 6. Revisión y cambios

Cualquier modificación de esta política:

- Debe ser aprobada explícitamente por la dirección funcional/técnica responsable de Odoo.
- Debe quedar registrada mediante un cambio de este archivo y su correspondiente control de versiones (commit con justificación clara).

Hasta que exista una modificación formal, esta versión es de **cumplimiento obligatorio**.

