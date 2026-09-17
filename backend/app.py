import os
import re
import sqlite3
import smtplib
from email.message import EmailMessage

from flask import Flask, jsonify, request

app = Flask(__name__)

DATABASE = os.path.join(os.path.dirname(__file__), "messages.db")
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAIL = os.getenv(
    "RECEIVER_EMAIL",
    "jaswanthkatragadda23@gmail.com"
)


def init_database():
    with sqlite3.connect(DATABASE) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@app.route("/api/contact", methods=["POST", "OPTIONS"])
def contact():
    if request.method == "OPTIONS":
        return "", 204

    data = request.get_json(silent=True) or {}

    name = str(data.get("name", "")).strip()
    sender_email = str(data.get("email", "")).strip()
    message = str(data.get("message", "")).strip()

    if not name or not sender_email or not message:
        return jsonify(error="All fields are required."), 400

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", sender_email):
        return jsonify(error="Please enter a valid email address."), 400

    with sqlite3.connect(DATABASE) as connection:
        connection.execute(
            "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
            (name, sender_email, message)
        )

    if EMAIL_USERNAME and EMAIL_PASSWORD:
        email = EmailMessage()
        email["Subject"] = f"Portfolio message from {name}"
        email["From"] = EMAIL_USERNAME
        email["To"] = RECEIVER_EMAIL
        email["Reply-To"] = sender_email
        email.set_content(
            f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message}"
        )

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
                smtp.send_message(email)
        except (smtplib.SMTPException, OSError):
            pass

    return jsonify(message="Message saved successfully."), 201


@app.route("/api/messages", methods=["GET"])
def messages():
    with sqlite3.connect(DATABASE) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute("""
            SELECT id, name, email, message, created_at
            FROM messages
            ORDER BY created_at DESC
        """).fetchall()

    return jsonify([dict(row) for row in rows])


@app.get("/")
def home():
    return jsonify(status="online", message="Portfolio backend is running")


if __name__ == "__main__":
    init_database()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)