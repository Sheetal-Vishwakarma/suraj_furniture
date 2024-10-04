from django.core.management.base import BaseCommand
from django.db import connections
import graphviz

class Command(BaseCommand):
    help = 'Generate a database diagram for Magento'

    def handle(self, *args, **kwargs):
        cursor = connections['default'].cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        schema = {}
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SHOW COLUMNS FROM {table_name}")
            columns = cursor.fetchall()
            schema[table_name] = [column[0] for column in columns]

        self.create_diagram(schema)

    def create_diagram(self, schema):
        dot = graphviz.Digraph()

        for table, columns in schema.items():
            dot.node(table, label=table)
            for column in columns:
                dot.node(f"{table}.{column}", label=column, shape='box')
                dot.edge(table, f"{table}.{column}")

        dot.render('magento_database_diagram', format='png', cleanup=True)
        self.stdout.write(self.style.SUCCESS('Database diagram generated successfully!'))
