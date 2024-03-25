from flask import Flask, request, jsonify
from Schema_loader import load_json_schema, load_xml_schema
from validator import validate_json, validate_xml

app = Flask(__name__)

# Load schemas (still example paths, not correct vor custom declarations)
json_schema = load_json_schema("../Schemas/JsonSchemaCustomDeclaration.json")
xml_validator = load_xml_schema("../Schemas/XMLSchemaCustomDeclaration.xsd")

@app.route("/validate", methods=["POST"])
def validate_file():
    file = request.files["file"]
    if not file:
        return jsonify({"error": "No file provided"}), 400

    if file.filename.lower().endswith(".json"):
        return validate_json(file, json_schema)
    elif file.filename.lower().endswith(".xml"):
        return validate_xml(file, xml_validator)
    else:
        return jsonify({"error": "Unsupported file type"}), 400

if __name__ == "__main__":
    app.run(debug=True)