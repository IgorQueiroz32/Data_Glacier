from flask import Flask

app = Flask(__name__)

@app.route('/data_glacier/flask') # endpoint
def presentation():
    return "Hi, my name is Igor and I am a data analyst"

app.run(port=5000)