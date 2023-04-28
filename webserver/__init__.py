from flask import Flask, send_from_directory

app = Flask(__name__)

import webserver.views
app.run(host='0.0.0.0', port=80)