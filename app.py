from flask import Flask, jsonify, request

app = Flask(__name__)

# Example macro version data
macro_versions = {
    "Launcher": "1.0.0",
    "Challenges": "1.0.0",
    "SpringPortal": "1.0.0",
    "springdušan": "1.0.0",
}

@app.route("/macros")
def macros():
    """
    Returns all macros if no query is provided.
    Returns a specific macro version if ?name=MacroName is given.
    """
    macro_name = request.args.get("name")
    if macro_name:
        version = macro_versions.get(macro_name)
        if version:
            return jsonify({macro_name: version})
        else:
            return jsonify({"error": "Macro not found"}), 404
    else:
        return jsonify({"macros": macro_versions})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
