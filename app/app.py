"""HTTP-приложение для проверки CI."""
from flask import Flask, jsonify


def create_app():
    """Создаёт приложение."""
    application = Flask(__name__)

    @application.get("/health")
    def health():
        """Возвращает состояние приложения."""
        return jsonify(status="ok")

    @application.get("/")
    def index():
        """Возвращает имя и версию приложения."""
        return jsonify(
            service="devops-ci-app",
            version="1.0.0",
            status="running",
        )

    return application


app = create_app()
