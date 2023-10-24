from flask import Flask, jsonify

# Start virtual env - planetary-api\scripts\activate
# flask --app app.py --debug run

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Helo World'


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the Planetary API. Boo yah woo yah')


@app.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found'), 404
# Explicit code - 404 (200 is default)


if __name__ == '__main__':
    app.run()

