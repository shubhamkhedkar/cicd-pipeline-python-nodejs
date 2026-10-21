"""Small Flask REST API."""
from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok"), 200

    @app.get("/api/greet")
    def greet():
        name = request.args.get("name", "world")
        return jsonify(message=f"Hello, {name}!"), 200

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
