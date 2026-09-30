from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello_world_i_am_mk', methods=['GET'])
def hello_world_i_am_mk():
    return jsonify({'message': 'Hello World I am MK'})

if __name__ == '__main__':
    app.run(debug=True)