from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

tasks = []
next_id = 1


@app.route('/add', methods=['POST'])
def add_task():
    global next_id

    data = request.get_json()
    task_name = data.get('task', '').strip()

    if not task_name:
        return jsonify({"error": "Task name is required"}), 400

    task = {
        "id": next_id,
        "name": task_name,
        "done": False,
        "time": datetime.now().strftime("%d %b %Y, %H:%M")
    }

    tasks.append(task)
    next_id += 1

    return jsonify({"message": "Task added", "task": task})


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


@app.route('/delete', methods=['POST'])
def delete_task():
    global tasks

    data = request.get_json()
    task_id = data.get('id')

    task_exists = any(t["id"] == task_id for t in tasks)

    if not task_exists:
        return jsonify({"error": "Task not found"}), 404

    tasks = [t for t in tasks if t["id"] != task_id]

    return jsonify({"message": "Task deleted"})


@app.route('/toggle', methods=['POST'])
def toggle_task():
    data = request.get_json()
    task_id = data.get('id')

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            return jsonify({"message": "Task updated", "task": task})

    return jsonify({"error": "Task not found"}), 404


@app.route('/edit', methods=['POST'])
def edit_task():
    data = request.get_json()
    task_id = data.get('id')
    new_name = data.get('name', '').strip()

    if not new_name:
        return jsonify({"error": "Task name is required"}), 400

    for task in tasks:
        if task["id"] == task_id:
            task["name"] = new_name
            return jsonify({"message": "Task edited", "task": task})

    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
