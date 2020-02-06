
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('hello', 'Simple hello World app', version='0.0.1')

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()