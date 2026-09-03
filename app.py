import pymysql
import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    usuarios = []
    try:
        conn = pymysql.connect(
            host='db',
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )
        conn.close()
        db_status = "Connected to the database successfully."
    except Exception as e:
        app.logger.error(f"DB connection error: {e}")
        db_status = "Error connecting to the database."

    return render_template('index.html', db_status=db_status, usuarios=usuarios)

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=5050, debug=debug_mode)  # nosec B104