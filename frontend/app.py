from flask import Flask, request, send_file, jsonify, render_template
import serial

app = Flask(__name__)

resource_locations = {'1234': [34.026213, -118.2877316]}

resource_info = {}

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

@app.route('/')
def index():
    return render_template('index.html', title='Welcome')

@app.route("/resource")
def resource():
    return render_template('resource.html')

@app.route("/coordinates")
def coordinates():
    site_id = request.args.get('id')
    print("ID:" + site_id)
    return jsonify({'lat': resource_locations[site_id][0], 'lng': resource_locations[site_id][1]})

@app.route("/command", methods=['GET', 'POST'])
def command():
    if request.method == 'GET':
        return render_template('command.html')
    elif request.method == 'POST':
        recv_data = request.json

        data_as_text = ""

        for pair in recv_data:
            data_as_text += str(pair[0]) + "," + str(pair[1]) + ";"

        bytes_rep = data_as_text.encode()

        ser.write(bytes_rep)

        return "success"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")