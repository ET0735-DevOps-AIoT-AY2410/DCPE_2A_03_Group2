from flask import Flask, jsonify
import picammers  # Assuming your functions are in this module

app = Flask(__name__)

@app.route('/capture', methods=['GET'])
def capture_and_decode():
    picam2 = picammers.initialize_picam()
    file_path = picammers.capture_image(picam2)
    barcode_data = picammers.decode_barcode(file_path)
    picammers.close_picam(picam2)
    return jsonify({'barcode_data': barcode_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
