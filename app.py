import os
import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        conn.close()

        return "return "Version 2 - CI/CD Test""

    except Exception as e:
        return f"Database connection failed: {e}"
