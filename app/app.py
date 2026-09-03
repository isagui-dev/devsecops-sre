from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Simulación de falla de seguridad (SAST)
DB_PASSWORD = "SuperSecretPassword123!"

# Métrica SRE
REQUEST_COUNT = Counter('http_requests_total', 'Total de peticiones HTTP', ['method', 'endpoint', 'status'])

@app.route('/')
def home():
    REQUEST_COUNT.labels(method='GET', endpoint='/', status='200').inc()
    return jsonify({"status": "healthy", "message": "DevSecOps & SRE App Running"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # nosec B104