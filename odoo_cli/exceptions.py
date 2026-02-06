"""
Excepciones propias de py-odoo-cli para un manejo de errores predecible.

Jerarquía:
- OdooClientError (base)
  - OdooConfigError   (configuración faltante o inválida)
  - OdooConnectionError (conexión/autenticación)
  - OdooFaultError    (error devuelto por el servidor Odoo)
  - OdooExecutionError (fallo genérico en execute)
"""


class OdooClientError(Exception):
    """Error base de la biblioteca. Todas las excepciones propias heredan de esta."""

    pass


class OdooConfigError(OdooClientError, ValueError):
    """Faltan variables de entorno o la configuración es inválida."""

    pass


class OdooConnectionError(OdooClientError, ConnectionError):
    """No se pudo conectar a Odoo o la autenticación falló."""

    pass


class OdooFaultError(OdooClientError, RuntimeError):
    """Error devuelto por el servidor Odoo (xmlrpc.client.Fault)."""

    def __init__(self, message: str, fault_code: int | None = None, fault_string: str | None = None):
        super().__init__(message)
        self.fault_code = fault_code
        self.fault_string = fault_string


class OdooExecutionError(OdooClientError, RuntimeError):
    """Error durante la ejecución de un método en Odoo (red, timeout, etc.)."""

    pass
