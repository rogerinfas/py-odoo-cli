import xmlrpc.client
import ssl
from .config import Config

class OdooClient:
    def __init__(self):
        Config.validate()
        self.url = Config.ODOO_URL
        self.db = Config.ODOO_DB
        self.username = Config.ODOO_USER
        self.password = Config.ODOO_PASSWORD
        self.uid = None
        
        # Create unverified context to avoid SSL errors with self-signed certs or old servers
        self.context = ssl._create_unverified_context()

    def connect(self):
        """Authenticate with Odoo and retrieve UID."""
        try:
            common = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/common', context=self.context)
            self.uid = common.authenticate(self.db, self.username, self.password, {})
            if not self.uid:
                raise PermissionError("Authentication failed. Check your credentials.")
            return self.uid
        except Exception as e:
            raise ConnectionError(f"Could not connect to Odoo: {e}")

    def execute(self, model, method, *args, **kwargs):
        """Execute a method on an Odoo model."""
        if not self.uid:
            self.connect()
            
        models = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/object', context=self.context)
        try:
            return models.execute_kw(
                self.db, self.uid, self.password,
                model, method,
                args, kwargs
            )
        except xmlrpc.client.Fault as e:
            raise RuntimeError(f"Odoo Fault: {e}")
        except Exception as e:
            raise RuntimeError(f"Execution error: {e}")

    def search_read(self, model, domain=None, fields=None, limit=None, offset=0, order=None):
        """Helper for search_read method."""
        domain = domain or []
        kwargs = {}
        if fields: kwargs['fields'] = fields
        if limit: kwargs['limit'] = limit
        if offset: kwargs['offset'] = offset
        if order: kwargs['order'] = order
        
        return self.execute(model, 'search_read', domain, **kwargs)

    def create(self, model, vals):
        """Helper to create a record."""
        return self.execute(model, 'create', [vals])

    def write(self, model, ids, vals):
        """Helper to update records."""
        return self.execute(model, 'write', [ids, vals])

    def unlink(self, model, ids):
        """Helper to delete records."""
        return self.execute(model, 'unlink', [ids])
