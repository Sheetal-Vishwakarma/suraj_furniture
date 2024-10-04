from django.core.management.base import BaseCommand
from django.db import connections

class Command(BaseCommand):
    help = 'Generate database schema diagram'

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
        # You can use Graphviz or another library to create the diagram here
        import graphviz

        dot = graphviz.Digraph()
        for table, columns in schema.items():
            dot.node(table)
            for column in columns:
                dot.node(f"{table}.{column}", label=column, shape='box')
                dot.edge(table, f"{table}.{column}")

        dot.render('magento_schema_diagram', format='png', cleanup=True)
