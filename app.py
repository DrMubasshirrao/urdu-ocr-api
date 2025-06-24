from flask import Flask, request, jsonify
import easyocr
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

reader = easyocr.Reader(['ur', 'en', 'ar', 'hi'])

@app.route('/ocr', methods=['POST'])
def ocr_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    result = reader.readtext(image.read())

    text = ' '.join([item[1] for item in result])
    return jsonify({'text': text})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
