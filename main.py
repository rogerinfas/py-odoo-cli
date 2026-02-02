#!/usr/bin/env python3
import argparse
import sys
from odoo_cli import OdooClient

def main():
    parser = argparse.ArgumentParser(description="CLI tool to interact with Odoo via XML-RPC")
    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    # Command: test_connection
    subparsers.add_parser("test_connection", help="Test connection to Odoo")

    # Command: list
    list_parser = subparsers.add_parser("list", help="List records from a model")
    list_parser.add_argument("model", help="Odoo model name (e.g. res.partner)")
    list_parser.add_argument("--limit", type=int, default=10, help="Limit results")
    list_parser.add_argument("--fields", help="Comma separated fields (e.g. name,email)")

    # Command: list_modules
    subparsers.add_parser("list_modules", help="List installed modules")

    # Command: list_config
    subparsers.add_parser("list_config", help="List system parameters")

    args = parser.parse_args()

    if not args.action:
        parser.print_help()
        sys.exit(1)

    try:
        client = OdooClient()
        
        if args.action == "test_connection":
            uid = client.connect()
            print(f"✅ Automatically connected! User ID: {uid}")
            
        elif args.action == "list":
            fields = args.fields.split(',') if args.fields else ['name']
            records = client.search_read(args.model, fields=fields, limit=args.limit)
            
            print(f"Found {len(records)} records in {args.model}:")
            print("-" * 40)
            for rec in records:
                print(rec)

        elif args.action == "list_modules":
            print("📦 Fetching installed modules...")
            modules = client.search_read(
                'ir.module.module', 
                domain=[['state', '=', 'installed']], 
                fields=['name', 'shortdesc', 'author', 'installed_version'],
                order='name'
            )
            print("-" * 80)
            print(f"{'Name':<30} | {'Version':<15} | {'Description'}")
            print("-" * 80)
            for m in modules:
                name = m.get('name') or ''
                version = m.get('installed_version') or ''
                desc = m.get('shortdesc') or ''
                print(f"{name:<30} | {version:<15} | {desc}")
            print("-" * 80)
            print(f"Total installed modules: {len(modules)}")

        elif args.action == "list_config":
            print("⚙️  Fetching system parameters...")
            params = client.search_read(
                'ir.config_parameter', 
                domain=[], 
                fields=['key', 'value'],
                order='key'
            )
            print("-" * 80)
            print(f"{'Key':<40} | {'Value'}")
            print("-" * 80)
            for p in params:
                key = p.get('key') or ''
                value = p.get('value') or ''
                # Truncate long values
                if len(value) > 50:
                    value = value[:47] + "..."
                print(f"{key:<40} | {value}")
            print("-" * 80)

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
