import unittest
from unittest.mock import patch, MagicMock
from odoo_cli.client import OdooClient

class TestOdooClient(unittest.TestCase):
    @patch('odoo_cli.client.Config')
    @patch('xmlrpc.client.ServerProxy')
    def test_connect(self, mock_server, mock_config):
        # Setup mock config
        mock_config.ODOO_URL = 'http://test'
        mock_config.ODOO_DB = 'db'
        mock_config.ODOO_USER = 'user'
        mock_config.ODOO_PASSWORD = 'pass'
        mock_config.ODOO_VERIFY_SSL = False
        
        # Setup mock XML-RPC
        mock_common = MagicMock()
        mock_common.authenticate.return_value = 1
        mock_server.return_value = mock_common
        
        client = OdooClient()
        uid = client.connect()
        
        self.assertEqual(uid, 1)
        mock_common.authenticate.assert_called_with('db', 'user', 'pass', {})

if __name__ == '__main__':
    unittest.main()
