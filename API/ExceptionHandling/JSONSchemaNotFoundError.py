class JSONSchemaNotFoundError(Exception):
    def __init__(self, schema_file):
        super().__init__(f"JSON Schema file {schema_file} not found.")