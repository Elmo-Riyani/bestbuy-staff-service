from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory staff data
staff_data = {}

@app.route('/staff', methods=['POST'])
def create_staff():
    staff = request.json
    staff_id = len(staff_data) + 1
    staff['id'] = staff_id
    staff_data[staff_id] = staff
    return jsonify(staff), 201

@app.route('/staff', methods=['GET'])
def get_all_staff():
    return jsonify(list(staff_data.values())), 200

@app.route('/staff/<int:id>', methods=['GET'])
def get_staff_by_id(id):
    staff = staff_data.get(id)
    if staff:
        return jsonify(staff), 200
    return jsonify({"error": "Staff not found"}), 404

@app.route('/staff/<int:id>', methods=['PUT'])
def update_staff(id):
    if id in staff_data:
        staff_data[id].update(request.json)
        return jsonify(staff_data[id]), 200
    return jsonify({"error": "Staff not found"}), 404

@app.route('/staff/<int:id>', methods=['DELETE'])
def delete_staff(id):
    if id in staff_data:
        deleted_staff = staff_data.pop(id)
        return jsonify(deleted_staff), 200
    return jsonify({"error": "Staff not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
