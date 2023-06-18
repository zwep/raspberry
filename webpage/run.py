from flask import Flask, render_template, send_file
import os
import datetime
from flask_cors import CORS

app = Flask(__name__, template_folder='template')
CORS(app, origins='http://localhost:8000')


@app.route('/data/arduino/remote_sensor.csv')
def serve_csv():
    csv_path = '~/data/arduino/remote_sensor.csv'  # Replace with the actual path to your CSV file
    csv_path = os.path.expanduser(csv_path)
    return send_file(csv_path, mimetype='text/csv')


@app.route("/")
def hello():
   file_to_csv = os.path.expanduser('/data/arduino/remote_sensor.csv')
   return render_template('index.html', file_to_csv=file_to_csv)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000, debug=True)
