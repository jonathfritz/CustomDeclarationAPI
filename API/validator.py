
from flask import jsonify
import json
from lxml import etree
from jsonschema import validate, ValidationError
from lxml.etree import XMLSchemaParseError
from Schema_loader import load_json_schema, load_xml_schema

# Assuming the schemas are loaded elsewhere and passed to the validator functions
def validate_json(file, json_schema):
    try:
        data = json.load(file)
        validate(instance=data, schema=json_schema)
        return jsonify({"message": "JSON file is valid"}), 200
    except ValidationError as ve:
        return jsonify({"error": "JSON validation error", "details": str(ve)}), 422

def validate_xml(file, xml_validator):
    try:
        doc = etree.parse(file)
        xml_validator.assertValid(doc)
        return jsonify({"message": "XML file is valid"}), 200
    except XMLSchemaParseError as xe:
        return jsonify({"error": "XML validation error", "details": str(xe)}), 422