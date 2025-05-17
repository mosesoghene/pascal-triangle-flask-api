from flask import Flask, jsonify, request

app = Flask(__name__)

def generate_pascal_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)
        triangle.append(row)
    return triangle

@app.route("/")
def home():
    return jsonify({"success": "Nothing to do here"}), 200


@app.route('/pascal', methods=['GET'])
def pascal_triangle():
    rows_param = request.args.get('rows', default='0')    
    if not rows_param.isdigit(): return jsonify({"error": "'rows' must be a positive integer"}), 400    
    rows = int(rows_param)
    if rows < 1: return jsonify({"error": "Number of rows must be >= 1"}), 400    
    triangle = generate_pascal_triangle(rows)
    return jsonify({"pascal_triangle": triangle})


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Resource not found. Valid endpoints: /pascal",
        "status_code": 404
    }), 404


if __name__ == '__main__': app.run(host='0.0.0.0', port=10000, debug=False)