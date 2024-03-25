import json
from lxml import etree
from lxml.etree import XMLSchema
from API.ExceptionHandling.InvalidJSONError import InvalidJSONError
from API.ExceptionHandling.JSONSchemaNotFoundError import JSONSchemaNotFoundError
from API.ExceptionHandling.XMLSchemaLoadError import XMLSchemaLoadError


def load_json_schema(schema_file):
    try:
        with open(schema_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise JSONSchemaNotFoundError(schema_file)
    except json.JSONDecodeError:
        raise InvalidJSONError(schema_file)

def load_xml_schema(schema_file):
    try:
        with open(schema_file, "rb") as file:
            xml_schema_doc = etree.parse(file)
            return XMLSchema(xml_schema_doc)
    except Exception as e:  # Consider catching more specific exceptions if possible
        raise XMLSchemaLoadError(f"Error loading XML Schema from {schema_file}: {str(e)}")