import os
from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST', 'db'),
        user=os.getenv('DB_USER', 'user'),
        password=os.getenv('DB_PASSWORD', 'password'),
        database=os.getenv('DB_NAME', 'testdb')
    )

@app.route('/')
def health_check():
    return jsonify({"status": "healthy", "message": "API activa"}), 200

@app.route('/db-test')
def db_test():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"status": "success", "db": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000) # nosec B104

=======
    app.run(host='0.0.0.0', port=5000)  # nosec B104
>>>>>>> f287598 (fix(security): resolve all local security changes for bandit and trivy)
