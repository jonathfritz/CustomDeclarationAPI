class InvalidJSONError(Exception):
    def __init__(self, schema_file):
        super().__init__(f"Invalid JSON in {schema_file}.")

