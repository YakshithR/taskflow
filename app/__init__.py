from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)
    tasks = [
        {"id": 1, "title": "Learn GitHub Actions", "done": False}
    ]

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.get("/tasks")
    def list_tasks():
        return jsonify(tasks), 200

    @app.post("/tasks")
    def create_task():
        data = request.get_json(silent=True) or {}
        title = data.get("title", "").strip()
        if not title:
            return jsonify({"error": "title is required"}), 400

        task = {
            "id": max((item["id"] for item in tasks), default=0) + 1,
            "title": title,
            "done": False,
        }
        tasks.append(task)
        return jsonify(task), 201

    @app.patch("/tasks/<int:task_id>")
    def update_task(task_id):
        task = next((item for item in tasks if item["id"] == task_id), None)
        if task is None:
            return jsonify({"error": "task not found"}), 404

        data = request.get_json(silent=True) or {}
        if "title" in data:
            title = str(data["title"]).strip()
            if not title:
                return jsonify({"error": "title cannot be empty"}), 400
            task["title"] = title
        if "done" in data:
            if not isinstance(data["done"], bool):
                return jsonify({"error": "done must be a boolean"}), 400
            task["done"] = data["done"]

        return jsonify(task), 200

    @app.delete("/tasks/<int:task_id>")
    def delete_task(task_id):
        task = next((item for item in tasks if item["id"] == task_id), None)
        if task is None:
            return jsonify({"error": "task not found"}), 404
        tasks.remove(task)
        return "", 204

    return app
