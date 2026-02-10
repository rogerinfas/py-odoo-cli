import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from odoo_cli import OdooClient

def main():
    try:
        client = OdooClient()
        client.connect()
        
        # RUC to delete
        ruc = '10425620687'
        
        print(f"🔍 Searching for partner with RUC: {ruc}...")
        
        partners = client.search_read(
            'res.partner',
            domain=[['vat', '=', ruc]],
            fields=['id', 'name', 'vat']
        )
        
        if not partners:
            print("❌ No partner found with that RUC.")
            return

        for partner in partners:
            print(f"⚠️  Found partner: {partner['name']} (ID: {partner['id']})")
            
            # Confirm deletion (safety check for interactive use, though we'll force it here for user request)
            # In a real interactive script we'd ask for input, but this is a specific request.
            
            print(f"🗑️  Deleting partner ID {partner['id']}...")
            try:
                result = client.unlink('res.partner', [partner['id']])
                if result:
                    print("✅ Partner deleted successfully.")
                else:
                    print("❌ Failed to delete partner (Odoo returned False).")
            except Exception as e:
                print(f"❌ Error deleting partner: {e}")
                print("   (Note: You cannot delete a partner if they are linked to existing invoices or entries.)")

    except Exception as e:
        print(f"❌ Critical error: {e}")

if __name__ == "__main__":
    main()
