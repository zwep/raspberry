from flask import Flask, render_template
import os
import datetime

app = Flask(__name__, template_folder='template')

@app.route("/")
def hello():
   file_to_csv = os.path.expanduser('~/data/arduino/remote_sensor.csv')
   return render_template('index.html', file_to_csv=file_to_csv)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000, debug=True)