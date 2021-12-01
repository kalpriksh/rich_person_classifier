from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/hello')
def hello():
  return 'hi'

@app.route('/classify_person', methods = ['GET', 'POST'])
def classify_person():
  image_data = request.form['image_data']
  
  response = jsonify(util.classify_image(image_data))
  response.headers.add('Access-Control-Allow-Origin', '*')
  
  return response

if __name__ == "__main__":
  util.load_saved_artifacts()
  app.run(port=5000)